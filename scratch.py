import json
import re
from typing import Optional, List, Tuple
from enum import StrEnum
from collections import OrderedDict

import rich
from langchain_openai import ChatOpenAI
from langchain.chat_models.base import BaseChatModel
from pydantic import BaseModel
from langchain_core.messages import HumanMessage, SystemMessage
from dotenv import load_dotenv

load_dotenv()


class PydanticOutputtingSingleTurnChat:
    def __init__(
        self,
        chat: BaseChatModel,
        system_prompt: str,
        output_model: BaseModel,
        n_retries: int = 3,
    ):
        self.chat = chat
        self.system_prompt = system_prompt
        self.output_model = output_model
        self.n_retries = n_retries

    def extract_json(self, response_str: str) -> str:
        """Extracts the first valid JSON object from a string using regex."""
        json_pattern = r"\{.*?\}"
        match = re.search(json_pattern, response_str, re.DOTALL)
        if match:
            return match.group(0)
        raise ValueError("No valid JSON found in response")

    def __call__(self, message: str) -> Optional[Tuple[str, BaseModel]]:
        """Invoke the chat with a human message and return the response content alongside
        the extracted and parsed Pydantic `BaseModel` object.
        """
        messages = [
            SystemMessage(content=self.system_prompt),
            HumanMessage(content=message),
        ]
        for _ in range(self.n_retries):
            response_content = self.chat.invoke(messages).content
            try:
                raw_json_str = self.extract_json(response_content)
                output_object = self.output_model(**json.loads(raw_json_str))
                return response_content, output_object
            except Exception as e:
                print(e)
        raise ValueError("No valid JSON found in response")


class BooleanResponse(BaseModel):
    reasoning: str
    decision: bool


class AtomicityClassifier:

    SYSTEM_PROMPT = r"""
Your job is to decide if a task is atomically scoped such that it is feasible to accomplish with a short, intuitive Mineflayer JS script (or if not, would be better off broken down further into subtasks).

For example, the Minecraft task, "Gather basic resources (wood, stone) to craft tools" is not atomic, as it can (and should) be broken down into subtasks like "Locate a tree", "Break the tree's wood blocks", etc. The task is only sufficiently atomic if it truly is _one_ low-level, short horizon thing.

Your output must follow this JSON format:
{
    "reasoning": "...",
    "decision": true/false
}

If yes (the task is sufficiently atomic and immediately feasible), your decision should be 'true'. Otherwise, your decision should be 'false'. In either case, briefly explain your reasoning in the 'reasoning' field.
"""  # TODO: Would Pydantic AI use `Response.model_json_schema()` here?

    USER_PROMPT_TEMPLATE = """
CURRENT ENVIRONMENT STATE:
{env_state}

THE TASK:
{task}
"""

    def __init__(self, chat: BaseChatModel):
        self.get_parsed_response = PydanticOutputtingSingleTurnChat(
            chat=chat,
            system_prompt=self.SYSTEM_PROMPT,
            output_model=BooleanResponse,
        )

    def __call__(self, task: str, env_state: str) -> bool:
        user_prompt = self.USER_PROMPT_TEMPLATE.format(env_state=env_state, task=task)
        try:
            result = self.get_parsed_response(user_prompt)
        except ValueError:
            raise NotImplementedError(
                "No implementation for when AtomicityClassifier fails to give a parsable response"
            )
        output_object: BooleanResponse = result[1]
        return output_object.decision


class PlanResponse(BaseModel):
    task_descriptions: List[str]


