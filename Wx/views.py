from django.shortcuts import HttpResponse
from Wx.wx_class import wxs
import time


def wx_authentication(request):
    if request.method == 'GET':
        signature = request.GET.get('signature')
        timestamp = request.GET.get('timestamp')
        nonce = request.GET.get('nonce')
        echostr = request.GET.get('echostr')
        token = 'cyanzoy'
        sh = wxs.SHA1()
        state, auth = sh.getSHA1(token, timestamp, nonce)
        if state == 0 and signature == auth:
            return HttpResponse(echostr)
        else:
            return HttpResponse('False')
    else:
        con = autoreply(request)
        return HttpResponse(con)


def autoreply(request):
    a2 = """
    <xml> 
  <ToUserName>oEKhCw5-o4Y-FKNQ5QSZjMzgMn-g</ToUserName>  
  <FromUserName>gh_1c850ea72db8</FromUserName>  
  <CreateTime>1521278977</CreateTime>  
  <MsgType>news</MsgType>  
  <ArticleCount>1</ArticleCount>  
  <Articles> 
    <item> 
      <Title>nihao</Title>  
      <Description>描述</Description>  
      <PicUrl>http://j4.dfcfw.com/charts/pic6/161725.png</PicUrl>  
      <Url>CDATA[http://www.baidu.com</Url> 
    </item> 
  </Articles> 
</xml>"""
    try:
        web_data = request.body
        state, type, touser_name, fromuser_name, con = wxs.XMLParse().extract(web_data)
        print(type)
        ass = dict()
        if type == 'text' and con != '你好':
            ass['content'] = con
        elif type == 'image':
            media_id = wxs.PullImage().pull_temporary()
            print(media_id, '-'*10)
            if str(media_id) == str(41005):
                type = 'text'
                ass['content'] = "内部错误"
            else:
                ass['media_id'] = media_id

        else:
            ass['title1'] = 'nihao'
            ass['description1'] = '描述'
            ass['picurl'] = 'http://j4.dfcfw.com/charts/pic6/161725.png'
            ass['url'] = 'http://j4.dfcfw.com/charts/pic6/161725.png'
            type = 'picT'

        resp_xml = wxs.XMLParse().generate(touser_name, fromuser_name, int(time.time()), type, **ass)
        print(resp_xml)
        return HttpResponse(resp_xml)
    except:
        print("error")





# http://j4.dfcfw.com/charts/pic6/161725.png