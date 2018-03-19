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
    try:
        web_data = request.body
        xml_resp = wxs.XMLParse().extract(web_data)

        resp_xml = wxs.XMLParse().generate(int(time.time()), **xml_resp)
        # print(resp_xml, '-'*5)
        return HttpResponse(resp_xml)
    except:
        print("view中error")





# http://j4.dfcfw.com/charts/pic6/161725.png