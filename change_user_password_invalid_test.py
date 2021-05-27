from endpoints import change_user_password_endpoint

def change_user_password_invalid_test():
    y = change_user_password_endpoint(username='user', old_password='asd', password1='password', password2='password')
    if (y['message'] == "invalid password"):
        print('Test success')
    else:
        print('Failed')
        print(y)

change_user_password_invalid_test()