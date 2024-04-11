#!/usr/bin/python3
"""
Gather data from an API
"""

import requests

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com"
    todos = requests.get(f"{url}/todos").json()