class Planner:
    SYSTEM_PROMPT = """Your job is to, given a high-level task, come up with the first or next steps that are most likely to lead to completing the task.

    Crucially, these steps should only be _marginally_ more specific than the input task (i.e., defined at the logical next-most granular level of abstraction).
    
    You will show the current overall hierarchical plan as a JSON. It will then be indicated which task node that you should add one or more further subtasks to. You will also be shown current in-game information. Your answer should consider all of this information.
    
    You should answer by only giving task _descriptions_ (don't worry about anything else). In other words, don't respond with anything but a list of one or more task descriptions, formatted as JSON like so:
    {
        "task_descriptions": ["...", "..."]
    }
    """  # TODO: Change prompt to also handle updating
    USER_PROMPT_TEMPLATE = """
    CURRENT HIERARCHICAL PLAN:
    ```json
    {hierarchical_plan}
    ```
    CURRENT TASK (that you should propose further subtasks for):
    ```json
    {task}
    ```
    CURRENT IN-GAME STATE:
    ```json
    {in_game_state}
    ```
    """

    def __init__(self, chat: BaseChatModel):
        self.get_parsed_response = PydanticOutputtingSingleTurnChat(
            chat=chat,
            system_prompt=self.SYSTEM_PROMPT,
            output_model=PlanResponse,
        )

    def __call__(
        self, hierarchical_plan: dict, task: dict, in_game_state: dict
    ) -> List[str]:
        user_prompt = self.USER_PROMPT_TEMPLATE.format(
            hierarchical_plan=json.dumps(hierarchical_plan),
            task=json.dumps(task),
            in_game_state=json.dumps(in_game_state),
        )
        try:
            result = self.get_parsed_response(user_prompt)
        except ValueError:
            raise NotImplementedError(
                "No implementation for when Planner fails to give a parsable response"
            )
        output_object: PlanResponse = result[1]
        return output_object.task_descriptions


class TaskStatus(StrEnum):
    SUCCESS = "Attempted (success)"
    FAILURE = "Attempted (failure)"
    PARTIAL = "Attempted (partial success)"
    ABORTED = "Aborted"
    IN_PROGRESS = "In progress"
    PLANNED = "Tentatively planned"


class Task(BaseModel):
    task: str
    description: str
    status: TaskStatus
    retrospective: Optional[str] = None
    subtasks: list["Task"] = []


class LlmHtnPolicy:
    def __init__(self, root_task: str, start_env_state: str):
        self.root_task: Task = Task(
            task="1", description=root_task, status=TaskStatus.IN_PROGRESS
        )
        self.current_task: Task = self.root_task
        self.env_state_history: OrderedDict[str, str] = OrderedDict()
        self.env_state_history["1"] = start_env_state
        self.atomicity_classifier = AtomicityClassifier(
            chat=ChatOpenAI(model="gpt-3.5-turbo", temperature=0.5)
        )
        # self.planner = Planner(chat=ChatOpenAI(model="gpt-3.5-turbo", temperature=0.5))
        self.planner = Planner(chat=ChatOpenAI(model="gpt-4o-mini", temperature=0.5))

    def __call__(self):
        current_env_state = next(reversed(self.env_state_history.values()))
        is_atomic = self.atomicity_classifier(
            self.current_task.description, current_env_state
        )
        if not is_atomic:
            new_subtask_descriptions = self.planner(
                hierarchical_plan=self.root_task.model_dump_json(indent=4),
                task=f"{self.current_task.task}: {self.current_task.description}",
                in_game_state=current_env_state,
            )
            new_planned_subtasks = [  # FIXME: Overwrite planned tasks
                Task(
                    task=f"{self.current_task.task}.{i}",
                    description=desc,
                    status=TaskStatus.PLANNED,
                )
                for i, desc in enumerate(new_subtask_descriptions, start=1)
            ]
            self.current_task.subtasks.extend(new_planned_subtasks)
            self.current_task.subtasks[0].status = TaskStatus.IN_PROGRESS
            self.current_task = self.current_task.subtasks[0]
            # rich.print(self.root_task.model_dump())
            self()
        return


# task = "Defeat the Ender Dragon"
task = "Build a village with as many houses as there are unique plant species in your current biome. In each house, there should be a chest containing a single unique item that the other house's chests do not contain. For extra points, use as many distinct wood varieties as you can."
task = "Find 3 nearby villages and count how many farms each village has."
env_state = "You just spawned into a fresh Minecraft world."
policy = LlmHtnPolicy(task, env_state)
policy()
rich.print(policy.root_task.model_dump_json(indent=4))
print()
