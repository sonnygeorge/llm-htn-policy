import re
import json
import os
import importlib
from typing import Dict, Type, Optional

from pydantic import BaseModel
from langchain.chat_models.base import BaseChatModel
from langchain_core.messages import HumanMessage, SystemMessage

from configs import Strings, POLICIES_AND_AGENTS, PromptKws


class Agent:
    """An "agent" in the context of a policy: a single-turn LLM chat that produces some
    `pydantic.BaseModel` output (retrying up to `max_retries` times if the output is not
    parsable as the specified `output_model`).
    """

    def __init__(
        self,
        name: str,
        short_description: str,
        rendered_sys_prompt: str,
        unrendered_user_prompt: str,
        output_model: Type[BaseModel],
        chat_model: BaseChatModel,
        max_retries: int = 2,
    ):
        # Metadata
        self.name = name
        self.short_description = short_description
        # Functional attributes
        self.rendered_sys_prompt = rendered_sys_prompt
        self.unrendered_user_prompt = unrendered_user_prompt
        self.output_model = output_model
        self.chat_model = chat_model
        self.max_retries = max_retries

    def _extract_json(self, string: str) -> str:  # FIXME: Not yet desired behavior
        """Extracts the first valid JSON object from a string using regex."""
        json_pattern = r"\{.*?\}"
        match = re.search(json_pattern, string, re.DOTALL)
        if match:
            return match.group(0)
        raise ValueError("No parsable JSON found in response")

    def invoke(self, input: BaseModel) -> Optional[BaseModel]:
        """Invokes the agent and returns the output model (unless `max_retries` is
        reached with no parsable LLM response, in which case this function returns None.
        """
        user_prompt = self.unrendered_user_prompt.format(**dict(input))
        messages = [
            SystemMessage(content=self.rendered_sys_prompt),
            HumanMessage(content=user_prompt),
        ]
        for _ in range(self.max_retries):
            response_content = self.chat_model.invoke(messages).content
            try:
                raw_json_str = self._extract_json(response_content)
                output_object = self.output_model(**json.loads(raw_json_str))
                return response_content, output_object
            except Exception as e:
                print(e)
        return None


def get_agents_for_policy(policy: str, domain: str) -> Dict[str, Agent]:
    agents = {}
    for agent, config in POLICIES_AND_AGENTS[policy].items():
        # Read in agent's system prompt
        sys_prompt_path = Strings.SYS_PROMPTS_DIR_PATH.format(
            policy=policy, agent=agent
        )
        with open(sys_prompt_path, "r") as f:
            sys_prompt = f.read()

        # Read in agent's user prompt
        user_prompt_path = Strings.USER_PROMPTS_DIR_PATH.format(
            policy=policy, agent=agent
        )
        with open(user_prompt_path, "r") as f:
            unrendered_user_prompt = f.read()

        # Read in domain-specific system prompt addition
        domain_sys_prompt_addition_path = (
            Strings.DOMAIN_SYS_PROMPT_ADDITIONS_DIR_PATH.format(
                domain=domain, policy=policy, agent=agent
            )
        )
        if os.path.exists(domain_sys_prompt_addition_path):
            with open(domain_sys_prompt_addition_path, "r") as f:
                domain_sys_prompt_addition = f.read()
        else:
            domain_sys_prompt_addition = None

        # Render the system prompt with the domain-specific addition
        prompt_kwargs = {
            PromptKws.DOMAIN_SPECIFIC_SYS_PROMPT_ADDITION: domain_sys_prompt_addition
        }
        rendered_sys_prompt = sys_prompt.format(**prompt_kwargs)

        # Import the agent's output model
        agent_output_model_path = Strings.AGENT_OUTPUT_MODEL_MODULE_PATH.format(
            policy=policy
        )
        agent_output_model_module = importlib.import_module(agent_output_model_path)
        agent_output_model_class_name = Strings.get_agent_output_model_class_name(agent)
        output_model: BaseModel = getattr(
            agent_output_model_module, agent_output_model_class_name
        )

        # Instantiate the agent and add it to the dictionary
        agents[agent] = Agent(
            name=config["name"],
            short_description=config["short_description"],
            rendered_sys_prompt=rendered_sys_prompt,
            unrendered_user_prompt=unrendered_user_prompt,
            output_model=output_model,
            chat_model=config["chat_model"],
        )
    return agents
