import unittest
from appium import webdriver
from time import sleep
from HTMLTestRunner.HTMLTestRunner import HTMLTestRunner
from week1.MyFind import Find
#显示等待
class Qiezi(unittest.TestCase):
    def setUp(self):#初始化
        self.myfind = Find()#创建工具类对象
        self.myfind.Myinit('com.qiezzi.eggplant','com.qiezzi.eggplant.base.WelcomeActivity')# 创建对象
    def testA_Scroll(self):#滑动
        d=self.myfind
        
        d.leftScroll()#滑动

        #点击立即体验
        d.MyfindId('com.qiezzi.eggplant:id/btn_feel_right_now').click()



    def testB_Login(self):
        d=self.myfind
        d.MyfindId('com.qiezzi.eggplant:id/edt_frist_login_accout').send_keys('15901337131')#输入手机号
        d.MyfindId('com.qiezzi.eggplant:id/edt_frist_login_password').send_keys('442131ljj')#输入密码

        d.MyfindId('com.qiezzi.eggplant:id/btn_frist_login_immediately').click()#点击登陆



    def testC_Clickme(self):
        sleep(5)
        d=self.myfind

        d.MyfindId('com.qiezzi.eggplant:id/btn_main_my').click()#点击我的
        d.MyfindId('com.qiezzi.eggplant:id/iv_my_set').click()#点击设置
        #清除缓存的文本

        str_clear=d.MyfindId('com.qiezzi.eggplant:id/cache_filder_size').text


        self.assertEqual('0K',str_clear)#断言验证是否一致

    def tearDown(self):
        pass


if __name__ == '__main__':
    suite=unittest.TestSuite()#新建测试集合对象
    suite.addTest(Qiezi('testA_Scroll'))#添加测试用例到测试集合
    suite.addTest(Qiezi('testB_Login'))
    suite.addTest(Qiezi('testC_Clickme'))

    runner=HTMLTestRunner(stream=open('result.html','w+'),title='兰京京',description='this is mine')#创建测试报告
    runner.run(suite)


