from endpoints import login_endpoint

def login_test():
    y = login_endpoint(username='user', password='password')
    if (y['access_token']):
        print('Logged on')
    else:
        print('error')

login_test()