from add_db import Flag

def parse(add):
    message = add.message
    message_ans = message
    username = add.username
    username_ans = username
    return message_ans, username_ans

def spider():
    db_manager = Flag('user')
    db_manager.clear_table()
    data = {}
    add={'',''}
    message, username = parse(add)
    data['message'] = message
    data['username'] = username
    db_manager.add(data)
    db_manager.close_db()

if __name__ == '__main__':
    spider()