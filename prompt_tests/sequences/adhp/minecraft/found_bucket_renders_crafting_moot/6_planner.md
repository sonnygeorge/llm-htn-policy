Assert when "current task" = "1" and plan traversal ≈:

```json
{
    "task": "1",
    "description": "Fill this cauldron with water",
    "status": "In progress",
    "retrospective": null,
    "subtasks": [
        {
            "task": "1.1",
            "description": "Identify most probable cauldron to which user could be referring",
            "status": "Execution attempted (success)",
            "retrospective": "Only one nearby cauldron at coordinates (201, 64, -30)",
            "subtasks": null,
        },
        {
            "task": "1.2",
            "description": "Acquire bucket",
            "status": "Dropped",
            "retrospective": "The blacksmith chest at coordinates (243, 67, -71) already contains a water bucket.",
            "subtasks": null
        },
        {
            "task": "1.3",
            "description": "Fill bucket with water",
            "status": "Planned",
            "retrospective": null,
            "subtasks": null,
        },
        {
            "task": "1.4",
            "description": "Place water in cauldron",
            "status": "Planned",
            "retrospective": null,
            "breakdown": null,
        }
    ]
}
```

...the updated plan:
1. Involves using the water bucket found in the blacksmith chest to fill the cauldron
3. Omits the notion of needing to fill the bucket up with water
