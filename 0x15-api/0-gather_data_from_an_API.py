#!/usr/bin/python3
"""" Python script that, using this REST API, for a given employee ID, returns
        information about his/her TODO list progress
"""
import requests
from sys import argv, exit


if len(argv) != 2:
    exit(1)
id = argv[1]
url = f"https://jsonplaceholder.typicode.com/users/{id}/todos"
url_2 = f"https://jsonplaceholder.typicode.com/users/{id}"
result = requests.get(url)
req = requests.get(url_2)
user = req.json()
tasks = result.json()
done = 0
total = 0
titles = []
for task in tasks:
    total += 1
    if task['completed']:
        done += 1
        titles.append(task['title'])
print(f"Employee {user['name']} is done with tasks({done}/{total}):")
for title in titles:
    print(f"\t {title}")
