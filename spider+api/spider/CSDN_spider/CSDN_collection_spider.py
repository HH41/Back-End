# -*- coding : utf-8 -*-
# @Time : 2021/11/12 19:36
# @Author : zhy
# @File : CSDN_collection_spider.py
# @Software: PyCharm

import requests
from urllib.parse import urlencode
import re
from spider.CSDN_spider.CSDN_db import DataManager

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                  '(KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36'
}


# 获取和解析页面函数 get_page()、parse_page()


def get_page(url):
    html = requests.get(url, headers=headers)
    return html.text


def parse_page(html):
    title = re.compile(r' var articleTitle = "(.*?)";', re.S)
    title_ans = re.search(title, html).group(1)
    print(title_ans)
    content = re.compile(r'<article class="baidu_pl">(.*?)</article>', re.S)
    content_ans = re.search(content, html).group(1)
    # print(content_ans)
    return title_ans, content_ans


# 爬虫

def CSDN_collect_spider(wechat_id):

    db = DataManager('dbase')
    username, password = db.get_username_password(wechat_id)

    session = requests.session()
    login_url = 'https://passport.csdn.net/v1/register/pc/login/doLogin'
    data = {"loginType": "1",
            "pwdOrVerifyCode": password,
            "userIdentification": username,
            "uaToken": "",
            "webUmidToken": ""}
    response = session.post(login_url, data=data, headers=headers)

    # print(response.text)

    # 以上为模拟登录过程

    collect_list_url = 'https://mp-action.csdn.net/interact/wrapper/pc/favorite/v1/api/getFolderList?'
    params1 = {
        'username': username,
        'pageSize': 50
    }
    url = collect_list_url + urlencode(params1)
    response = session.get(url, headers=headers)
    json = response.json()
    items = json.get('data').get('list')
    floder_id = []
    for item in items:
        fid = item.get('id')
        floder_id.append(fid)

    # 以上为获取每个收藏夹id过程

    floder_url = 'https://mp-action.csdn.net/interact/wrapper/pc/favorite/v1/api/getFavoritesByFolderId?'
    collect_url_list = []
    for fid in floder_id:
        params2 = {
            'folderId': fid,
            'page': 1,
            'pageSize': 10,
            'sources': '',
            'username': username
        }
        url = floder_url + urlencode(params2)
        response = session.get(url, headers=headers)
        json = response.json()
        items = json.get('data').get('list')
        for item in items:
            u = item.get('url')
            collect_url_list.append(u)

    # 以上为获取收藏夹中博客url过程

    db = DataManager('dbase')
    for url in collect_url_list:
        data = {}
        html = get_page(url)
        title, content = parse_page(html)
        data['title'] = title
        data['content'] = content
        db.trans_to_collection_table(data, wechat_id)
    db.close_db()


if __name__ == '__main__':
    CSDN_collect_spider('test3')
