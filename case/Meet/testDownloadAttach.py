#coding:utf-8
import requests
import unittest
import time
from common.login import LG
from common.logger import Log
class Attach(unittest.TestCase):
    def setUp(self):
        self.s = requests.session()
        self.lgin = LG(self.s) #实例化登录类
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
        self.log = Log()#实例化日志的类

    def test_download_attach(self):
        u'下载讲义接口'
        url = 'http://api.meet.sunnycare.com/v2/attach/mine'
        json_data = {
            "token":self.uid_token,
            "attach_code":'ss'
        }
        r = self.s.post(url,headers = self.header,json=json_data)


    def tearDown(self):
        self.s.close()

if __name__=='__main__':
    unittest.main()

