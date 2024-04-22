#!/usr/bin/python3
"""" Python script that, using this REST API, for a given employee ID, returns
        information about his/her TODO list progress
"""
import requests
from sys import argv, exit


if __name__ == '__main__':
    if len(argv) != 2:
        exit(1)
    url = f"https://jsonplaceholder.typicode.com/users/{argv[1]}/todos"
    url_2 = f"https://jsonplaceholder.typicode.com/users/{argv[1]}"
    tasks = requests.get(url).json()
    user = requests.get(url_2).json()['name']
    done = [tk['title'] for tk in tasks if tk['completed']]
    print(f"Employee {user} is done with tasks({len(done)}/{len(tasks)}):")
    for title in done:
        print(f"\t {title}")
