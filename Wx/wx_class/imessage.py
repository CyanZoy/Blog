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
<Content><![CDATA[{p[content]}]]></Content>
</xml>"""

IMAGE_MESSAGE = """<xml>
<ToUserName>{p[toUser]}></ToUserName>
<FromUserName>{p[fromUser]}</FromUserName>
<CreateTime>{p[time]}</CreateTime>
<MsgType>image</MsgType>
<Image>
<MediaId>{p[media_id]}</MediaId>
</Image>
</xml>"""

IMAGE_TEXT_MESSAGE = """<xml>
<ToUserName>{p[toUser]}</ToUserName>
<FromUserName>{p[fromUser]}</FromUserName>
<CreateTime>{p[time]}</CreateTime>
<MsgType>news</MsgType>
<ArticleCount>1</ArticleCount>
<Articles>
<item>
    <Title>{p[title1]}</Title> 
    <Description>{p[description1]}</Description>
    <PicUrl>{p[picurl]}</PicUrl>
    <Url>{p[url]}</Url>
</item>
</Articles>
</xml>"""

