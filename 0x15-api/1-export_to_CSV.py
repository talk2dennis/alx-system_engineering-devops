#!/usr/bin/python3
""""
Python script to export data in the CSV format
    Format must be: "USER_ID","USERNAME","TASK_COMPLETED_STATUS","TASK_TITLE"
    File name must be: USER_ID.csv
"""
import csv
import requests
from sys import argv, exit


if __name__ == '__main__':
    if len(argv) != 2:
        exit(1)
    url = f"https://jsonplaceholder.typicode.com/users/{argv[1]}/todos"
    url_2 = f"https://jsonplaceholder.typicode.com/users/{argv[1]}"
    tasks = requests.get(url).json()
    user = requests.get(url_2).json()
    with open(f"{argv[1]}.csv", 'w') as f:
        writer = csv.writer(f, quoting=csv.QUOTE_ALL)
        for task in tasks:
            writer.writerow(
                [argv[1], user['username'], task['completed'], task['title']]
            )
