from abc import ABC, abstractmethod
from typing import Any, Dict, Optional, Tuple

from pydantic import BaseModel

from agent import Agent


class EnvState(ABC):
    """Abstract base class for environment state data. The idea is that the environment
    state can be any arbitrary data/data structure, so long as it has a method to convert
    itself into LLM-prompt-appropriate natural language.
    """

    @abstractmethod
    def as_natural_language(self) -> str:
        """Converts the environment state into LLM-prompt-appropriate natural language."""
        pass


class Domain(ABC):
    pass  # FIXME


class Task(ABC):
    def __init__(self, domain_interface: Domain):
        pass

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
        self, agent: Agent, inputs: BaseModel, outputs: BaseModel
    ) -> None:
        """Called every time a Policy's agents are called to get and record human feedback
        on a per-agent basis."""
        pass

    @abstractmethod
    def reset(self) -> EnvState:
        pass

    @abstractmethod
    def step(self) -> bool:
        """Called after every action execution to (1) calculate and record any important
        variables (e.g., step-by-step reward) and (2) return whether to drop the task
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


PrimitiveAction = Any  # FIXME


class Policy(ABC):
    # TODO: Implement appropriate equivalent of loss.backward() for Supervised+RL training
    @abstractmethod
    def __init__(self, agents: Dict[str, Agent], task: str):
        pass

    @abstractmethod
    def __call__(self, env_state, task: Task) -> PrimitiveAction:
        pass
