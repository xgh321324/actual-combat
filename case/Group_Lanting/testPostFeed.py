#coding:utf-8
import requests,unittest
from common.login_lanting import auto_login_by_UID
from common.logger import Log
import urllib3
urllib3.disable_warnings()

class Feed(unittest.TestCase):
    def setUp(self):
        self.s = requests.session()
        self.auto_login_token = auto_login_by_UID()  #auto_login_by_UID返回的token
        self.header = {'User-Agent': 'PelvicFloorPersonal/4.1.1 (iPad; iOS 10.1.1; Scale/2.00)',
                       'Accept-Encoding': 'gzip, deflate',
                       'Accept-Language': 'zh-Hans-CN;q=1',
                       'Content-Type': 'application/json',
                       'requestApp': '2',
                       'requestclient': '2',
                       'versionForApp': '4.1.1',
                       'Authorization': 'Basic YXBpTGFudGluZ0BtZWRsYW5kZXIuY29tOkFwaVRobWxkTWxkQDIwMTM=',
                       'Connection': 'keep-alive'
                       }
        self.log = Log()

    def test_post_feed(self):
        u'测试发布文字-不发布到圈子'
        self.log.info('测试发布文字接口-不发布到圈子')
        url = 'http://api.sns.sunnycare.cc/v1/feed/add'
        json_data = {"token":self.auto_login_token,
                     "text":"不知道自己的心"
                     }
        r = self.s.post(url,headers = self.header,json=json_data)
        self.log.info('返回的内容是是：%s' % r.json())
        self.assertEqual(200,r.json()['code'])
        self.assertEqual('动态发布成功.',r.json()['note'])
        self.log.info('测试发布文字接口-不发布到圈子情况测试结束\n')

    def test_post_feed2(self):
        u'测试发布文字到圈子-参数正常'
        self.log.info('测试发布文字到圈子-参数正常')
        url = 'http://api.sns.sunnycare.cc/v1/feed/add'
        json_data = {"token":self.auto_login_token,
                     "text":"不知道自己的心",
                     'groups':['G00009']
                     }
        r = self.s.post(url,headers = self.header,json=json_data)
        self.log.info('返回的内容是是：%s' % r.json())
        self.assertEqual(200,r.json()['code'])
        self.assertEqual('动态发布成功.',r.json()['note'])
        self.log.info('测试发布文字到圈子-参数正常情况测试结束\n')

    def test_post_feed3(self):
        u'测试发布文字到大于3个圈子-参数正常'
        self.log.info('测试发布文字到大于3个圈子-参数正常')
        url = 'http://api.sns.sunnycare.cc/v1/feed/add'
        json_data = {"token":self.auto_login_token,
                     "text":"不知道自己的心",
                     'groups':['G00009','G00008','G00007','G00006']
                     }
        r = self.s.post(url,headers = self.header,json=json_data)
        self.log.info('返回的内容是是：%s' % r.json())
        self.assertEqual('最多只能分享到 3 个圈子.',r.json()['note'])
        self.log.info('测试发布文字到大于3个圈子-参数正常情况测试结束\n')

    def test_post_picture(self):
        u'发布图片接口到圈子'
        self.log.info('测试发布图片接口到圈子')
        url = 'http://api.sns.sunnycare.cc/v1/feed/add'
        json_data = {
            "pic":[
                {
                    "path":"test\/sns\/2018\/6\/5\/61676081536705472720180605155604.png",
                    "width":828,
                    "height":1107
                }
            ],
            "groups":["G00009"],
            "token":self.auto_login_token,
            "text":"南京东路"
        }
        r = self.s.post(url,headers = self.header,json=json_data)
        self.log.info('返回的内容是：%s' % r.json())
        self.assertEqual(200,r.json()['code'])
        self.assertEqual('动态发布成功.',r.json()['note'])
        self.log.info('测试发布图片接口到圈子结束！\n')

    def test_post_picture2(self):
        u'发布图片接口到大于3个圈子'
        self.log.info('测试发布图片接口到大于3个圈子')
        url = 'http://api.sns.sunnycare.cc/v1/feed/add'
        json_data = {
            "pic":[
                {
                    "path":"test\/sns\/2018\/6\/5\/61676081536705472720180605155604.png",
                    "width":828,
                    "height":1107
                }
            ],
            "groups":['G00009','G00008','G00007','G00006'],
            "token":self.auto_login_token,
            "text":"南京东路"
        }
        r = self.s.post(url,headers = self.header,json=json_data)
        self.log.info('返回的内容是：%s' % r.json())
        self.assertEqual('最多只能分享到 3 个圈子.',r.json()['note'])
        self.log.info('测试发布图片接口到大于3个圈子结束！\n')

    def test_post_artical(self):
        u'测试发布内容-introduction摘要为空'
        self.log.info('测试发布内容接口-introduction摘要为空')
        url = 'http://api.sns.sunnycare.cc/v1/post/add'
        json_data = {
                    "token": self.auto_login_token,
                    "title": "标题ssss1",
                    "cover": 'test\/sns\/2018\/6\/5\/61676081536705472720180605155604.png',
                    #"introduction": "简介",
                    "content": [
                        {
                            "sort":"0",
                            "type":"0",
                            "value": "文本内容001"
                         },
                        {
                            "sort":"1",
                            "type":"1",
                            "value": "sns/2018/05/15/013.jpg",
                             "width": "640",
                             "height": "480",
                             "remark": "注释"
                         },
                        {
                            "sort":"2",
                             "type":"2",
                             "value": "dcc885ea85824089ba8129761f3925fe",
                             "cover": "sns/2018/05/15/013.jpg",
                             "remark": "注释", "width": "1024", "height": "764", "size": "1024", "second": "30"
                         }
                    ],
                    "groups": ["G00001", "G00002", "G00003"]
                }
        #for i in range(1,100):
        r = self.s.post(url,headers = self.header,json=json_data)
        self.log.info('返回的内容是是：%s' % r.json())
        self.log.info('测试发布内容接口-introduction摘要为空情况测试结束\n')

    def tearDown(self):
        self.s.close()


if __name__=='__main__':
    unittest.main()
