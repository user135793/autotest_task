from endpoints import create_user_endpoint

def create_new_user_test():
    for x in range(999999):
        y = create_user_endpoint(username='userx' + str(x), password1='password', password2='password')
        if (y == 201):
            break


create_new_user_test()


