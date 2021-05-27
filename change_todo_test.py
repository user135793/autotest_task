from endpoints importchange_todo_endpoint

def change_todo_test():
    y = change_todo_endpoint(username='user', todo_id='10', text='text', status='CANCELED')
    print(y)

change_todo_test()