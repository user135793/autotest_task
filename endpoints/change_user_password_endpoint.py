from .default import default


def change_user_password_endpoint( username = '', old_password = '', password1 = '', password2 = ''):
    token = default.getToken()
    default.headers["Authorization"] = "Bearer " + token

    data_for_change = {"username": username, "old_password": old_password, 'password1': password1, 'password2': password2}
    data_for_change = default.json.dumps(data_for_change)

    r = default.requests.put(default.url + 'users/', headers=default.headers, data=data_for_change)
    y = default.json.loads(r.text)

    if(r.status_code == 202):
        if(y['result'] == 'Password successfully updated!'):
            print(y)
            print('\nSuccess')
            return y
        else:
            print('Error')
            return y
    elif (r.status_code == 401):
        test.login_test('user', 'password')
    else:
        print(r.text)
        print('\nFalse')
        return y