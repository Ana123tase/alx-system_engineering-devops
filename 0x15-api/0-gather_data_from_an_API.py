#!/usr/bin/python3
import requests
import sys

def fetch_employee_todo_progress(employee_id):
    base_url = 'https://jsonplaceholder.typicode.com/users'
    user_url = f'{base_url}/{employee_id}'
    todos_url = f'{user_url}/todos'

    try:
        user_response = requests.get(user_url)
        user_response.raise_for_status()
        todos_response = requests.get(todos_url)
        todos_response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        sys.exit(1)

    user_data = user_response.json()
    todos_data = todos_response.json()

    employee_name = user_data['name']
    total_tasks = len(todos_data)
    done_tasks = [task['title'] for task in todos_data if task['completed']]

    print(f"Employee {employee_name} is done with tasks ({len(done_tasks)}/{total_tasks}):")
    for task in done_tasks:
        print(f"\t{task}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 script.py <employee_id>")
        sys.exit(1)

    employee_id = sys.argv[1]
    fetch_employee_todo_progress(employee_id)
