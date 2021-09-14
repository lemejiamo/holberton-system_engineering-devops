#!/usr/bin/python3
""" Gather Data from API """

if __name__ == "__main__":
    from urllib import request
    import json
    import sys

    url_id = "https://jsonplaceholder.typicode.com/users"
    todo_all = "https://jsonplaceholder.typicode.com/todos"

    with request.urlopen(url_id) as url:
        employe_data = json.loads(url.read().decode())

    with request.urlopen(todo_all) as url:
        todo_all = json.loads(url.read().decode())

    json_name = "todo_all_employees.json"
    data = {}
    users = []

    for user in employe_data:
        id = user["id"]
        if int(id) not in users:
            users.append(user["id"])

    for user in users:
        data[user] = []
        for registry in todo_all:
            dict = {}
            if user == registry["userId"]:
                for key, value in registry.items():
                    if key == "title":
                        dict["task"] = value
                    if key == "completed":
                        dict[key] = value
                dict["username"] = employe_data[user-1].get("name")
                data[user].append(dict)

    with open(json_name, 'w', newline='') as jsonfile:
        json.dump(data, jsonfile)
