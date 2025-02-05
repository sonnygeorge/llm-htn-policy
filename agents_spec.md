# Agents Spec

## 1. 🔵 Exit (Recursion) Classifier

### System Prompt

Instructions on how to decide if task should be exitted.

Inputs:
- Output format for JSON

### User Prompt

Inputs:
- The entire hierarchical plan traversal
- Indication of what the "current task" we are deliberating exitting is
- Current environment state
- Notepad(?)

Outputs:
- The classification decision (true=exit, false=don't exit)
- The "reasoning" for the classification decision\*

### Test Cases

**Should abort because utility of distant parent rendered moot after attempt**
1. ?

**Should abort because utility of immediate parent rendered moot after attempt**
1. ?

**Should abort because current task utility rendered moot after attempt**
1. ?

**Should abort because utility rendered moot (after exiting from completed child)**
1. `found_bucket_removes_need_for_bucket_crafting/1_🔵`

**Should abort because utility rendered moot (after exiting from aborted child)**
2. `found_bucket_removes_need_for_bucket_crafting/3_🔵`

**Foolishly suggested in the first place**
1. ?

**Current task can be considered complete**
1. ?

**Current task cannot be considered complete (but should not be aborted—i.e. should continue to be pursued)**
1. ?

## 2. 🔷 Exit (Recursion) Summarizer

### System Prompt

Instructions on how to summarize the exit of a task node.

Inputs:
- Output format for JSON

### User Prompt

Inputs:
- The "reasoning" for the (exit) classification decision\*
- ?

Outputs:
- `retrospective` for the "current task" that is being exited
- `status` for the "current task" that is being exited

### Test Cases

**Exit status should be "Aborted"**
1. `found_bucket_removes_need_for_bucket_crafting/2_🔷`

...

## 3. (Re-) Planner

### System Prompt

Instructions on how to (re-) plan future subtasks.

Inputs:
- Output format for JSON

### User Prompt

Inputs:
- The entire hierarchical plan traversal
- Indication of the "current task" and "subtasks" for we are (re-) planning future tasks
- Current environment state
- Notepad(?)

Outputs:
- The sequence of "(re-) planned" future "subtasks"

### Test Cases

**Revising future planned subtasks**
1. `found_bucket_removes_need_for_bucket_crafting/5_🔴`

...

## 4. Attempt Summarizer

### System Prompt

Instructions on summarize the outcomes of an action attempt.

Inputs:
- Output format for JSON

### User Prompt

Inputs:
- The entire hierarchical plan traversal
- Indication of what the "subtask" for wich we are evaluating and summarizing the successful or failed completion is
- (NEW) Current environment state
- Notepad(?)

Outputs:
- `retrospective` for the "subtask" that is being evaluated
- `status` for the "subtask" that is being evaluated

### Test Cases

...

## 📝 Misc. Notes

- Memory-compressing agent is deferred for future work/consideration
- Useful design pattern: have a "state" object that is an input to the agents


