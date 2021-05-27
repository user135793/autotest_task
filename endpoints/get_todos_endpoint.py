from .default import default
from endpoints import login_endpoint

def get_todos_endpoint(username = ''):
    token = default.getToken()
    default.headers["Authorization"] = "Bearer " + token

    r = default.requests.get(default.url + 'todos/' + username, headers=default.headers)

    if (r.status_code == 200):
        print('\nSuccess')
        return(r.text)
    elif (r.status_code == 401):
        login_endpoint.login_endpoint(username='user')
    else:
        print(r.text + '\nFalse')