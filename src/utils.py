from src.llm_htn_policy import LlmHtnPolicy, Task

from typing import Optional


def get_pretty_htn_string(htn: LlmHtnPolicy) -> str:
    """Pretty prints a snapshot of a traversal of hierarchical task network (HTN) of the
    input policy."""
    row_fmt_str = "{0}{1}{2} {3}\n"
    root_status = "[📍]" if htn.root_task == htn.current_task else htn.root_task.status
    output = row_fmt_str.format("", "", root_status, htn.root_task.description)

    def _recursively_add_subtasks_to_output(
        task: Task, prev_indent: str = "", prev_corner: Optional[str] = None
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
