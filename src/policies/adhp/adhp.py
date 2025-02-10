from collections import OrderedDict
from enum import StrEnum
from typing import Dict, Optional

from pydantic import BaseModel

from abstract import EnvState, Policy, PrimitiveAction
from agent import Agent


class TaskStatus(StrEnum):
    SUCCESS = "Attempted (success)"
    FAILURE = "Attempted (failure)"
    PARTIAL = "Attempted (partial success)"
    DROPPED = "Dropped"
    IN_PROGRESS = "In progress"
    PLANNED = "Tentatively planned"


class Task(BaseModel):
    task: str
    description: str
    status: TaskStatus
    retrospective: Optional[str] = None
    subtasks: list["Task"] = []


class Policy(Policy):  # FIXME: Implement
    def __init__(self, agents: Dict[str, Agent], task: str, start_env_state: str):
        self.agents = agents
        self.root_task: Task = Task(
            task="1", description=task, status=TaskStatus.IN_PROGRESS
        )
        self.current_task: Task = self.root_task
        self.env_state_history: OrderedDict[str, str] = OrderedDict()
        self.env_state_history["1"] = start_env_state

    def __call__(self, env_state: EnvState) -> Optional[PrimitiveAction]:
        """...

        Returns:
            Optional[PrimitiveAction]: The action to take next in the environment or None
                if the policy believes the overall task is complete.
        """
        env_state = next(reversed(self.env_state_history.values()))
        is_atomic = False  # TODO
        if not is_atomic:
            current_traversal_str = self.root_task.model_dump_json(indent=4)
            env_state_str = env_state.as_natural_language()
            new_subtask_descriptions = None  # FIXME: Get from the planner
            # new_planned_subtasks = [  # FIXME: Overwrite planned tasks
            #     Task(
            #         task=f"{self.current_task.task}.{i}",
            #         description=desc,
            #         status=TaskStatus.PLANNED,
            #     )
            #     for i, desc in enumerate(new_subtask_descriptions, start=1)
            # ]
            # self.current_task.subtasks.extend(new_planned_subtasks)
            # self.current_task.subtasks[0].status = TaskStatus.IN_PROGRESS
            # self.current_task = self.current_task.subtasks[0]
            # # rich.print(self.root_task.model_dump())
            # self()
