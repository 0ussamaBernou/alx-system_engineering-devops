#!/usr/bin/python3
"""
Gather data from an API
"""

import requests
from sys import argv
import json

if __name__ == "__main__":
    id = argv[1]
    url = "https://jsonplaceholder.typicode.com"
    user = requests.get(f"{url}/users/{id}").json()
    todos = requests.get(f"{url}/todos?userId={id}").json()

    completed = [task.get("title") for task in todos if task.get("completed")]

    tasks = {
        id: [
            {
                "task": task.get("title"),
                "completed": task.get("completed"),
                "username": user.get("username"),
            }
            for task in todos
        ]
    }
    with open(f"{id}.json", "w") as file:
        json.dump(tasks, file)
