class AgentDescriptions:
    BACKTRACKER = """Decides whether to backtrack to the parent task node in the plan traversal.

There are 3 high level reasons why the "current task" node should _not_ be pursued going forward:
- It can be considered done (successfully completed)
- It is no longer worth pursuing
- It task was foolishly suggested/planned in the first place
"""
    PLANNER = "Creates/revises/approves future planned subtask nodes"
    OBSERVER = r'Reflecting over the environment state after a primitive action subtask node is attempted, suggests: (1) the appropriate "status" update and (2) a short "retrospective" summary of the salient information from the attempt (w.r.t. the overall plan)'
