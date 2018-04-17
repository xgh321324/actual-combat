#coding:utf-8
import requests
import unittest
from common.login import LG
import time
class ColumnInfo(unittest.TestCase):
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
    def testColumnInfo(self):
        u'测试专栏信息接口'
        url = 'http://api.lesson.sunnycare.cc/v1/spe'
        #将所有专栏的code放进list
        column_list = ['Z2018041715491952019','Z2018041617010338836','ZL2018040945462','ZL2018040912829']
        #详情介绍链接
        detail_links = []
        for i in column_list:
            json_data = {"spe_code":i,"timestamp":str(time.time()),"token":self.uid_token}
            r = self.s.post(url,headers = self.header,json=json_data)
            #print(r.json())
            detail_links.append(r.json()['data']['detail_link'])
            self.assertEqual('请求成功.',r.json()['note'],msg='专栏信息返回的状态不是请求成功，有问题！')
        #下面测试专栏介绍的链接
        for link in detail_links:
            r2 = self.s.get(link)
            self.assertEqual(200,r2.status_code,msg='专栏介绍链接返回状态码不是200！')


    def tearDown(self):
        self.s.close()
if __name__=='__main__':
    unittest.main()