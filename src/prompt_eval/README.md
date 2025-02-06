# Prompt Evaluation

🚧 **Under Construction** 🚧

This directory contains code and data for human-judged evaluation of a prompt version+model combo's performance over a variety of scenarios.

The idea is: for any "policy" (consisting of sequences of one or more "agent" calls to generate the next primitive action(s)), we manually judge (score) the generations of a prompt version+model combo, over a diversity of scenarios that, ideally, cover the range of behaviors we want the agents to exhibit.

This is important for the sake of measuring our progress as we incrementally develop prompts (and perhaps fine-tune models).

## Todo

- [ ] Convert existing tests to JSON format once input/output objects have been defined
- [ ] Implement `evaluate.py` script
- [ ] Finish enumerating desired behaviors in this README

## Coverage

(See symbolic naming legend in the `README.md` of the `/src` directory.)

### 🧠🔢

#### ⏪🚪

| Desired Behavior | Tests |
| --- | --- |
| ❌🌀—Don't backtrack when current task should be pursued further &... | |
| ‌‌ ‌‌ ‌‌- is new (has no children subtasks) | |
| ‌‌ ‌‌ ‌‌- is _not_ new (has children subtasks) &... | |
|‌‌ ‌‌ ‌‌ ‌‌ ‌‌ ‌‌ -  has no subtasks planned for the future | |
|‌ ‌‌ ‌‌ ‌‌ ‌‌ ‌‌ -  has subtasks planned for the future | `minecraft/`<br>- `found_bucket_renders_crafting_moot/5_⏪🚪` |
| 🌀✅—Backtrack when current task can be considered successfully completed after... | |
| ‌‌ ‌‌ ‌‌- _primitive-action_ subtask attempt completion | |
| ‌‌ ‌‌ ‌‌- _non-primitive-action_ subtask attempt completion |
| 🌀❌—Backtrack when current task should be considered definitively failed and<br>given up on (for now?) after... | |
| ‌‌ ‌‌ ‌‌- _primitive-action_ subtask attempt completion | |
| ‌‌ ‌‌ ‌‌- _non-primitive-action_ subtask attempt completion |
| 🌀🤷—Backtrack when current task should be considered partially successful—but<br>otherwise given up on (for now?)—after... | |
| ‌‌ ‌‌ ‌‌- _primitive-action_ subtask attempt completion | |
| ‌‌ ‌‌ ‌‌- _non-primitive-action_ subtask attempt completion |
| 🌀🦕—Backtrack b/c, after _primitive-action_ subtask attempt completion... | |
| ‌‌ ‌‌ ‌‌- distant parent rendered moot | |
| ‌‌ ‌‌ ‌‌- immediate parent rendered moot | |
| ‌‌ ‌‌ ‌‌- current task rendered moot | |
| 🌀🏙️—Backtrack b/c, after _non-primitive-action_ subtask attempt completion... | |
| ‌‌ ‌‌ ‌‌- distant parent rendered moot | |
| ‌‌ ‌‌ ‌‌- immediate parent rendered moot | `minecraft/`<br>- `found_bucket_renders_crafting_moot/1_⏪🚪` |
| ‌‌ ‌‌ ‌‌- current task rendered moot | |
| 🌀🗑️—Backtrack b/c, after _non-primitive-action_ subtask "abortion"... | |
| ‌‌ ‌‌ ‌‌- distant parent rendered moot | |
| ‌‌ ‌‌ ‌‌- immediate parent rendered moot | |
| ‌‌ ‌‌ ‌‌- current task rendered moot | `minecraft/`<br>- `found_bucket_renders_crafting_moot/3_⏪🚪` |
| 🌀🤡—Backtrack when current task was foolishly suggested &... |  |
| ‌‌ ‌‌ ‌‌- is new (has no children subtasks) |  |
| ‌‌ ‌‌ ‌‌- is _not_ new (has children subtasks) |  |



#### ⏪📝

| Desired Behavior | Tests |
| --- | --- |
| Set status to "Attempted (success)" after 🌀✅ and... | |
| ‌‌ ‌‌ ‌‌- _primitive-action_ subtask attempt completion | |
| ‌‌ ‌‌ ‌‌- _non-primitive-action_ subtask attempt completion |
| Set status to "Attempted (failure)" after 🌀❌ and... | |
| ‌‌ ‌‌ ‌‌- _primitive-action_ subtask attempt completion | |
| ‌‌ ‌‌ ‌‌- _non-primitive-action_ subtask attempt completion |
| Set status to "Attempted (partial success)" after 🌀🤷 and... | |
| ‌‌ ‌‌ ‌‌- _primitive-action_ subtask attempt completion | |
| ‌‌ ‌‌ ‌‌- _non-primitive-action_ subtask attempt completion |
| Set status to "Aborted" after 🌀🦕 and... | |
| ‌‌ ‌‌ ‌‌- distant parent rendered moot | |
| ‌‌ ‌‌ ‌‌- immediate parent rendered moot | |
| ‌‌ ‌‌ ‌‌- current task rendered moot | |
| Set status to "Aborted" after 🌀🏙️ and... | |
| ‌‌ ‌‌ ‌‌- distant parent rendered moot | |
| ‌‌ ‌‌ ‌‌- immediate parent rendered moot | `minecraft/`<br>- `found_bucket_renders_crafting_moot/2_⏪📝` |
| ‌‌ ‌‌ ‌‌- current task rendered moot | |
| Set status to "Aborted" after 🌀🗑️ and... | |
| ‌‌ ‌‌ ‌‌- distant parent rendered moot | |
| ‌‌ ‌‌ ‌‌- immediate parent rendered moot | |
| ‌‌ ‌‌ ‌‌- current task rendered moot | `minecraft/`<br>- `found_bucket_renders_crafting_moot/4_⏪📝` |
| Set status to "Aborted" after 🌀🤡 and... | |
| ‌‌ ‌‌ ‌‌- is new (has no children subtasks) |  |
| ‌‌ ‌‌ ‌‌- is _not_ new (has children subtasks) |  |

#### 📅🔄

| Desired Behavior | Tests |
| --- | --- |
| ... | |
| Revising planned subtasks is warranted after backtracking... | |
| ‌‌ ‌‌ ‌‌- status="Aborted" | `minecraft/`<br>- `found_bucket_renders_crafting_moot/6_📅🔄` |
| ‌‌ ‌‌ ‌‌- status="Attempted (success)" | |
| ‌‌ ‌‌ ‌‌- status="Attempted (failure)" | |
| ‌‌ ‌‌ ‌‌- status="Attempted (partial success)" | |
| ... | |


#### 🏃‍♂️📝

| Desired Behavior | Tests |
| --- | --- |
| Set status to "Attempted (failure)" when an error is thrown b/c... | |
| ‌‌ ‌‌ ‌‌- primitive action function not in namespace | |
| ‌‌ ‌‌ ‌‌- function arguments invalid | |
| ... | |