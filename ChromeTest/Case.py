
import unittest
from ChromeTest.Find import MyFind
from time import sleep
class ChromeTest(unittest.TestCase):

    def setUp(self):
        self.find=MyFind()
    # def testClick(self):
    #     '''测试用例1  打开chrome首页 输入网址百度'''
    #     d=self.driver
    #     self.find.FindId('com.android.chrome:id/search_box_text').click()
    #     self.find.FindId('com.android.chrome:id/url_bar').send_keys('http://www.baidu.com')
    #     self.find.FindId('index-kw').send_keys('appium')
    #     self.find.FindId('index-bn').click()
    def testweb(self):
        print('hello')
        '''切入到webview'''
        sleep(3)
        d=self.find.MyDriver()#获取驱动
        '''所有的上下文对象'''
        list=d.contexts
        print(list)
        sleep(3)
        for con in list:
            # 如果以
            # webview开头
            if con.lower().startswith('webview'):
                #切入到这个context
                d._switch_to.context(con)
                print('success')
        '''获取当前的上下文对象'''
        print(d.context)
        sleep(3)
        self.find.FindXpath('//*[@id="classListLine_1"]/p').click()
        sleep(3)
        self.find.FindXpath('//*[@id="classListLine_3"]/p').click()
        sleep(10)



    def tearDown(self):
        pass
        # self.driver.quit()