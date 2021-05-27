from endpoints import create_user_endpoint

def create_user_no_1_password_test():
    y = create_user_endpoint(username='user', password1='', password2='qweweqweqwe')
    print(y)
    if (y['message'] == "Empty fields: ['password1']"):
        print('success')
    else:
        print('False')

create_user_no_1_password_test()
