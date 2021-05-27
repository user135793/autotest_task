from endpoints import create_user_endpoint

def create_user_no_1_password_test():
    y = create_user_endpoint(username='user', password1='sdffgfggfhfgh', password2='qweweqweqwe')
    print(y)
    if (y['message'] == "Passwords does not match"):
        print('success')
    else:
        print('False')

create_user_no_1_password_test()
