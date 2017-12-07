import time
import unittest
from review.Tool import BaseTestManager
from review.Businness import businessAction
from HTMLTestRunner.HTMLTestRunner import HTMLTestRunner



class Zhibo(unittest.TestCase):
    def  setUp(self):
        self.server=businessAction('com.syoogame.yangba.MainActivity', 'com.syoogame.yangba')
    def testA_Cancel(self):
        '''点击取消更新按钮'''
        self.server.ClickCancel()
        '''查看我的按钮是否存在'''
    def testB_clickMe(self):
        '''点击我的'''
        '''点击取消更新按钮'''
        self.server.ClickCancel()
        '''点击我的'''
        self.server.ClickMe()
    def testC_attention(self):
        '''点击关注，出现登陆按钮'''
        '''点击取消更新按钮'''
        self.server.ClickCancel()
        '''点击关注，出现登陆按钮'''
        self.server.Clickattention()
        '''判断登陆按钮是否存在'''
        element=self.server.action.baseFind.FindByXpath('//android.widget.TextView[@text=\"登录\"]')
        self.assertIsNotNone(element)
    def testD_Search(self):
        '''点击搜索框，检查是否能正常搜索'''
        '''点击取消更新按钮'''
        self.server.ClickCancel()
        '''点击搜索框元素'''
        self.server.ClickSearch()
        time.sleep(5)
    def testE_setting(self):
        '''检查设置模块'''
        '''点击取消更新按钮'''
        self.server.ClickCancel()
        '''点击我的'''
        self.server.ClickMe()
        '''点击设置'''

        self.server.ClickSetting()
        time.sleep(5)
        '''点击直播的关于'''
        self.server.ClickAboutZhibo()
        '''返会版本号'''
        str_version=self.server.VersionZhibo()
        '''断言版本号是否正确'''
        self.assertEqual('1.0',str_version)



    def tearDown(self):
        self.server.ClickToTeardown()



if __name__ == '__main__':
    suite = unittest.TestSuite()
    # suite.addTest(Zhibo('testA_Cancel'))
    # suite.addTest(Zhibo('testB_clickMe'))
    # suite.addTest(Zhibo('testC_attention'))
    # suite.addTest(Zhibo('testD_Search'))
    suite.addTest(Zhibo('testE_setting'))
    file = open('re.html', 'w+')
    runner = HTMLTestRunner(stream=file, title='兰京京', description='这是我的测试报告1510F')
    runner.run(suite)

