#coding:utf-8
import time
import unittest
import requests
class LG():
    def login(self):
        '''登录方法'''
        url = 'http://api.rih.medohealth.com/API/V1/DoctorLoginForToken/doctorValidIdenfifyCodeByTelForLogin'
        header = {'User-Agent': 'LanTingDoctor/1.3.1 (iPad; iOS 10.1.1; Scale/2.00)',
                       'Accept-Encoding': 'gzip, deflate',
                       'Accept-Language': 'zh-Hans-CN;q=1',
                       'Content-Type': 'application/json',
                       'requestApp': '3',
                       'requestclient': '2',
                       'versionForApp': '1.3',
                       'Authorization': 'Basic YXBpTGFudGluZ0BtZWRsYW5kZXIuY29tOkFwaVRobWxkTWxkQDIwMTM=',
                       'Connection': 'keep-alive'}
        s = requests.session()
        t = {"loginDevice":"2","telNumber":"18351928060","identifyCode":"666666","loginCity":"no location"}  #利用杨雪的有固定验证码的账号登录
        r = s.post(url,headers=header,json=t)
        #print(r.json())

    def get_token(self):
        '''取第一步登录成功后的token作为下一步的请求体'''
        url = 'http://api.rih.medohealth.com/API/V1/DoctorLoginForToken/doctorValidIdenfifyCodeByTelForLogin'
        header = {'User-Agent': 'LanTingDoctor/1.3.1 (iPad; iOS 10.1.1; Scale/2.00)',
                       'Accept-Encoding': 'gzip, deflate',
                       'Accept-Language': 'zh-Hans-CN;q=1',
                       'Content-Type': 'application/json',
                       'requestApp': '3',
                       'requestclient': '2',
                       'versionForApp': '1.3',
                       'Authorization': 'Basic YXBpTGFudGluZ0BtZWRsYW5kZXIuY29tOkFwaVRobWxkTWxkQDIwMTM=',
                       'Connection': 'keep-alive'}
        s = requests.session()
        t = {"loginDevice":"2","telNumber":"18351928060","identifyCode":"666666","loginCity":"no location"}  #利用杨雪的有固定验证码的账号登录
        r = s.post(url,headers=header,json=t)
        success_token = r.json()['data']['Token']  #后面的很多操作会用到这个token，该token在登录成功后的步骤中作为请求的数据
        #print('success token:%s' % success_token)
        return success_token
    def get_duid(self):
        '''取第一步登录成功后的duid作为第二部登录的请求体'''
        url = 'http://api.rih.medohealth.com/API/V1/DoctorLoginForToken/doctorValidIdenfifyCodeByTelForLogin'
        header = {'User-Agent': 'LanTingDoctor/1.3.1 (iPad; iOS 10.1.1; Scale/2.00)',
                       'Accept-Encoding': 'gzip, deflate',
                       'Accept-Language': 'zh-Hans-CN;q=1',
                       'Content-Type': 'application/json',
                       'requestApp': '3',
                       'requestclient': '2',
                       'versionForApp': '1.3',
                       'Authorization': 'Basic YXBpTGFudGluZ0BtZWRsYW5kZXIuY29tOkFwaVRobWxkTWxkQDIwMTM=',
                       'Connection': 'keep-alive'}
        s = requests.session()
        t = {"loginDevice":"2","telNumber":"18351928060","identifyCode":"666666","loginCity":"no location"}  #利用杨雪的有固定验证码的账号登录
        r = s.post(url,headers=header,json=t)
        success_duid = r.json()['data']['doctorInfo']['duid']  #后面的很多操作会用到这个duid，
        #print('success duid:%s' % success_duid)
        return success_duid
    def gettoken_loginbyUID(self):
        u'取第二部UID登录成功后的token'
        url = 'http://api.rih.sunnycare.cc/API/V1/DoctorLoginForToken/doctorAutoLoginByUID'  #医生用uid自动登录接口'
        header = {'User-Agent': 'LanTingDoctor/1.3.1 (iPad; iOS 10.1.1; Scale/2.00)',
                       'Accept-Encoding': 'gzip, deflate',
                       'Accept-Language': 'zh-Hans-CN;q=1',
                       'Content-Type': 'application/json',
                       'requestApp': '3',
                       'requestclient': '2',
                       'versionForApp': '1.3',
                       'Authorization': 'Basic YXBpTGFudGluZ0BtZWRsYW5kZXIuY29tOkFwaVRobWxkTWxkQDIwMTM=',
                       'Connection': 'keep-alive'}
        s = requests.session()
        json_data1 = {"UID":str(self.get_duid()),"loginDevice":"1","loginCity":"no location"}  #device 1是安卓
        r = s.post(url,headers= header,json=json_data1) ##医生用uid自动登录接口的请求数据又是登录成功后返回的json中的duid
        UID_token = r.json()['data']['Token'] #取到我想要的token
        return UID_token

if __name__=='__main__':
    x = LG()
    x.login()
    x.get_token()
    x.get_duid()

