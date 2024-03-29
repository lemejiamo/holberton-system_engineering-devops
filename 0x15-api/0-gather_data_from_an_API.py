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

    # tasks do it by user

    data = employe_data[0]
    name = data["name"]
    todo_employe = []
    tasks = 0
    task_solved = 0
    for task in todo_all:
        if int(user_id) == task["userId"]:
            tasks = tasks + 1
            if task["completed"] is True:
                string = task["title"]
                task_solved = task_solved + 1
                todo_employe.append(string)

    print("Employee {} is done with tasks({}/{}):"
          .format(name,
                  task_solved,
                  tasks))

    for item in todo_employe:
        print("\t {}".format(item))
