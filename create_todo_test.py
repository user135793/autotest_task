from endpoints import create_todo_endpoint

def create_todo_test():
    y = create_todo_endpoint(username='user', text='text', status='TODO')
    print(y)

create_todo_test()