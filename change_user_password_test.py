from endpoints import change_user_password_endpoint

def change_user_password_test():
    y = change_user_password_endpoint(username='user', old_password='password', password1='password', password2='password')
    if (y['result'] == "Password successfully updated!"):
        print('Test success')
    else:
        print('Failed')
        print(y)

change_user_password_test()