# LlmHtnPolicy

Currently using `./main.py` to run the code/functions I am incrementally developing.

## TODO

- [ ] - `HtnPolicy.__call__`: Determine a "standard" interface for inputting _any_ observation space and outputting _any_ action space
- [ ] - The "Distiller"/"Pruner"...
  - Crucially one that, for the sake of useful natural language prompts, distills the salient information from the HTN traversal into a representation that is apt for LLM comprehension.
    - [ ] ❗ What is the best way to represent an HTN traversal for LLM comprehension?
  - ...and perhaps (for memory compression in truly long-horizon autonomy), a step that permanently prunes away past task branches—leaving a "pruned" flag in their place and summarizing the salient details of the higher-level task attempt (whose subtask branches where pruned)