#!/usr/bin/python3
""""
Python script to export data in the JSON format.
Records all tasks that are owned by all employee
Format must be: { "USER_ID": [{"task": "TASK_TITLE", "completed":
    TASK_COMPLETED_STATUS, "username": "USERNAME"}, {"task": "TASK_TITLE",
    "completed": TASK_COMPLETED_STATUS, "username": "USERNAME"}, ... ]}
File name must be: todo_all_employees.json
"""
import json
import requests


if __name__ == '__main__':
    url = f"https://jsonplaceholder.typicode.com/users/"
    users = requests.get(url).json()
    with open("todo_all_employees.json", "w") as f:
        json.dump({
            user['id']: [{
                "task": task['title'], "completed": task['completed'],
                "username": user['username']
                } for task in requests.get(f"{url}{user['id']}/todos").json()]
            for user in users}, f)
