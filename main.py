import fire

from typing import Optional


def annotate(
    domain: str = "minecraft",
    tasks_dir: str = None,  # FIXME
    policy: str = "adhp",
    prompt_version: str = 1,
    domain_prompt_snippet_version: str = 1,
    models: dict = {
        "adhp": {
            "backtracker": "gpt-3.5-turbo",
            "planner": "gpt-4o-mini",
            "observer": "gpt-3.5-turbo",
        }
    },
    headless: bool = False,
    open_planviz: bool = True,
    log_level: str = "info",
    log_dir: str = None,
    output_file: Optional[str] = None,
    **kwargs,
):
    raise NotImplementedError("'annotate' not yet implemented")


def train_supervised(
    domain: str = "minecraft",
    train_data: str = None,  # FIXME: Later
    eval_data: str = None,  # FIXME: Later
    policy: str = "adhp",
    models: dict = {
        "adhp": {
            "backtracker": "gpt-3.5-turbo",
            "planner": "gpt-4o-mini",
            "observer": "gpt-3.5-turbo",
        }
    },
    log_level: str = "info",
    log_dir: str = None,
    output_file: Optional[str] = None,
    **kwargs,
):
    raise NotImplementedError("'train_supervised' not yet implemented")


def train_rl(
    domain: str = "minecraft",
    train_tasks_dir: str = None,  # FIXME: Later
    eval_tasks_dir: str = None,  # FIXME: Later
    policy: str = "adhp",
    prompt_version: str = 1,
    domain_prompt_snippet_version: str = 1,
    models: dict = {
        "adhp": {
            "backtracker": "gpt-3.5-turbo",
            "planner": "gpt-4o-mini",
            "observer": "gpt-3.5-turbo",
        }
    },
    headless: bool = True,
    open_planviz: bool = False,
    log_level: str = "info",
    log_dir: str = None,
    output_file: Optional[str] = None,
    **kwargs,
):
    raise NotImplementedError("'train_rl' not yet implemented")


def evaluate_policy(
    domain: str = "minecraft",
    test_tasks_dir: str = None,  # FIXME: Later
    policy: str = "adhp",
    prompt_version: str = 1,
    domain_prompt_snippet_version: str = 1,
    models: dict = {
        "adhp": {
            "backtracker": "gpt-3.5-turbo",
            "planner": "gpt-4o-mini",
            "observer": "gpt-3.5-turbo",
        }
    },
    headless: bool = True,
    open_planviz: bool = False,
    log_level: str = "info",
    log_dir: str = None,
    output_file: Optional[str] = None,
    **kwargs,
):
    raise NotImplementedError("'evaluate_policy' not yet implemented")


def run_prompt_tests(
    domain: str = "minecraft",
    policy: str = "adhp",
    prompt_version: str = 1,
    domain_prompt_snippet_version: str = 1,
    models: dict = {
        "adhp": {
            "backtracker": "gpt-3.5-turbo",
            "planner": "gpt-4o-mini",
            "observer": "gpt-3.5-turbo",
        }
    },
    log_level: str = "info",
    log_dir: str = None,
    output_file: Optional[str] = None,
):
    raise NotImplementedError("'run_prompt_tests' not yet implemented")


def run_generic(
    domain: str = "minecraft",
    tasks_dir: str = None,  # FIXME
    policy: str = "adhp",
    prompt_version: str = 1,
    domain_prompt_snippet_version: str = 1,
    models: dict = {
        "adhp": {
            "backtracker": "gpt-3.5-turbo",
            "planner": "gpt-4o-mini",
            "observer": "gpt-3.5-turbo",
        }
    },
    headless: bool = False,
    open_planviz: bool = True,
    log_level: str = "info",
    log_dir: str = None,
    **kwargs,
):
    print(kwargs)


def main(program="run_generic", **kwargs):
    if "config" in kwargs:
        # TODO: kwargs = read in config file and overwrite with kwargs
        pass

    if program == "annotate":
        annotate(**kwargs)
    elif program == "train_supervised":
        train_supervised(**kwargs)
    elif program == "train_rl":
        train_rl(**kwargs)
    elif program == "evaluate_policy":
        evaluate_policy(**kwargs)
    elif program == "run_prompt_tests":
        run_prompt_tests(**kwargs)
    elif program == "run_generic":
        run_generic(**kwargs)


if __name__ == "__main__":
    fire.Fire(main)
