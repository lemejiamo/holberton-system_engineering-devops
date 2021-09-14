#!/usr/bin/python3
""" Gather Data from API """

if __name__ == "__main__":
    from urllib import request
    import csv
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
    csv_name = str(user_id) + '.csv'

    with open(csv_name, 'w', newline='') as csvfile:
        file = csv.writer(csvfile, delimiter=',',
                          quotechar='"', quoting=csv.QUOTE_ALL)
        for registry in todo_all:
            if int(user_id) == registry["userId"]:
                task_status = registry["completed"]
                task_title = registry['title']
                file.writerow([user_id,
                               name,
                               task_status,
                               task_title])
