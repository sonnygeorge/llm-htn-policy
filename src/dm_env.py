"""Code for more simple simulated environment (e.g., en lieu of a Minecraft or other
environment) for testing/iterating on the HTN-traversing policy. Specifically, code
for an environment in which a human continuously decides what happens in an imagined
environment using natural language console inputs (e.g., like a D&D dungeon master, who on
the fly, conceives and articulates what happens next).
"""

from src.llm_htn_policy import Task, TaskStatus, LlmHtnPolicy


def run_dungeon_master_htn_policy_simulation():
    """Simulate usage of using the `HtnTraversalPolicy` with a human "dungeon master",
    where the observation space is natural language that the user conceives on the fly and
    inputs into the console.
    """
    # TODO: Actually implement this function
    sys_prompt = input("What is short system prompt to describe who the AI is?")
    task_description = input("What task should they perform/do?")

    root_task = Task(description="Root Task", status=TaskStatus.IN_PROGRESS)
    htn = LlmHtnPolicy(root_task=root_task)

    while True:
        env_state = input("Given the action, what is the result?")
        next_action = htn(env_state)
