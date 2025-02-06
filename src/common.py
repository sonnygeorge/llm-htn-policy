"""Common classes and functions used throughout the project."""

import re
import json
from abc import ABC, abstractmethod
from typing import Optional, Tuple, Type

from pydantic import BaseModel
from langchain.chat_models.base import BaseChatModel
from langchain_core.messages import HumanMessage, SystemMessage


class Task(ABC):
    """Abstract base class for a task."""

    @property
    @abstractmethod
    def description(self) -> str:
        """Description of the task."""
        pass

    @property
    @abstractmethod
    def max_steps(self) -> int:
        """Maximum number of steps allowed for an episode pursuing this task."""
        pass

    @abstractmethod
    def get_human_feedback(
        self, agent: "Agent", inputs: BaseModel, outputs: BaseModel
    ) -> None:
        """Called every time a Policy's agents are called to get and record human feedback
        on a per-agent basis."""
        pass

    @abstractmethod
    def step(self) -> bool:
        """Called after every action execution to (1) calculate and record any important
        variables (e.g., step-by-step reward) and (2) return whether to abort the task
        episode because of something observed in the environment (e.g., an irreversible
        state)."""
        pass

    @abstractmethod
    def finalize(self) -> Tuple[Optional[float], Optional[bool]]:
        """Called after the task-pursuing episode is over, returning final metrics (or
        None if the metric calculations are not implemented).

        Returns:
            Tuple of:
            - (1) the final reward (normalized b/w -1 and 1)
            - (2) the binary success evaluation of the task (True=success & False=fail)
        """
        pass


class EnvState(ABC):
    """Abstract base class for environment state data. The idea is that the environment
    state can be any arbitrary data/data structure, so long as it has a method to convert
    itself into LLM-prompt-appropriate natural language.
    """

    @abstractmethod
    def as_natural_language(self) -> str:
        """Converts the environment state into LLM-prompt-appropriate natural language."""
        pass


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
        input_model: Type[BaseModel],
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
        self.input_model = input_model
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
