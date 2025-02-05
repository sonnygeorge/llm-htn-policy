# LlmHtnPolicy

Currently using `./main.py` for the code/functions that I am incrementally developing.

## Todo

- Research MC-TextWorld from CraftJarvis
- Determine what the prompt context windows are for "small" open-source LLMs and develop prompts with this in mind (and potentially re-introduce the "memory compressor" back into the game plan...)
- What is the best way to represent a hierarchical plan traversal in natural language for LLM comprehension? Ryan Greenblatt style (use all the possible ways)?
- Casually see if there are any "gem" freelancers on Upwork
- Come up with a handful of "extremely long-horizon" Minecraft (and robot/other?) tasks (where success is easily programatically verifiable?)
- Keep an eye out for resources in other papers that might give me head start(s) (e.g. an already fined-tuned LLM for Minecraft knowledge, repurposable MineDojo Docker image/container, etc.)
- Determine (Ask Chris) how to run/train LLMs remotely (probably, in my case, an EC2 that I turn off and on whenever I need it?)

Indefinitely postponed:

- The LLM call that is responsible for distilling/compressing the "memory" when it exceeds a threshold

## Task Ideas

- Build a house where inside, there is a flower pot holding each of the following plants: cactus, rose, dandelion, and oak sapling.
- Find 3 nearby villages and count how many farms each village has.

## Domains

### TextWorld:

Pros:
- Ease of use
- Out-of-the-box, it will be good for testing "exiting task node upon completion"
- Will be good for developing a prompt that ensures/fine-tuning to enforce initial high-level decompositions that follow tasks that are input already with a natural breakdown.
- Will be good at then ensuring that when its appropriate, the decompositions to primitive actions are indeed in the DSL format of the primitive action space (or otherwise easily mappable w/ semantic search or a cheap LLM)

Cons:
- Will not be good for going past recursion/decomposition layer 3, since high level plans are spoonfed, and this breakdown will basically map 1-to-1 with primitive actions
- Potentially good for "practicing" exiting task nodes that are foolishly suggested

### MC-TextWorld from CraftJarvis:

TBD

## Rhetoric

- (Precedent "long-horizon task" papers are just gather one item or a robot doing something for up to a minute or two...) **This paper considers the (any-horizon) (any-depth hierarchical) composition of many such long-horizon tasks.**