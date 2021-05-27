from endpoints import create_user_endpoint

def create_user_short_password_test():
    y = create_user_endpoint(username='', password1='qweqwewqe', password2='qweqweeqw')
    print(y)
    if (y['message'] == "Empty fields: ['username']"):
        print('success')
    else:
        print('False')

create_user_short_password_test()
