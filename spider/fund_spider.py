# -*- coding: utf-8 -*-
"""
 @Time    : 2018/3/18 12:24
 @Author  : CyanZoy
 @File    : fund_spider.py
 @Describe: 用户爬取基金网站的内容
 """
from lxml import etree
import requests
import os, django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Blog.settings")
django.setup()
from Wx.models import Fund
import time, random
import json
import re


class Grab:
    def __init__(self, args):
        self.url = args
        self.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                                      'Chrome/55.0.2883.87 UBrowser/6.2.3964.2 Safari/537.36'}
        self.server = 'http://fundgz.1234567.com.cn/js/{:0>6}.js?rt={}'

    def get_fund_info(self):
        pass
        start_url = [self.server.format(i, int(time.time())) for i in self.url]
        for _ in start_url:
            con = requests.get(_, headers=self.headers).content.decode('utf-8')
            data = json.loads(re.findall('{.*}', con)[0])
            Fund.objects.filter(fund_code=data['fundcode']).update(fund_rise_fall=data['gszzl'],
                fund_pic_url="http://j4.dfcfw.com/charts/pic6/{}.png?v={}".format(data['fundcode'], random.random()),
                fund_update_time=time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()))


if __name__ == "__main__":
    d = (1, 3, 3, 5)
    dl = Grab(d)
    # dl.get_fund_info()

