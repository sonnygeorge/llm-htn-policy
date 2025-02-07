import fire
import importlib.util

from abstract import Task, Policy
from agent import get_agents_for_policy
from configs import Strings
from utils import ascertain_operational_domain_starting_up_if_necessary


# TODO: Run all tasks in a specified directory instead of one at a time


def run(policy: str = "🧠🔢", domain: str = "minecraft", task: str = "acquire_iron"):
    domain_interface = ascertain_operational_domain_starting_up_if_necessary(domain)
    # Get task
    task_module_path = Strings.TASK_MODULE_PATH.format(domain=domain, task=task)
    task_module = importlib.import_module(task_module_path)
    TaskClass = getattr(task_module, Strings.get_task_class_name(task))
    task: Task = TaskClass(domain_interface=domain_interface)
    # Get agents
    agents = get_agents_for_policy(policy, domain)
    # Get policy
    policy_module_path = Strings.POLICY_MODULE_PATH.format(policy=policy)
    policy_module = importlib.import_module(policy_module_path)
    PolicyClass = getattr(policy_module, Strings.UNIVERSAL_POLICY_CLASS_NAME)
    policy: Policy = PolicyClass(agents=agents, task=task.description)
    # Run the policy on the task
    observation = task.reset()
    for _ in range(task.max_steps):
        action = policy(observation, task)
        if action is None:  # Policy believes the task is complete
            break
        observation, should_terminate = task.step(action)
        if should_terminate:
            break
    task.finalize()
    # TODO: Whatever else to log artifacts, etc.


if __name__ == "__main__":
    fire.Fire(run)  # Expose the `run` function to the command line
