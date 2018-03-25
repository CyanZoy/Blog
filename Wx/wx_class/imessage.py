# -*- coding: utf-8 -*-
"""
 @Time    : 2018/3/16 19:44
 @Author  : CyanZoy
 @File    : imessage.py
 @Describe:用来定义各种消息的xml模板
 """
TEXT_MESSAGE = """<xml>
<ToUserName><![CDATA[{p[toUser]}]]></ToUserName>
<FromUserName><![CDATA[{p[fromUser]}]]></FromUserName>
<CreateTime>{p[time]}</CreateTime>
<MsgType><![CDATA[text]]></MsgType>
<Content><![CDATA[{p[Content]}]]></Content>
</xml>"""


IMAGE_MESSAGE = """<xml><ToUserName>< ![CDATA[{p[toUser]}] ]></ToUserName><FromUserName>< ![CDATA[{p[fromUser]}] ]></FromUserName><CreateTime>{p[time]}</CreateTime><MsgType>< ![CDATA[image] ]></MsgType><Image><MediaId>< ![CDATA[{p[media_id]}] ]></MediaId></Image></xml>"""

IMAGE_TEXT_MESSAGE = """<xml>
<ToUserName>{p[toUser]}</ToUserName>
<FromUserName>{p[fromUser]}</FromUserName>
<CreateTime>{p[time]}</CreateTime>
<MsgType>news</MsgType>
<ArticleCount>{p[count]}</ArticleCount>
<Articles>
{p[item]}
</Articles>
</xml>"""

