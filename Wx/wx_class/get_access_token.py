# -*- coding: utf-8 -*-
"""
 @Time    : 2018/3/17 12:44
 @Author  : CyanZoy
 @File    : get_access_token.py
 @Describe:获取sccess_token
 """
import requests
import json
import time
import os, django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Blog.settings')
django.setup()
from Wx.models import acc


class AccT:
    """accstoken管理"""
    def __init__(self):
        self.APPID = 'wx8947539b9ba847b2'
        self.APPSECRET = '00d6c285b0b6d2fea8afe57a52120aa6'
        self.url = 'https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid={}&secret={}'

    def get_acc(self):
        """
        获取accesstoken
        :return: accesstoken
        """
        result = requests.get(self.url.format(self.APPID, self.APPSECRET)).content.decode('utf-8')
        return json.loads(result)

    def acc(self):
        """
        提供accesstoken保存与更新接口
        :return:accesstoken
        """
        a = acc.objects.all()
        if a:
            b = a.values('id', 'accesstoken', 'accesstoken_time', 'expires_in')[0]
            num = b['id']
            access_token = b['accesstoken']
            accesstoken_time = b['accesstoken_time']
            expires_in = b['expires_in']

            current = int(time.time())
            if current - accesstoken_time > int(expires_in):
                result = self.get_acc()
                access_token = result['access_token']
                expires_in = result['expires_in']
                current_time = int(time.time())
                acc.objects.filter(id=num).update(accesstoken=access_token, expires_in=expires_in,
                                                  accesstoken_time=current_time)
                return access_token
            else:
                return access_token


        else:
            # current_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
            result = self.get_acc()
            access_token = result['access_token']
            expires_in = result['expires_in']
            current_time = int(time.time())
            a = acc(accesstoken=access_token, expires_in=expires_in, accesstoken_time=current_time)
            a.save()

            return access_token


if __name__ == "__main__":
    dl = AccT()
    print(dl.acc())

