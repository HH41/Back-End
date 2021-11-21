# -*- coding : utf-8 -*-
# @Time : 2021/11/13 15:55
# @Author : zhy
# @File : CSDN_db.py
# @Software: PyCharm

import pymysql


class DataManager:
    def __init__(self, db_name):
        self.db = self.connect_to_db(db_name)

    def connect_to_db(self, db_name):
        db = pymysql.connect(host='localhost', user='root', password='020506zhhy', port=3306, db=db_name)
        return db

    def close_db(self):
        self.db.close()

    def clear_table(self):                          # 清空资讯表
        cursor = self.db.cursor()
        sql3 = 'DELETE FROM CSDN_news'
        try:
            cursor.execute(sql3)
            self.db.commit()
            print('clear table ok')
        except Exception as e:
            self.db.rollback()
            print('clear talbe error: ', e)

    def trans_to_news_table(self, data):            # 插入新的资讯
        cursor = self.db.cursor()
        sql3 = 'INSERT INTO CSDN_news(title, content) values(%s, %s)'
        try:
            cursor.execute(sql3, (data['title'], data['content']))
            self.db.commit()
            print('insert ok')
        except Exception as e:
            self.db.rollback()
            print('insert error: ', e)

    def trans_to_collection_table(self, data, wechat_id):         # 将获取到的收藏夹存入数据库
        cursor = self.db.cursor()
        sql3 = 'INSERT IGNORE INTO CSDN_collection(wechat_id,title, content) values(%s,%s, %s)'
        try:
            cursor.execute(sql3, (wechat_id, data['title'], data['content']))
            self.db.commit()
            print('insert ok')
        except Exception as e:
            self.db.rollback()
            print('insert error: ', e)

    def get_username_password(self, wechatid):                    # 从数据库中获取用户微信ID对应的CSDN账号和密码
        cursor = self.db.cursor()
        sql3 = 'SELECT * FROM csdn_username WHERE wechat_id="%s";' % wechatid
        try:
            cursor.execute(sql3)
            result = cursor.fetchall()[0]
            username = result[1]
            password = result[2]
            print(username, password)
            return username, password
        except Exception as e:
            self.db.rollback()
            print(e)


if __name__ == '__main__':
    DataManager('dbase').get_username_password('test')
