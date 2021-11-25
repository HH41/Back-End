# -*- coding : utf-8 -*-
# @Time : 2021/11/10 19:41
# @Author : zhy
# @File : oschina_db.py
# @Software: PyCharm

import pymysql


class DataManager:
    def __init__(self, db_name):
        self.db = self.connect_to_db(db_name)

    def connect_to_db(self, db_name):
        db = pymysql.connect(host='localhost', user='root', password='密码', port=3306, db=db_name)
        return db

    def close_db(self):
        self.db.close()

    def clear_table(self):                          # 清空资讯表
        cursor = self.db.cursor()
        sql3 = 'DELETE FROM oschina_news'
        try:
            cursor.execute(sql3)
            self.db.commit()
            print('clear table ok')
        except Exception as e:
            self.db.rollback()
            print('clear talbe error: ', e)

    def trans_to_oschinadb(self, data):              # 插入新的资讯
        cursor = self.db.cursor()
        sql3 = 'INSERT INTO oschina_news(title, content) values(%s, %s)'
        try:
            cursor.execute(sql3, (data['title'], data['content']))
            self.db.commit()
            print('insert ok')
        except Exception as e:
            self.db.rollback()
            print('insert error: ', e)
