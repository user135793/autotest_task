from endpoints import create_user_endpoint

def create_user_no_2_password_test():
    y = create_user_endpoint(username='user', password1='qweqeeqwe', password2='')
    print(y)
    if (y['message'] == "Empty fields: ['password2']"):
        print('success')
    else:
        print('False')

create_user_no_2_password_test()
