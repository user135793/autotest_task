from endpoints import create_user_endpoint

def create_user_short_password_test():
    y = create_user_endpoint(username='user', password1='godgo', password2='godgo')
    print(y)
    if (y['message'] == "password to short. Min length is 6 chars"):
        print('success')
    else:
        print('False')

create_user_short_password_test()
