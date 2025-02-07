# Project Name (TBD)

Currently using `./main.py` for the code/functions that I am incrementally developing.

## Todo

ASAP:

- ❗ Use OPENAI playground to develop a (v1?) prompt for the "Backtrack Gate" (rename to "Backtracker"?) that also does the job of the "Backtrack Summarizer"
- ❗ Remove emojis from "naming legend"

Soon:

- End-to-end pipeline w/ current design pattern using 'arbitrary' domain and FORMALLY CODE REVIEW MYSELF

Soonish:

- Add algorithm diagram to readme(s) somewhere
- Determine what the prompt context windows are for "small" open-source LLMs and develop prompts with this in mind (and potentially re-introduce the "memory compressor" back into the game plan...)
- What is the best way to represent a hierarchical plan traversal in natural language for LLM comprehension? Ryan Greenblatt style (use all the possible ways)?
- Casually see if there are any "gem" freelancers on Upwork

Later:

- Come up with a handful of "extremely long-horizon" Minecraft (and robot/other?) tasks (where success is easily programatically verifiable?)
- Keep an eye out for resources in other papers that might give me head start(s) (e.g. an already fined-tuned LLM for Minecraft knowledge, repurposable MineDojo Docker image/container, etc.)
- Determine (Ask Chris) how to run/train LLMs remotely (probably, in my case, an EC2 that I turn off and on whenever I need it?)

Indefinitely postponed:

- The LLM call that is responsible for distilling/compressing the "memory" when it exceeds a threshold

## Task Ideas

- Build a house where inside, there is a flower pot holding each of the following plants: cactus, rose, dandelion, and oak sapling.
- Find 3 nearby villages and count how many farms each village has.

## Rhetoric Ideas

- (Precedent "long-horizon task" papers are just gather one item or a robot doing something for up to a minute or two...) **This paper considers the (any-horizon) (any-depth hierarchical) composition of many such long-horizon tasks.**