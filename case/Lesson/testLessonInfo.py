#coding:utf-8
import requests
import unittest
from common.login import LG
import time
from common.logger import Log
import urllib3
urllib3.disable_warnings()
class LessonInfo(unittest.TestCase):
    log = Log()#实例化记录日志的类
    def setUp(self):
        self.s = requests.session()
        self.lgin = LG(self.s) #实例化登录类
        self.lgin.login()
        self.uid_token = self.lgin.login() #直接取第二部登录
        self.header = {'User-Agent': 'LanTingDoctor/1.3.1 (iPad; iOS 10.1.1; Scale/2.00)',
                       'Accept-Encoding': 'gzip, deflate',
                       'Accept-Language': 'zh-Hans-CN;q=1',
                       'Content-Type': 'application/json',
                       'requestApp': '3',
                       'requestclient': '2',
                       'versionForApp': '2.0',
                       'Authorization': 'Basic YXBpTGFudGluZ0BtZWRsYW5kZXIuY29tOkFwaVRobWxkTWxkQDIwMTM=',
                       'Connection': 'keep-alive'
                       }
    def testLessonList(self):
        u'测试课程列表'
        self.log.info('-----开始测试课程列表接口-----')
        url = 'https://api.lesson.wrightin.com/v1/lesson/list'
        json_data = {"timestamp":str(time.time()),"token":self.uid_token,"time":"0"}
        r = self.s.post(url,headers = self.header,json=json_data,verify=False)
        self.log.info('课程列表返回：%s' % r.json())
        #判断课程列表获取是否成功
        self.assertEqual('请求成功.',r.json()['note'],msg='返回的状态不是请求成功！！！')
        self.log.info('------------测试结束--------')
        #将lesson_code保存至txt留下一接口所用
        with open(r'C:\Users\Administrator\Desktop\test_data.txt','w') as f:
            for i in r.json()['data']['list']:
                f.write((i['lesson_code'])+'\n')

    def testLessonInfo(self):
        u'测试课程信息'
        self.log.info('------开始测试课程信息接口---------')
        url = 'https://api.lesson.wrightin.com/v1/lesson'

        #从txt读取上个接口的lesson_codes来循环post
        with open(r'C:\Users\Administrator\Desktop\test_data.txt','r') as f:
                lesson_codes=(f.readlines())
        #因为readline读取的列表元素末尾有'\n' 所以利用字符串的strip（）去除
        #print(lesson_codes)
        need_codes = []
        for x in lesson_codes:
            need_codes.append(x.strip())
        print('需要的need_codes：%s' % need_codes,'长度是：%s' % len(need_codes))

        #下面循环post课程 来断言课程详情是否获取成功
        for n in need_codes:
            json_data = {"lesson_code":n,"token":self.uid_token}
            r2 = self.s.post(url,headers = self.header,json=json_data,verify=False)
            self.log.info('课程信息返回：%s' % r2.json())
            self.assertEqual('请求成功.',r2.json()['note'])

        self.log.info('------------测试结束---------------')

    def tearDown(self):
        self.s.close()
if __name__=='__main__':
    unittest.main(warnings='ignore')
