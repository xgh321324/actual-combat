#coding:utf-8
import requests
import unittest
import xlrd
from common.login import LG
class Test_pay(unittest.TestCase):
    def setUp(self):
        self.s = requests.session()
        self.lgin = LG() #实例化登录类
        self.uid_token = self.lgin.gettoken_loginbyUID() #直接取第二部登录
        self.header = {'User-Agent': 'LanTingDoctor/1.3.1 (iPad; iOS 10.1.1; Scale/2.00)',
                       'Accept-Encoding': 'gzip, deflate',
                       'Accept-Language': 'zh-Hans-CN;q=1',
                       'Content-Type': 'application/json',
                       'requestApp': '3',
                       'requestclient': '2',
                       'versionForApp': '2.0',
                       'Authorization': 'Basic YXBpTGFudGluZ0BtZWRsYW5kZXIuY29tOkFwaVRobWxkTWxkQDIwMTM=',
                       'Connection': 'keep-alive'}

    def test_lesson_frontpage(self):
        u'测试课程首页接口'
        url = 'http://api.lesson.sunnycare.cc/v1/rec'
        json_data = {"nonce":"2hcvqaxfbau8f6cos6okr4j27um5dpr2","timestamp":"1523937360","sign":"560F0E0C35F2FFDF213512F8E6470F22","token":self.uid_token}
        r = self.s.post(url,headers = self.header,json=json_data)
        print(r.json())
        self.assertEqual('请求成功.',r.json()['note'],msg='请求返回状态不是200，有问题')
    def tearDown(self):
        self.s.close()
if __name__ == '__main__':
    unittest.main()

