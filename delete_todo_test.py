from endpoints import delete_todo_endpoint

def delete_todo_test():
    y = delete_todo_endpoint(username='user', todo_id='50')
    print(y)

delete_todo_test()