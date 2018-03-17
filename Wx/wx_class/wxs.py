# -*- encoding:utf-8 -*-
import hashlib
import xml.etree.cElementTree as ET
from Wx.wx_class import imessage, get_access_token as GA, ierror
import os
import requests


class SHA1:
    """计算公众平台的消息签名接口"""

    def getSHA1(self, token, timestamp, nonce):
        """用SHA1算法生成安全签名
        @param token:  票据
        @param timestamp: 时间戳
        @param encrypt: 密文
        @param nonce: 随机字符串
        @return: 安全签名
        """
        try:
            sortlist = [token, timestamp, nonce]
            sortlist.sort()
            sha = hashlib.sha1()
            sha.update("".join(sortlist).encode('utf-8'))
            return ierror.WXBizMsgCrypt_OK, sha.hexdigest()
        except Exception as e:
            print(e)
            return ierror.WXBizMsgCrypt_ComputeSignature_Error, None


class XMLParse:
    """提供提取消息格式中的密文及生成回复消息格式的接口"""

    def extract(self, xmltext):
        """提取出xml数据包中的加密消息
        @param xmltext: 待提取的xml字符串
        @return: 提取出的加密消息字符串
        """
        try:
            print(xmltext)
            xml_tree = ET.fromstring(xmltext)
            msg_type = xml_tree.find("MsgType").text
            touser_name = xml_tree.find("ToUserName")
            fromuser_name = xml_tree.find("FromUserName")
            con = ''
            if msg_type == 'text':
                content = xml_tree.find('Content')
                con = content
            elif msg_type == 'image':
                media_id = xml_tree.find('MediaId')
                con = media_id

            return ierror.WXBizMsgCrypt_OK, msg_type, touser_name.text, fromuser_name.text, con.text
        except Exception as e:
            print("wxs->wxtract", e)
            return ierror.WXBizMsgCrypt_ParseXml_Error, None, None

    def generate(self, touser_name, fromuser_name, timestamp, type, **kwargs):
        """生成xml消息
        @param content: 消息内容
        @param touser_name: 我
        @param timestamp: 时间戳
        @param fromuser_name: 来者
        @return: 生成的xml字符串
        """

        resp_dict = {
            'toUser': fromuser_name,
            'fromUser': touser_name,
            'time': timestamp,
        }
        for key in kwargs:
            if key == 'content':
                resp_dict[key] = kwargs[key]
            if key == 'media_id':
                resp_dict[key] = kwargs[key]
            if key == 'title1':
                resp_dict[key] = kwargs[key]
            if key == 'description1':
                resp_dict[key] = kwargs[key]
            if key == 'picurl':
                resp_dict[key] = kwargs[key]
            if key == 'url':
                resp_dict[key] = kwargs[key]

        resp_xml = ''

        if type == 'text':
            resp_xml = imessage.TEXT_MESSAGE.format(p=resp_dict)
        elif type == 'image':
            resp_xml = imessage.IMAGE_MESSAGE.format(p=resp_dict)
        elif type == 'picT':
            resp_xml = imessage.IMAGE_TEXT_MESSAGE.format(p=resp_dict)

        return resp_xml


class PullImage:
    """提供上传素材的接口"""
    path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    tem_url = 'https://api.weixin.qq.com/cgi-bin/media/upload?access_token={p[access_token]}&type={p[type]}'

    def pull_temporary(self):
        """
        上传临时素材接口
        :return:media_id
        """
        # f = open(self.path+'/images/code.jpg', 'rb')
        payload_img = {
            'access_token': GA.AccT().acc(),
            'type': 'image'
        }
        data = {'media': open('code.jpg', 'rb')}
        r = requests.post(url=self.tem_url.format(p=payload_img), files=data)
        print(r.url, r.status_code)
        dicts = r.json()
        if 'errcode' in dicts:
            return dicts
        else:
            return dicts['media_id']

    def pull_permanent(self):
        """上传永久素材接口
        :return:media_id
        """


if __name__ == "__main__":

    p = PullImage().pull_temporary()
    print(p)




