We want to, for example, start with an in-progress hierarchical plan like this (where execution traversal is just finishing with node "1.2.1.1"):

```json
{
    {
        "node": "1",
        "description": "Fill this cauldron with water",
        "status": "In progress",
        "retrospective": null,
        "breakdown": [
            {
                "node": "1.1",
                "description": "Identify most probable cauldron to which user could be referring",
                "status": "Execution attempted (success)",
                "retrospective": "Only one nearby cauldron at coordinates (201, 64, -30)",
                "breakdown": null,
            },
            {
                "node": "1.2",
                "description": "Acquire bucket",
                "status": "In progress",
                "retrospective": null,
                "breakdown": [
                    {
                        "node": "1.2.1",
                        "description": "Acquire 3 iron",
                        "status": "In progress",
                        "retrospective": null,
                        "breakdown": [
                            {
                                "node": "1.2.1.1",
                                "description": "Check nearby blacksmith chest for iron",
                                "status": "Execution attempted (success)",
                                "retrospective": "Upon inspection, the blacksmith chest at coordinates (243, 67, -71) did not contain any iron. Instead, its contents were: 1 iron axe, 1 apple, 1 water bucket, 3 wheat, and 1 pair of diamond boots.",
                            }
                        ]
                    },
                    {
                        "node": "1.2.2",
                        "description": "Craft bucket with 3 iron",
                        "status": null,
                        "retrospective": null,
                        "breakdown": null,
                    }
                ]
            },
            {
                "node": "1.3",
                "description": "Fill bucket with water",
                "status": "Proposed future plan",
                "retrospective": null,
                "breakdown": null,
            },
            {
                "node": "1.4",
                "description": "Place water in cauldron",
                "status": "Proposed future plan",
                "retrospective": null,
                "breakdown": null,
            }
        ]
    }
}
```

...and use LLMs to: 

1. reason over the state of the plan traversal
2. realize that a current direction of approach has become moot (or otherwise worth abandoning)
3. backtrack the traversal back to the node ("1") that is the parent of the now-moot subtask branch ("1.2")
4. update the status of the now-moot branching node ("1.2") to "aborted"
5. prune all children of the now-moot subtask ("1.2")
6. give and update the node with retrospective reasoning for why this subtask ("1.2") was aborted
7. revise all remaining future plans given this update (e.g. removing the previous "1.3" since the bucket that will be used no longer needs to be filled with water)

...resulting in an HTN like this (where the execution traversal is now entering node "1.3"):

```json
{
    {
        "node": "1",
        "description": "Fill this cauldron with water",
        "status": "In progress",
        "retrospective": null,
        "breakdown": [
            {
                "node": "1.1",
                "description": "Identify most probable cauldron to which user could be referring",
                "status": "Execution attempted (success)",
                "retrospective": "Only one nearby cauldron at coordinates (201, 64, -30)",
                "breakdown": null,
            },
            {
                "node": "1.2",
                "description": "Acquire bucket",
                "status": "Execution attempted (aborted)",
                "retrospective": "While seeking to acquire iron to craft a bucket, we learned that the nearby blacksmith chest contained a usable water bucket, removing the need to acquire an empty bucket to be filled with water.",
                "breakdown": null,
            },
            {
                "node": "1.3",
                "description": "Place water in cauldron",
                "status": "Proposed future plan",
                "retrospective": null,
                "breakdown": null,
            }
        ]
    }
}
```
