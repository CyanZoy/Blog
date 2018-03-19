# -*- encoding:utf-8 -*-
import hashlib
import xml.etree.cElementTree as ET
from Wx.wx_class import imessage, get_access_token as GA, ierror
import os
import requests
from Wx import models
from spider import fund_spider


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
        @return: 节点与内容的dict
        """
        xml_tree = ET.fromstring(xmltext)
        xml_resp = dict()
        for _ in xml_tree:
            xml_resp[_.tag] = _.text

        return xml_resp

    def generate(self, timestamp, **kwargs):
        """生成xml消息
        :param timestamp: 时间戳
        :param kwargs:用户发送过来的xml内容
        :return: 回复消息的xml
        """
        item = """<item><Title>{p[0]} {p[1]}%</Title> 
                <Description>{p[1]}</Description>
                <PicUrl>{p[2]}</PicUrl>
                <Url>{p[2]}</Url>
                </item>"""
        items = ""
        resp_dict = {'toUser': kwargs['FromUserName'], 'fromUser': kwargs['ToUserName'], 'time': timestamp}
        filter_key = {'FromUserName', 'CreateTime', 'ToUserName', 'MsgId'}
        lis = [_ for _ in kwargs if _ not in filter_key]
        for key in lis:
            resp_dict[key] = kwargs[key]

        if kwargs['MsgType'] == 'text':
            return imessage.TEXT_MESSAGE.format(p=resp_dict)
        elif kwargs['MsgType'] == 'image':
            return imessage.IMAGE_MESSAGE.format(p=resp_dict)
        elif kwargs['MsgType'] == 'event':
            code = models.Fund.objects.all().values('fund_code')
            lis = []
            for _ in code:
                lis.append(_['fund_code'])

            fund_spider.Grab(lis).get_fund_info()
            fu = models.Fund.objects.all().values_list('fund_name', 'fund_rise_fall', 'fund_pic_url')
            resp_dict['count'] = len(fu)
            for _ in fu:
                items += item.format(p=_)
            resp_dict['item'] = items
            print(resp_dict)

            return imessage.IMAGE_TEXT_MESSAGE.format(p=resp_dict)


class PullImage:
    """提供上传素材的接口"""
    path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    tem_url = 'https://api.weixin.qq.com/cgi-bin/media/upload?access_token={p[access_token]}&type={p[type]}'

    def pull_temporary(self):
        """
        上传临时素材接口
        :return:media_id
        """
        f = open(self.path+'/images/czy.jpg', 'rb')
        payload_img = {
            'access_token': GA.AccT().acc(),
            'type': 'image'
        }
        r = requests.post(url=self.tem_url.format(p=payload_img), files={'media': f})
        dicts = r.json()
        if 'errcode' in dicts:
            return dicts['errcode']
        else:
            return dicts['media_id']

    def pull_permanent(self):
        """上传永久素材接口
        :return:media_id
        """


class ManagerMenus:
    """提供菜单管理接口"""
    create_url = ' https://api.weixin.qq.com/cgi-bin/menu/create?access_token={}'

    def create(self):
        tes = """{"button":
        [
            {
                "sub_button":[
                    {"name":"Blog","type":"view","url":"http://www.cyanzoy.top/myBlog"},
                    {"name":"基金1","type": "click","key": "V1003_fund"}
                ],"name":"个人网站","type":null
            },
            {
                "sub_button":[
                    {"type":"view","name":"余姚公交","url":"http://www.cyanzoy.top:8520"},
                    {"type":"click","name":"基金","key":"V1001_fund"}
                ],"name":"菜单","type":null
            }
        ]}"""

        r = requests.post(url=self.create_url.format(GA.AccT().acc()), data=tes.encode('utf-8'))
        print(r.url)
        print(r.content)


if __name__ == "__main__":

    # p = PullImage().pull_temporary()
    # print(p)
    p = ManagerMenus().create()



