from .default import default

def login_endpoint(username = '', password=''):
    data_login = {"username": username, "password": password}
    data_login = default.json.dumps(data_login)

    r = default.requests.post(default.url + 'login/', headers=default.headers, data=data_login)
    y = default.json.loads(r.text)

    if (r.status_code == 200):
        print('\nLogged on')

        f = open("./token.txt", "w")
        f.write(y["access_token"])
        f.close()
        return (y)
    else:
        print(r.text + '\nFalse')