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
