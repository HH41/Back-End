# -*- coding : utf-8 -*-
# @Time : 2021/11/12 10:38
# @Author : zhy
# @File : dbase_operate.py
# @Software: PyCharm

from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from sqlalchemy.databases import mysql

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = 'mysql+pymysql://root:密码@127.0.0.1:3306/sys'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SECRET_KEY"] = "zzz"

db = SQLAlchemy(app)

# 每个类对应数据库中的一个表，其中包含需要对表进行的操作


class oschina_news(db.Model):                           # oschina热点>资讯表
    __tablename__ = "oschina_news"
    title = db.Column(db.VARCHAR(100), primary_key=True)
    content = db.Column(mysql.MSMediumText, nullable=False)

    def title_list(self):
        s = oschina_news.query.all()
        # print(s[0].title)
        list1 = []
        for i in s:
            list1.append(i.title)
        # print(list1)
        return list1

    def content_details(self, title_name):
        s = oschina_news.query.filter_by(title=title_name).first()
        # print(type(s))
        # print(s.content)
        return s.content


class CSDN_news(db.Model):                              # CSDN热点资讯
表
    __tablename__ = "csdn_news"
    title = db.Column(db.VARCHAR(100), primary_key=True)
    content = db.Column(mysql.MSMediumText, nullable=False)

    def title_list(self):
        s = CSDN_news.query.all()
        # print(s[0].title)
        list1 = []
        for i in s:
            list1.append(i.title)
        # print(list1)
        return list1

    def content_details(self, title_name):
        s = CSDN_news.query.filter_by(title=title_name).first()
        # print(type(s))
        # print(s.content)
        return s.content


class cnblogs_news(db.Model):                            # 博客园热点>资讯表
    __tablename__ = "cnblogs_news"
    title = db.Column(db.VARCHAR(100), primary_key=True)
    content = db.Column(mysql.MSMediumText, nullable=False)

    def title_list(self):
        s = cnblogs_news.query.all()
        # print(s[0].title)
        list1 = []
        for i in s:
            list1.append(i.title)
        # print(list1)
        return list1

    def content_details(self, title_name):
        s = cnblogs_news.query.filter_by(title=title_name).first()
        # print(type(s))
        # print(s.content)
        return s.content


class CSDN_collection(db.Model):                           # CSDN收藏>夹表
    __tablename__ = "csdn_collection"
    wechat_id = db.Column(db.VARCHAR(100), primary_key=True)
    title = db.Column(db.VARCHAR(100), primary_key=True)
    content = db.Column(mysql.MSMediumText, nullable=False)

    def title_list(self, weichatid):
        s = CSDN_collection.query.filter_by(wechat_id=weichatid)
        # print(s[0].title)
        list1 = []
        for i in s:
            list1.append(i.title)
        # print(list1)
        return list1

    def content_details(self, title_name):
        s = CSDN_collection.query.filter_by(title=title_name).first()
        # print(type(s))
        # print(s.content)
        return s.content


class CSDN_username(db.Model):                             # CSDN账号>密码表
    __tablename__ = "csdn_username"
    wechat_id = db.Column(db.VARCHAR(100), primary_key=True)
    username = db.Column(db.VARCHAR(100), nullable=False)
    password = db.Column(db.VARCHAR(100), nullable=False)

    def insert_username(self, wechatid, username, password):
        try:
            s = CSDN_username(wechat_id=wechatid, username=username, password=password)
            db.session.add(s)
            db.session.commit()
            print("insert ok")
        except Exception as e:
            db.session.rollback()
            print(e)


if __name__ == '__main__':
    # oschina_news().content_details('忍不了糟糕平台，程序员开源新项目并“碾压”价值7.5亿的官方版')
    # CSDN_collection().title_list('test')
    # CSDN_collection().content_details('刷了几千道算法题，这些我私藏的刷题网站都在这里了！')
    pass
