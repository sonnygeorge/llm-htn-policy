# LlmHtnPolicy

Currently using `./main.py` for the code/functions that I am incrementally developing.

## Todo

- [ ] `LlmHtnPolicy.__call__`: Determine a "standard" interface for inputting _any_ observation space and outputting _any_ action space
- [ ] The "Distiller"/"Pruner"...
  - Crucially one that, for the sake of useful natural language prompts, distills the salient information from the HTN traversal into a representation that is apt for LLM comprehension.
    - [ ] ❗ What is the best way to represent an HTN traversal for LLM comprehension?
  - ...and perhaps (for memory compression in truly long-horizon autonomy), a step that permanently prunes away past task branches—leaving a "pruned" flag in their place and summarizing the salient details of the higher-level task attempt (whose subtask branches where pruned)

  ## Task Ideas

  - Build a house where inside, there is a flower pot holding each of the following plants: cactus, rose, dandelion, and oak sapling.
  - Find 3 nearby villages and count how many farms each village has.

  ## Rhetoric

  - (Precedent "long-horizon task" papers are just gather one item or a robot doing something for up to a minute or two...) **This paper considers the (any-horizon) (any-depth hierarchical) composition of many such long-horizon tasks.**