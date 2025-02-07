from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

from typing import Dict


load_dotenv()


class Strings:
    # Directories
    SYS_PROMPTS_DIR_PATH = "policies/{policy}/prompts/system/{agent}"
    USER_PROMPTS_DIR_PATH = "policies/{policy}/prompts/user/{agent}"
    DOMAIN_SYS_PROMPT_ADDITIONS_DIR_PATH = (
        "domains/{domain}/system_prompt_additions/{policy}/{agent}"
    )

    # Dynamically imported modules
    TASK_MODULE_PATH = "domains/{domain}/tasks/{task}.py"
    POLICY_MODULE_PATH = "policies/{policy}/policy.py"
    AGENT_OUTPUT_MODEL_MODULE_PATH = "policies/{policy}/agent_io.py"

    # Class names
    UNIVERSAL_POLICY_CLASS_NAME = "Policy"

    @staticmethod
    def get_task_class_name(lower_snake_case_task: str) -> str:
        return "".join(w.capitalize() for w in lower_snake_case_task.split("_"))

    @staticmethod
    def get_agent_output_model_class_name(lower_snake_case_agent: str) -> str:
        upper_camel_case_agent = "".join(
            w.capitalize() for w in lower_snake_case_agent.split("_")
        )
        return f"{upper_camel_case_agent}Output"


class PromptKws:
    DOMAIN_SPECIFIC_SYS_PROMPT_ADDITION = "domain_specific_addition"


DOMAINS = [
    "arbitrary",
    "alfworld",
    "minecraft",
]

POLICIES_AND_AGENTS: Dict[str, dict] = {
    "🧠0️⃣": {},
    "🧠1️⃣": {},
    "🧠2️⃣": {},
    "🧠🔢": {
        "⏪🚪": {
            "name": "Backtrack Gate",
            "short_description": "Decides whether to backtrack to the parent task node in the plan traversal",
            "chat_model": ChatOpenAI(model="gpt-4o-mini", temperature=0.5),
        },
        "⏪📝": {
            "name": "Backtrack Summarizer",
            "short_description": "",  # TODO: Fill in
            "chat_model": ChatOpenAI(model="gpt-3.5-turbo", temperature=0.5),
            # Do I even need to do this if the backtrack gate is already giving succint, summative reasoning?
            # If not, I would need the backtrack gate to really precisely complete the reasoning flowchart and indicate the resulting status...
            # TODO: In a playground, probe the ability of typical small LLMs abilities to complete the reasoning flowchart and output the right status classification
        },
        "📅🔄": {
            "name": "(Re-) Planner",
            "short_description": "Creates/revises/approves future planned subtask nodes",
            "chat_model": ChatOpenAI(model="gpt-4o-mini", temperature=0.5),
        },
        "🏃‍♂️📝": {
            "name": "Attempt Summarizer",
            "short_description": r'Reflecting over the environment state after a primitive action subtask node is attempted, suggests: (1) the appropriate "status" update and (2) a short "retrospective" summary of the salient information from the attempt (w.r.t. the overall plan)',
            "chat_model": ChatOpenAI(model="gpt-3.5-turbo", temperature=0.5),
        },
    },
}
