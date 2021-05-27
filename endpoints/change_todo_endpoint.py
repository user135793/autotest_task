from .default import default
from .login_endpoint import login_endpoint


def change_todo_endpoint(username = '', todo_id = '', text = '', status = 'TODO'):
    token = default.getToken()
    default.headers["Authorization"] = "Bearer " + token

    data_for_change = {'text': text, 'status': status}
    data_for_change = default.json.dumps(data_for_change)

    r = default.requests.put(default.url + 'todos/' + username + '/' + str(todo_id), headers=default.headers, data=data_for_change)
    y = default.json.loads(r.text)

    if (r.status_code == 202):
        if (y['result'] == 'Todo id:'+ todo_id + ' successfully updated!'):
            print('\nTodos changed')
            return y
        else:
            print(y)
            print('Error')
    elif (r.status_code == 401):
        login_endpoint(username='user', password='password')
    else:
        print(y)
        print('\nFalse')
        return y