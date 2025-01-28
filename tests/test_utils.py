from src.llm_htn_policy import LlmHtnPolicy, Task, TaskStatus
from src.utils import get_pretty_htn_string


def get_mock_htn_policy_for_htn_pretty_string() -> LlmHtnPolicy:
    root_task = Task(description="Root Task", status=TaskStatus.IN_PROGRESS)
    htn_traversal = LlmHtnPolicy(root_task=root_task)
    # Add first layer of subtasks
    s1 = Task(description="Subtask 1", status=TaskStatus.SUCCESS, parent=root_task)
    s2 = Task(description="Subtask 2", status=TaskStatus.ABANDONED, parent=root_task)
    s3 = Task(
        description="Subtask 3 (perhaps an alternative to Subtask 2, which was abandoned)",
        status=TaskStatus.IN_PROGRESS,
        parent=root_task,
    )
    s4 = Task(description="Subtask 4", status=TaskStatus.FUTURE, parent=root_task)
    s5 = Task(description="Subtask 5", status=TaskStatus.FUTURE, parent=root_task)
    s6 = Task(description="Subtask 6", status=TaskStatus.FUTURE, parent=root_task)
    s7 = Task(description="Subtask 7", status=TaskStatus.FUTURE, parent=root_task)
    root_task.subtasks.extend([s1, s2, s3, s4, s5, s6, s7])
    # Add second layer of subtasks
    s1_1 = Task(description="Subtask 1.1", status=TaskStatus.SUCCESS, parent=s1)
    s1_2 = Task(description="Subtask 1.2", status=TaskStatus.FAILURE, parent=s1)
    s1_3 = Task(description="Subtask 1.3", status=TaskStatus.SUCCESS, parent=s1)
    s1.subtasks.extend([s1_1, s1_2, s1_3])
    s2_1 = Task(description="Subtask 2.1", status=TaskStatus.FAILURE, parent=s2)
    s2_2 = Task(description="Subtask 2.2", status=TaskStatus.FAILURE, parent=s2)
    s2_3 = Task(description="Subtask 2.3", status=TaskStatus.ABANDONED, parent=s2)
    s2.subtasks.extend([s2_1, s2_2, s2_3])
    s3_1 = Task(description="Subtask 3.1", status=TaskStatus.SUCCESS, parent=s3)
    s3_2 = Task(description="Subtask 3.2", status=TaskStatus.IN_PROGRESS, parent=s3)
    s3_3 = Task(description="Subtask 3.3", status=TaskStatus.FUTURE, parent=s3)
    s3_4 = Task(description="Subtask 3.4", status=TaskStatus.FUTURE, parent=s3)
    s3_5 = Task(description="Subtask 3.5", status=TaskStatus.FUTURE, parent=s3)
    s3.subtasks.extend([s3_1, s3_2, s3_3, s3_4])
    # Add third layer of subtasks
    s1_1_1 = Task(description="Subtask 1.1.1", status=TaskStatus.PARTIAL, parent=s1_1)
    s1_1_2 = Task(description="Subtask 1.1.2", status=TaskStatus.SUCCESS, parent=s1_1)
    s1_1_3 = Task(description="Subtask 1.1.3", status=TaskStatus.SUCCESS, parent=s1_1)
    s1_1.subtasks.extend([s1_1_1, s1_1_2, s1_1_3])
    s2_2_1 = Task(description="Subtask 2.2.1", status=TaskStatus.PARTIAL, parent=s2_2)
    s2_2_2 = Task(description="Subtask 2.2.2", status=TaskStatus.FAILURE, parent=s2_2)
    s2_2.subtasks.extend([s2_2_1, s2_2_2])
    s3_2_1 = Task(description="Subtask 3.2.1", status=TaskStatus.SUCCESS, parent=s3_2)
    s3_2_2 = Task(description="Subtask 3.2.2", status=TaskStatus.SUCCESS, parent=s3_2)
    s3_2_3 = Task(
        description="Subtask 3.2.3 (this is the current task)",
        status=TaskStatus.IN_PROGRESS,
        parent=s3_2,
    )
    s3_2_4 = Task(description="Subtask 3.2.4", status=TaskStatus.FUTURE, parent=s3_2)
    s3_2_5 = Task(description="Subtask 3.2.5", status=TaskStatus.FUTURE, parent=s3_2)
    s3_2_6 = Task(description="Subtask 3.2.6", status=TaskStatus.FUTURE, parent=s3_2)
    s3_2.subtasks.extend([s3_2_1, s3_2_2, s3_2_3, s3_2_4, s3_2_5, s3_2_6])
    # Add fourth layer of subtasks
    s3_2_2_1 = Task(
        description="Subtask 3.2.2.1", status=TaskStatus.SUCCESS, parent=s3_2_2
    )
    s3_2_2_2 = Task(
        description="Subtask 3.2.2.2", status=TaskStatus.SUCCESS, parent=s3_2_2
    )
    s3_2_2_3 = Task(
        description="Subtask 3.3.3.3", status=TaskStatus.SUCCESS, parent=s3_2_2
    )
    s3_2_2.subtasks.extend([s3_2_2_1, s3_2_2_2, s3_2_2_3])
    # Set current task
    htn_traversal.current_task = s3_2_3
    return htn_traversal


