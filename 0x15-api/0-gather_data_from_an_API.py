#!/usr/bin/python3
"""
Gather data from an API
"""

import requests
from sys import argv

if __name__ == "__main__":
    id = argv[1]
    url = "https://jsonplaceholder.typicode.com"
    user = requests.get(f"{url}/users/{id}").json()
    todos = requests.get(f"{url}/todos?userId={id}").json()

    completed = [task.get("title") for task in todos if task.get("completed")]

    print(
        f"Employee {user.get('name')} is done with "
        f"tasks({len(completed)}/{len(todos)}):"
    )

    [print(f"\t {task}") for task in completed]
