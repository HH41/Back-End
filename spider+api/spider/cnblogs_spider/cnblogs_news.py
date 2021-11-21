# -*- coding : utf-8 -*-
# @Time : 2021/11/12 20:44
# @Author : zhy
# @File : cnblogs_news.py
# @Software: PyCharm

import requests
import re
import parsel
from cnblogs_db import DataManager

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 ('
                  'KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36'
}

# 获取和解析页面函数 get_page()、parse_page()


def get_page(url):
    response = requests.get(url, headers=headers)
    # print(response.text)
    return response.text


def parse_page(html):
    s = parsel.Selector(html)
    title_ans = s.xpath('//h1/a/span/text()').get()
    content = re.compile(r'<div class="postBody">(.*?)</div>', re.S)
    content_ans = re.search(content, html).group(1)
    # print(title_ans)
    # print(content_ans)
    return title_ans, content_ans


def cnblogs_news_spider():
    topviews_url = 'https://www.cnblogs.com/aggsite/SideRight'
    response = requests.get(topviews_url)
    html = response.text
    s = parsel.Selector(html)
    lis = s.xpath('//div[1]/ul//a/@href')       # xpath获取URL
    url_lis = []
    for li in lis:
        url_lis.append(li.get())

    db_manager = DataManager('dbase')
    db_manager.clear_table()
    for url in url_lis:
        print(url)
        data = {}
        html = get_page(url)
        title, content = parse_page(html)
        data['title'] = title
        data['content'] = content
        db_manager.trans_to_news_table(data)
    db_manager.close_db()


if __name__ == '__main__':
    cnblogs_news_spider()