MOCK_HTN_POLICY_FOR_PRETTY_HTN_STRING = get_mock_htn_policy_for_htn_pretty_string()
EXPECTED_PRETTY_HTN_STRING = f"""{TaskStatus.IN_PROGRESS} Root Task
  ├──{TaskStatus.SUCCESS} Subtask 1
  │    ├──{TaskStatus.SUCCESS} Subtask 1.1
  │    │    ├──{TaskStatus.PARTIAL} Subtask 1.1.1
  │    │    ├──{TaskStatus.SUCCESS} Subtask 1.1.2
  │    │    └──{TaskStatus.SUCCESS} Subtask 1.1.3
  │    │   
  │    ├──{TaskStatus.FAILURE} Subtask 1.2
  │    └──{TaskStatus.SUCCESS} Subtask 1.3
  │   
  ├──{TaskStatus.ABANDONED} Subtask 2
  │    ├──{TaskStatus.FAILURE} Subtask 2.1
  │    ├──{TaskStatus.FAILURE} Subtask 2.2
  │    │    ├──{TaskStatus.PARTIAL} Subtask 2.2.1
  │    │    └──{TaskStatus.FAILURE} Subtask 2.2.2
  │    │   
  │    └──{TaskStatus.ABANDONED} Subtask 2.3
  │   
  ├──{TaskStatus.IN_PROGRESS} Subtask 3 (perhaps an alternative to Subtask 2, which was abandoned)
  │    ├──{TaskStatus.SUCCESS} Subtask 3.1
  │    ├──{TaskStatus.IN_PROGRESS} Subtask 3.2
  │    │    ├──{TaskStatus.SUCCESS} Subtask 3.2.1
  │    │    ├──{TaskStatus.SUCCESS} Subtask 3.2.2
  │    │    │    ├──{TaskStatus.SUCCESS} Subtask 3.2.2.1
  │    │    │    ├──{TaskStatus.SUCCESS} Subtask 3.2.2.2
  │    │    │    └──{TaskStatus.SUCCESS} Subtask 3.3.3.3
  │    │    │   
  │    │    ├──[📍] Subtask 3.2.3 (this is the current task)
  │    │    ├──{TaskStatus.FUTURE} Subtask 3.2.4
  │    │    ├──{TaskStatus.FUTURE} Subtask 3.2.5
  │    │    └──{TaskStatus.FUTURE} Subtask 3.2.6
  │    │   
  │    ├──{TaskStatus.FUTURE} Subtask 3.3
  │    └──{TaskStatus.FUTURE} Subtask 3.4
  │   
  ├──{TaskStatus.FUTURE} Subtask 4
  ├──{TaskStatus.FUTURE} Subtask 5
  ├──{TaskStatus.FUTURE} Subtask 6
  └──{TaskStatus.FUTURE} Subtask 7"""


def test_get_pretty_htn_string():
    assert (
        get_pretty_htn_string(MOCK_HTN_POLICY_FOR_PRETTY_HTN_STRING)
        == EXPECTED_PRETTY_HTN_STRING
    )
