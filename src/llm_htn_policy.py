from abc import ABC, abstractmethod
from collections import OrderedDict
from dataclasses import dataclass
from enum import StrEnum
from typing import List, Optional


class TaskStatus(StrEnum):
    SUCCESS = "[✅]"  # Executed successfully
    FAILURE = "[❌]"  # Failed
    PARTIAL = "[🤷]"  # Outcome wasn't a "black & white" success/fail (partial success)
    ABANDONED = "[💀]"  # Dropped in favor of a different approach
    IN_PROGRESS = "[⏳]"  # Currently being decomposed/executed
    FUTURE = "[💭]"  # Postulated as a future task


@dataclass
class TaskAttempt:
    """
    Data pertaining to an attempted execution of a task.

    Attributes:
        start (int): Timestamp/step of when the attempt commenced.
        end (int): Timestamp/step of when the attempt concluded.
        analysis (str): Salient details summarizing the attempt—e.g. in what way(s) it was
            successful, why it was given up on, etc.
    """

    start: Optional[int] = None
    end: Optional[int] = None
    analysis: Optional[str] = None


class Task:
    """Node in a hierarchical task network."""

    def __init__(
        self,
        description: str,
        status: TaskStatus,
        parent: Optional["Task"] = None,
        subtasks: Optional[List["Task"]] = None,
        attempt: Optional[TaskAttempt] = None,
    ):
        self.description = description
        self.status = status
        self.parent = parent
        self.subtasks = subtasks if subtasks is not None else []
        self.attempt_summary = attempt if attempt is not None else TaskAttempt()


class EnvState(ABC):
    """Abstract base class for an environment state."""

    @abstractmethod
    def as_natural_language(self) -> str:
        """Converts the environment state to natural language."""
        pass


class LlmHtnPolicy:
    """Policy that infers actions by way of LLM task decomposition and HTN traversal.

    Attributes:
        root (Task): The root task of the hierarchical task network (HTN).
        current_task (Task): The current "task at hand" in the HTN traversal.
        env_state_history (OrderedDict[int, EnvState]): Ordered mapping of
            timestamps/steps to environment states.
    """

    def __init__(self, root_task: Task):
        # TODO: Probably take just the natural language description of the root task
        # TODO: probably take some sort of 'LLM' object and set of prompts
        self.root_task = root_task
        self.current_task = root_task
        self.env_state_history: OrderedDict[int, EnvState] = OrderedDict()

    def _analyze_and_update_current_task_attempt(self) -> None:
        """Uses an LLM to reflect over the most recent attempt at executing the current
        task and updates the task's `status` and `attempt` attributes accordingly.
        """
        pass  # TODO

    def _consider_aborting_directions_of_approach_and_revert_current_task_if_necessary(
        self,
    ) -> None:
        """Uses an LLM to considers whether the current directions of approach are worth
        giving up on. If so, reverts the current task to some parental task (the "drawing
        board" to "return" to), changing the status of intermediate tasks tp `ABANDONED`
        and updating their `attempt.analysis` attributes with explanatory reasoning.
        """
        pass  # TODO: Implement

    def _is_current_task_sufficiently_atomic_for_execution(self) -> bool:
        """Uses an LLM to determine whether the current task is sufficiently atomic for
        execution.
        """
        # FIXME: Eventually remove assert for efficiency
        assert len(self.current_task.subtasks) == 0, "(sign of a redundant call)"
        pass  # TODO: Implement

    def _infer_next_subtask(self) -> None:
        """Uses an LLM to infer a good next subtask for `self.current_task` and updates
        the HTN accordingly.

        TODO: Inferring n tasks will likely be more natural/effient for COT prompts...
              In this case, the non-immediate tasks in an n-task sequence would have the
              `TaskStatus.FUTURE` status, indicating they're postulated as future tasks.
        """
        pass  # TODO: Implement

    def __call__(self, env_state: EnvState):  # FIXME: Return type
        """Infers the next action to take in the environment by way of LLM task
        decomposition and HTN traversal.
        """
        timestamp = len(self.env_state_history)  # FIXME (if ∃ a better alternative)
        self.env_state_history[timestamp] = env_state

        self._analyze_and_update_current_task_attempt()
        if self.current_task.status == TaskStatus.SUCCESS:
            if self.current_task != self.root_task:
                self.current_task = self.current_task.parent  # Move back up in the HTN
            else:
                return "DONE"  # FIXME: Return a more intentional 'done' signal

        self._consider_aborting_directions_of_approach_and_revert_current_task_if_necessary()

        while True:
            if len(self.current_task.subtasks) == 0:  # Prevent redundant calls of below
                if self._is_current_task_sufficiently_atomic_for_execution():
                    return self.current_task  # Current task is ready to be executed

            self._infer_next_subtask()  # Otherwise break the task down further
