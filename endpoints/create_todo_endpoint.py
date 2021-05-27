from .default import default
from endpoints import login_endpoint

def create_todo_endpoint(username='', text = '', status = 'TODO'):
    token = default.getToken()
    default.headers["Authorization"] = "Bearer " + token

    todo_data = {"text": text, "status": status}
    todo_data = default.json.dumps(todo_data)

    r = default.requests.post(default.url + 'todos/' + username + '/', headers=default.headers, data=todo_data)
    y = default.json.loads(r.text)
    if (r.status_code == 201):
        if (y['result'] == 'New todo successfully created!'):
            print('\nSuccess')
            print(r.text)
        else:
            print('Error')
    elif (r.status_code == 401):
        login_endpoint.login_endpoint(username='user', password='password')
    else:
        print(r.text + '\nFalse')