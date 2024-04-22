#!/usr/bin/python3
""""
Python script to export data in the JSON format.
Records all tasks that are owned by this employee
Format must be: { "USER_ID": [{"task": "TASK_TITLE", "completed":
    TASK_COMPLETED_STATUS, "username": "USERNAME"}, {"task": "TASK_TITLE",
    "completed": TASK_COMPLETED_STATUS, "username": "USERNAME"}, ... ]}
File name must be: USER_ID.json
"""
import json
import requests
from sys import argv, exit


if __name__ == '__main__':
    if len(argv) != 2:
        exit(1)
    url = f"https://jsonplaceholder.typicode.com/users/{argv[1]}/todos"
    url_2 = f"https://jsonplaceholder.typicode.com/users/{argv[1]}"
    tasks = requests.get(url).json()
    user = requests.get(url_2).json()
    with open(f"{argv[1]}.json", "w") as f:
        json.dump(
            {argv[1]: [{
                "task": task["title"], "completed": task["completed"],
                "username": user['username']} for task in tasks]}, f
         )
