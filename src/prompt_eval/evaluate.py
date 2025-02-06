from typing import Optional

from pydantic import BaseModel


class PromptEvalTest(BaseModel):
    """Evaluation information for a single agent call in a sequence of agent calls.

    Attributes:
        inputs (BaseModel): The input to the agent call.
        good_outputs_example (Optional[BaseModel]): An example of good outputs given the
            inputs.
        desired_outcomes (str): A description of the desired outcomes of the agent call.
    """

    inputs: BaseModel
    good_outputs_example: Optional[BaseModel]  # Optional for now, could be used for RL
    desired_outcomes: str
