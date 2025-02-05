# "Headless" Simulator Idea

Idea:

Build a simplified MC "headless" simulator and use it to...

1. Acquire both/either:
    1. Useful `test_scenario` cases (by saving "good" artifacts and manually tweaking "bad" artifacts based on what it should have done)
    2. "good"/"bad" human judgment of llm/agent outputs for for RLHF fine-tuning

2. Be able to programatically check the completion of tasks (especially "extremely long-horizon" ones) and use these outputs for:
    1. The empirical results of a paper
    2. (Sparse-reward) RL fine-tuning

## Considerations

### Action Primitives

If I were to make this "headless" simulator, I would need to define a set of action primitives:
- That are indeed comprehensive for solving the many eventually desired tasks in the actual game
- That are indeed reliably doable with Mineflayer JS 
- For which the simulator then generates (more or less) representative (statistically accurate) outcomes (env representations).

### Alternatives

[MC-TextWorld](https://github.com/CraftJarvis/MC-TextWorld) from the [CraftJarvis](https://craftjarvis.github.io/) team.

## Order of Operations

1. Prompt optimization/prompt engineering
2. LLM fine-tuning
