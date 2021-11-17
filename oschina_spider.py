# -*- codeing = utf-8 -*-
# @Time : 2021/11/9 22:45
# @Author : zhy
# @File : oschina_spider.py
# @Software: PyCharm

import requests
import re
import oschina_spider_getURL
from oschina_db import DataManager

headers ={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36'
}

def get_page(url):
    response = requests.get(url,headers=headers)
    #print(response.text)
    return response.text

def parse_page(html):
    title = re.compile(r'<val data-name="weixinShareTitle" data-value="(.*?)"></val>',re.S)
    title_ans = re.search(title,html).group(1)
    content = re.compile(r'<div class="content">(.*?)</div>',re.S)
    content_ans = re.search(content,html).group(1)
    #print(title_ans)
    #print(content_ans)
    return title_ans, content_ans

def spider():
    url_lis = []
    url_lis = oschina_spider_getURL.get_url()
    db_manager = DataManager('dbase')
    db_manager.clear_table()
    for url in url_lis:
        print(url)
        data = {}
        html = get_page(url)
        title,content = parse_page(html)
        data['title'] = title
        data['content'] = content
        db_manager.trans_to_oschinadb(data)
    db_manager.close_db()

if __name__ == '__main__':
    spider()