# Agents Spec

## 1. 🔵 Exit (Recursion) Classifier

### System Prompt

- Domain-agnostic instructions on how to decide if a task should be exitted (a function w/in a multi-agent system)
- Domain-agnostic few-shot examples

(Dynamic) Inputs:
- Domain-specific stuff:
    - General introductory info (e.g., 'The multi-agent system controls a Vanilla Minecraft player where env state looks like ____. Your job is to decide whether to exit the current task node...')
    - Few-shot "good" examples
    - Agent-specific tips (e.g., Pay attention to ____. Don't ____.)
- Output format for JSON

### User Prompt

(Dynamic) Inputs:
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

- Domain-agnostic instructions on how to summarize the exit of a task node (a function w/in a multi-agent system)
- Domain-agnostic few-shot examples

(Dynamic) Inputs:
- Domain-specific stuff:
    - General introductory info (e.g., 'The multi-agent system controls a Vanilla Minecraft player where env state looks like ____. Your job is to distill why a task node was deemed to be exited...')
    - Few-shot "good" examples
    - Agent-specific tips (e.g., Pay attention to ____. Don't ____.)
- Output format for JSON

### User Prompt

(Dynamic) Inputs:
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

- Domain-agnostic instructions on how to (re-) plan future subtasks (a function w/in a multi-agent system)
- Domain-agnostic few-shot examples

(Dynamic) Inputs:
- Domain-specific stuff:
    - General introductory info (e.g., 'The multi-agent system controls a Vanilla Minecraft player where env state looks like ____. You must plan sequential actions that eventually decompose to these action primitives...')
    - The set of available action primitives
    - Few-shot "good" examples
    - Agent-specific tips (e.g., Pay attention to ____. Don't ____.)
- Output format for JSON

### User Prompt

(Dynamic) Inputs:
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

- Domain-agnostic instructions on summarize the outcomes of an action attempt (a function w/in a multi-agent system)
- Domain-agnostic few-shot examples

(Dynamic) Inputs:
- Domain-specific stuff:
    - General introductory info (e.g., 'The multi-agent system controls a Vanilla Minecraft player where env state looks like ____. Your job is to summarize the attempt one of the following action primitives...')
    - The set of available action primitives
    - Few-shot "good" examples
    - Agent-specific tips (e.g., Pay attention to ____. Don't ____.)
- Output format for JSON

### User Prompt

(Dynamic) Inputs:
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
