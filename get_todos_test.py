from endpoints import get_todos_endpoint

def get_todos_test():
    y = get_todos_endpoint(username='user')
    print(y)

get_todos_test()
y = login_endpoint('user', 'password')
print(y)