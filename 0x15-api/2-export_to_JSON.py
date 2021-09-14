#!/usr/bin/python3
""" Gather Data from API """

if __name__ == "__main__":
    from urllib import request
    import json
    import sys

    try:
        user_id = int(sys.argv[1])
    except:
        exit()

    url_id = "https://jsonplaceholder.typicode.com/users?id=" + str(user_id)
    todo_all = "https://jsonplaceholder.typicode.com/todos"

    with request.urlopen(url_id) as url:
        employe_data = json.loads(url.read().decode())

    with request.urlopen(todo_all) as url:
        todo_all = json.loads(url.read().decode())

    name = employe_data[0].get("name")
    json_name = str(user_id) + '.json'
    print(json_name)
    data = {}
    data[user_id] = []

    for registry in todo_all:
        if int(user_id) == registry["userId"]:
            dict = {}
            for key, value in registry.items():
                if key == "title":
                    dict["task"] = value
                if key == "completed":
                    dict[key] = value
                dict["username"] = name
            data[user_id].append(dict)

    with open(json_name, 'w', newline='') as jsonfile:
        json.dump(data, jsonfile)
