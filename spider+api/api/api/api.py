# -*- coding : utf-8 -*-
# @Time : 2021/11/12 10:23
# @Author : zhy
# @File : api.py
# @Software: PyCharm

from dbase_operate import oschina_news, db, app, CSDN_news, cnblogs_news, CSDN_collection, CSDN_username
import json
from flask import request
from spider.CSDN_spider.CSDN_collection_spider import CSDN_collect_spider


db.init_app(app)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
app.config['JSON_AS_ASCII'] = False
app.secret_key = "123"


@app.route("/oschinanews/titlelist", methods=["GET"])            # oschina热点资讯标题接口
def oschina_titlelist():
    s = oschina_news()
    list_ans = []                                                # 需要返回的标题列表
    list_ans = s.title_list()
    dict1 = {'statu': 200, 'msg': 'Success'}
    json1 = json.loads(json.dumps(dict1))
    json1['titlelist'] = list_ans
    return json1


@app.route("/oschinanews/content/<title>", methods=["GET"])      # oschina热点资讯内容接口
def oschina_content(title):                                      # 参数：需要返回内容的文章的标题
    s = oschina_news()
    dict1 = {'statu': 200, 'msg': 'Success'}
    dict2 = {'statu': 404, 'msg': 'Title Loss'}
    dict3 = {'statu': 404, 'msg': 'Content Loss'}
    try:
        # my_json = request.get_json()
        # print(my_json)
        get_title = title

        if not get_title:
            return json.loads(json.dumps(dict2))

        content = s.content_details(get_title)
        json1 = json.loads(json.dumps(dict1))
        json1['content'] = content
        return json1
    except Exception as e:
        print(e)
        return json.loads(json.dumps(dict3))


@app.route("/csdnnews/titlelist", methods=["GET"])                  # CSDN热点资讯标题接口
def csdn_news_titlelist():
    s = CSDN_news()
    list_ans = []
    list_ans = s.title_list()
    dict1 = {'statu': 200, 'msg': 'Success'}
    json1 = json.loads(json.dumps(dict1))
    json1['titlelist'] = list_ans
    return json1


@app.route("/csdnnews/content/<title>", methods=["GET"])            # CSDN热点资讯内容接口
def csdn_news_content(title):                                       # 参数：需要返回内容的文章的标题
    s = CSDN_news()
    dict1 = {'statu': 200, 'msg': 'Success'}
    dict2 = {'statu': 404, 'msg': 'Title Loss'}
    dict3 = {'statu': 404, 'msg': 'Content Loss'}
    try:
        # my_json = request.get_json()
        # print(my_json)
        get_title = title

        if not get_title:
            return json.loads(json.dumps(dict2))

        content = s.content_details(get_title)
        json1 = json.loads(json.dumps(dict1))
        json1['content'] = content
        return json1
    except Exception as e:
        print(e)
        return json.loads(json.dumps(dict3))


@app.route("/cnblogsnews/titlelist", methods=["GET"])                     # 博客园热点资讯标题接口
def cnblogs_news_titlelist():
    s = cnblogs_news()
    list_ans = []
    list_ans = s.title_list()
    dict1 = {'statu': 200, 'msg': 'Success'}
    json1 = json.loads(json.dumps(dict1))
    json1['titlelist'] = list_ans
    return json1


@app.route("/cnblogsnews/content/<title>", methods=["GET"])                # 博客园热点资讯内容接口
def cnblogs_news_content(title):                                           # 参数：需要返回内容的文章的标题
    s = cnblogs_news()
    dict1 = {'statu': 200, 'msg': 'Success'}
    dict2 = {'statu': 404, 'msg': 'Title Loss'}
    dict3 = {'statu': 404, 'msg': 'Content Loss'}
    try:
        # my_json = request.get_json()
        # print(my_json)
        get_title = title

        if not get_title:
            return json.loads(json.dumps(dict2))

        content = s.content_details(get_title)
        json1 = json.loads(json.dumps(dict1))
        json1['content'] = content
        return json1
    except Exception as e:
        print(e)
        return json.loads(json.dumps(dict3))


@app.route("/csdncollection/titlelist/<wechatid>", methods=["GET"])        # CSDN收藏夹文章标题接口
def csdn_collection_titlelist(wechatid):                                   # 参数：微信ID或其他能唯一标识微信用户的字符串
    s = CSDN_collection()
    list_ans = []
    list_ans = s.title_list(wechatid)
    dict1 = {'statu': 200, 'msg': 'Success'}
    json1 = json.loads(json.dumps(dict1))
    json1['titlelist'] = list_ans
    return json1


@app.route("/csdncollection/content/<title>", methods=["GET"])             # CSDN收藏夹文章内容接口
def csdn_collection_content(title):                                        # 参数：需要返回内容的文章的标题
    s = CSDN_collection()
    dict1 = {'statu': 200, 'msg': 'Success'}
    dict2 = {'statu': 404, 'msg': 'Title Loss'}
    dict3 = {'statu': 404, 'msg': 'Content Loss'}
    try:
        # my_json = request.get_json()
        # print(my_json)
        get_title = title

        if not get_title:
            return json.loads(json.dumps(dict2))

        content = s.content_details(get_title)
        json1 = json.loads(json.dumps(dict1))
        json1['content'] = content
        return json1
    except Exception as e:
        print(e)
        return json.loads(json.dumps(dict3))


@app.route("/csdncollection/username", methods=["POST"])                      # CSDN账号密码接口
def csdn_username():
    s = CSDN_username()
    dict1 = {'statu': 200, 'msg': 'Success'}
    dict2 = {'statu': 400, 'msg': 'Failed'}
    try:
        my_json = request.get_json()
        print(my_json)
        wechatid = my_json.get("wechatid")
        username = my_json.get("username")
        password = my_json.get("password")

        if not wechatid or not username or not password:
            return json.loads(json.dumps(dict2))

        s.insert_username(wechatid, username, password)

        return json.loads(json.dumps(dict1))
    except Exception as e:
        print(e)
        return json.loads(json.dumps(dict2))


@app.route("/collectionspider/<wechatid>", methods=["GET"])            # 运行CSDN收藏夹爬虫接口
def run_csdn_collection_spider(wechatid):                              # 参数：微信ID或其他能唯一标识微信用户的字符串
    dict1 = {'statu': 200, 'msg': 'Run Spider Successfully'}
    dict2 = {'statu': 400, 'msg': 'Failed to Run Spider'}
    try:
        CSDN_collect_spider(wechatid)
        json1 = json.loads(json.dumps(dict1))
        return json1
    except Exception as e:
        print(e)
        return json.loads(json.dumps(dict2))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
