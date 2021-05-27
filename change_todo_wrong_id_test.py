from endpoints importchange_todo_endpoint

def change_todo_wrong_id_test(todo_id):
    y = change_todo_endpoint(username='user', todo_id=todo_id, text='text', status='CANCELED')
    if (y['message'] == "todo id#:"+ todo_id + " not found"):
        print('Test success')
    else:
        print('Failed')
        print(y)

change_todo_wrong_id_test('1')