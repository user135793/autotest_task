from .default import default

def create_user_endpoint(username = '', password1 = '', password2 = ''):

    data_login = {"username": username, "password1": password1, "password2": password2}
    data_login = default.json.dumps(data_login)

    r = default.requests.post(default.url + 'users',headers=default.headers, data=data_login)
    y = default.json.loads(r.text)

    if (r.status_code == 400):
        if (y['message'] == "User Already exist"):
            print(username + r.text)
            print(r.status_code)
            return (y)
        else:
            return(y)
    elif (r.status_code == 201):
        print('\nSuccess')
        print(r.text)
        return (r.status_code)
    else:
        print(r.status_code)
        print(r.text + '\nFalse')
        return (r.status_code)
