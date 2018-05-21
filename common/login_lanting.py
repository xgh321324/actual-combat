#coding:utf-8
import requests

def auto_login_by_UID():
    header = {'User-Agent': 'LanTingDoctor/2.0.2 (iPad; iOS 10.1.1; Scale/2.00)',
                       'Accept-Encoding': 'gzip, deflate',
                       'Accept-Language': 'zh-Hans-CN;q=1',
                       'Content-Type': 'application/json',
                       'requestApp': '3',
                       'requestclient': '2',
                       'versionForApp': '2.0',
                       'Authorization': 'Basic YXBpTGFudGluZ0BtZWRsYW5kZXIuY29tOkFwaVRobWxkTWxkQDIwMTM=',
                       'Connection': 'keep-alive'
                       }
    url = 'http://api.rih.medohealth.com/API/V1/LogForToken/autoLoginByUID'
    json_data = {"uiUID":"Y7xdvSRFmWiKqEM195u6CNyt8kfrLJBH","loginDevice":"2","loginCity":"no location"}
    s = requests.session()
    r = s.post(url,headers = header,json=json_data)
    print(r.json())
    t = r.json()['data']['Token']
    print(t)
    return (t)

if __name__=='__main__':
    auto_login_by_UID()