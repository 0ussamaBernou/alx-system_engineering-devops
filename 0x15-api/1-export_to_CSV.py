#!/usr/bin/python3
"""
Gather data from an API
"""

import requests
from sys import argv

if __name__ == "__main__":
    id = argv[1]
    link = "https://jsonplaceholder.typicode.com"
    user = requests.get(f"{link}/users/{id}").json()
    todos = requests.get(f"{link}/todos?userId={id}").json()

    completed = [task.get("title") for task in todos if task.get("completed")]

    with open(f"{id}.csv", "w") as f:
        for task in todos:
            f.write(
                f'"{user.get("id")}","{user.get("username")}",'
                f'"{True if task.get("title") in completed else False}",'
                f'"{task.get("title")}"\n'
            )
