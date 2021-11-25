# -*- codeing = utf-8 -*-
# @Time : 2021/11/13 15:55
# @Author : zhy
# @File : CSDN_db.py
# @Software: PyCharm

import pymysql

class DataManager:
    def __init__(self, db_name):
        self.db = self.connect_to_db(db_name)

    def connect_to_db(self, db_name):
        db = pymysql.connect(host='localhost',user='root',password='密码',port=3306,db=db_name)
        return db

    def close_db(self):
        self.db.close()

    def clear_table(self):
        cursor = self.db.cursor()
        sql3 = 'DELETE FROM CSDN_news'
        try:
            cursor.execute(sql3)
            self.db.commit()
            print('clear table ok')
        except Exception as e:
            self.db.rollback()
            print('clear talbe error: ', e)

    def trans_to_news_table(self, data):
        cursor = self.db.cursor()
        sql3 = 'INSERT INTO CSDN_news(title, content) values(%s, %s)'
        try:
            cursor.execute(sql3, (data['title'], data['content']))
            self.db.commit()
            print('insert ok')
        except Exception as e:
            self.db.rollback()
            print('insert error: ', e)

    def trans_to_collection_table(self, data,wechat_id):
        cursor = self.db.cursor()
        sql3 = 'INSERT IGNORE INTO CSDN_collection(wechat_id,title, content) values(%s,%s, %s)'
        try:
            cursor.execute(sql3, (wechat_id,data['title'], data['content']))
            self.db.commit()
            print('insert ok')
        except Exception as e:
            self.db.rollback()
            print('insert error: ', e)