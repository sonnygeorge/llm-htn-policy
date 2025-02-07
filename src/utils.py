"""Misc. helper functions that don't fit elsewhere."""

from enum import StrEnum
from typing import Optional

from abstract import DomainInterface


def ascertain_operational_domain_starting_up_if_necessary(
    domain: str,
) -> DomainInterface:
    pass  # TODO: Implement this function


# TODO: Move to policy dir
def get_pretty_htn_string(htn) -> str:  # FIXME: Old/defunct
    """Pretty prints a snapshot of a traversal of hierarchical task network (HTN) of the
    input policy."""

    class DefunctTaskStatus(StrEnum):
        SUCCESS = "[✅]"  # Executed successfully
        FAILURE = "[❌]"  # Failed
        PARTIAL = (
            "[🤷]"  # Outcome wasn't a "black & white" success/fail (partial success)
        )
        ABANDONED = "[💀]"  # Dropped in favor of a different approach
        IN_PROGRESS = "[⏳]"  # Currently being decomposed/executed
        FUTURE = "[💭]"  # Postulated as a future task

    row_fmt_str = "{0}{1}{2} {3}\n"
    root_status = "[📍]" if htn.root_task == htn.current_task else htn.root_task.status
    output = row_fmt_str.format("", "", root_status, htn.root_task.description)

    def _recursively_add_subtasks_to_output(
        task, prev_indent: str = "", prev_corner: Optional[str] = None
    ):
        n_subtasks = len(task.subtasks)
        for i, subtask in enumerate(task.subtasks):
            nonlocal output
            # Indent
            if prev_corner is None:
                indent = ""
            elif prev_corner == "  └──":
                indent = prev_indent + "    "
            else:  #  prev_corner == " ├──"
                indent = prev_indent + "  │  "
            # Corner
            corner = "  ├──" if i < n_subtasks - 1 else "  └──"
            # Status
            status = "[📍]" if subtask == htn.current_task else subtask.status
            output += row_fmt_str.format(indent, corner, status, subtask.description)
            if corner == "  └──" and len(subtask.subtasks) == 0:
                output += row_fmt_str.format(indent, "", "", "")
            _recursively_add_subtasks_to_output(subtask, indent, corner)

    _recursively_add_subtasks_to_output(htn.root_task)
    return output.strip()
