# -*- codeing = utf-8 -*-
# @Time : 2021/11/9 20:49
# @Author : zhy
# @File : oschina_spider_getURL.py
# @Software: PyCharm

import requests
import parsel

headers ={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36'
}

def get_page(url):
    response = requests.get(url,headers = headers)
    #print(response.text)
    return response.text

def get_url():
    url = 'https://www.oschina.net/'
    html = get_page(url)
    s = parsel.Selector(html)
    lis = s.xpath('//div[@class="panel-content__column news-panel"][1]/div[@class="tab-page"][1]//div[@class="item"]/a/@href')  # 获取所有的a标签的链接
    #print(type(lis))
    url_lis = []
    for li in lis:
        x = li.get().split('.')
        #print(x[1])
        if(x[1] != 'oschina'):
            continue
        url_lis.append(li.get())
    #print(url_lis)
    return url_lis

if __name__== '__main__':
    get_url()