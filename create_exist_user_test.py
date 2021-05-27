from endpoints import create_user_endpoint

def create_exist_user_test():
    y = create_user_endpoint(username='user', password1='password', password2='password')
    print(y)
    if (y['message'] == 'User Already exist'):
        print('success')
    else:
        print('False')

create_exist_user_test()





#a.login_test('user', 'password')

#a.create_exist_user_test(username='user', password='password')
#a.create_user_no_password_test(username='user')
#a.create_user_not_match_password_test(username='user', password='password')
#a.create_user_no_1_password_test(username='user', password='password')
#a.create_user_no_2_password_test(username='user', password='password')
#a.get_todos_test(username='user')
#a.create_todo(username='user', text='blabla', status='TODO')
#a.change_user_password_test(username='user', old_password='password', password='password')
#a.change_todo(username='user', todo_id='10', text='blabla', status='CANCELED')
#a.delete_todo(username='user', todo_id='11')
