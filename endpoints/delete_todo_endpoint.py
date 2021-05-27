from .default import default
from endpoints import get_todos_endpoint, delete_todo_endpoint

def delete_todo_endpoint(username, todo_id):
    token = default.getToken()
    default.headers["Authorization"] = "Bearer " + token

    r = default.requests.delete(default.url + 'todos/' + username + '/' + str(todo_id), headers=default.headers)
    y = default.json.loads(r.text)

    if (r.status_code == 200):
        print(r.status_code)
        print('\nSuccess')
    elif (r.status_code == 401):
        test.login_test(self, username='user', password='password')

    elif (r.status_code == 404):
        # test.create_todo(self, username='user', text='blabla', status='TODO')
        all = get_todos_endpoint( username='user')
        all = default.json.loads(all)
        if (all):
            new_id = str(all[0]['id'])
            print(new_id)
            delete_todo_endpoint(username, new_id)
        else:
            print('list out of range')
    else:
        print(r.text)
        print('\nFalse')