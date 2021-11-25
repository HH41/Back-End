# -*- coding : utf-8 -*-
# @Time : 2021/11/12 15:11
# @Author : zhy
# @File : CSDN_news_spider.py
# @Software: PyCharm

import requests
from urllib.parse import urlencode
import re
from CSDN_db import DataManager

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                  '(KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36'
}


def get_url_json(base_url):
    params = {
        'page': 0,
        'pageSize': 25
    }
    url = base_url + urlencode(params)
    # print(url)
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.json()
    except requests.ConnectionError as e:
        print('Error', e.args)

# 获取热点资讯的URL


def get_urls():
    base_url = 'https://blog.csdn.net/phoenix/web/blog/hot-rank?'
    json = get_url_json(base_url)
    url_lis = []
    if json:
        items = json.get('data')
        i = 1
        for item in items:
            item = item.get('articleDetailUrl')
            url_lis.append(item)
            i += 1
            if i == 11:
                break
        # print(len(url_lis))
        # print(url_lis)
    return url_lis

# 获取和解析页面函数 get_page()、parse_page()


def get_page(url):
    html = requests.get(url, headers=headers)
    return html.text


def parse_page(html):
    title = re.compile(r' var articleTitle = "(.*?)";', re.S)
    title_ans = re.search(title, html).group(1)
    # print(title_ans)
    content = re.compile(r'<article class="baidu_pl">(.*?)</article>', re.S)
    content_ans = re.search(content, html).group(1)
    # print(content_ans)
    return title_ans, content_ans


def spider():
    url_lis = []
    url_lis = get_urls()
    db_manager = DataManager('sys')
    db_manager.clear_table()
    for url in url_lis:
        data = {}
        html = get_page(url)
        title, content = parse_page(html)
        data['title'] = title
        data['content'] = content
        db_manager.trans_to_news_table(data)
    db_manager.close_db()


if __name__ == '__main__':
    spider()
