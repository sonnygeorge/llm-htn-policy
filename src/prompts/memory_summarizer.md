NOTES:

- GOAL: take this HTN (json?), which is currently ([size measure] - word count?) and summarize it {reduction amount}% to ([size measure] - word count?) such that as much useful/salient information is retained/remember w.r.t to solving the task.
  - Do this iteratively:
    - 1. Checking total memory size, if > {limit}
    - 2. Pick n candidates to be condensed (forgotten or summarized)
    - 3. Reason over them, and pick the best candidate
    - 4. Summarize the candidate, loop back to 1

