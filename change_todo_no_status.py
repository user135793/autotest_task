from endpoints import change_todo_endpoint

def change_todo_no_status_test():
    y = change_todo_endpoint(username='user', todo_id='10', text='text', status='')
    if (y['message'] == "Status mast be 'TODO', 'INPROGRESS', 'DONE' or 'CANCELED'"):
        print('Test success')
    else:
        print('Failed')
        print (y)

change_todo_no_status_test()