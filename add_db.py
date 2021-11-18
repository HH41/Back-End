import pymysql

class Flag:
    def __init__(self, db_name):
        self.db = self.connect_to_db(db_name)

    def connect_to_db(self, db_name):
        db = pymysql.connect(host='localhost',user='root',password='qwe1234..',port=3306,db=db_name)
        return db

    def close_db(self):
        self.db.close()

    def clear_table(self):
        cursor = self.db.cursor()
        sql3 = 'DELETE FROM users'
        try:
            cursor.execute(sql3)
            self.db.commit()
            print('clear table ok')
        except Exception as e:
            self.db.rollback()
            print('clear table error: ', e)
    def add(self,data):
        cursor = self.db.cursor()
        sql3 = 'INSERT INTO user(message, username) values(%s, %s)'
        try:
            cursor.execute(sql3, (data['message'], data['username']))
            self.db.commit()
            print('insert ok')
        except Exception as e:
            self.db.rollback()
            print('insert error: ',e)