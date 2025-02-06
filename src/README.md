# `/src` Directory

The directory with the source code for the project.

## Symbolic Naming Legend

### Policies

| Emoji | Symbolizes |
| --- | --- |
| 🧠0️⃣ | ReAct policy (no planning) |
| 🧠1️⃣ | Closed-loop planning in sequences of primitive actions (1-layer planning) |
| 🧠2️⃣ | Closed-loop planning with a "high-level" plan & primitive action breakdowns (2-layer planning) |
| 🧠🔢 | Closed-loop planning w/ any-depth task decomposition (any-layer planning) |

### Agents

#### Agents of the 🧠🔢 Policy

| Emoji | Symbolizes |
| --- | --- |
| ⏪🚪 | "Backtrack Gate" agent |
| ⏪📝 | "Backtrack Summarizer" agent |
| 📅🔄 | "(Re-) Planner" agent |
| 🏃‍♂️📝 | "Attempt Summarizer" agent |