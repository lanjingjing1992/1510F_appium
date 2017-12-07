import unittest
from appium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class Meituan(unittest.TestCase):
    def setUp(self):
        #重写setup方法 初始化的内容
        desired_capabilities = {}  # 字典 用来存放的手机信息  app信息
        desired_capabilities['platformName'] = 'Android'  # 安卓平台
        desired_capabilities['unicodeKeyboard']=True
        desired_capabilities['resetKeyboard']=True
        desired_capabilities['platformVersion'] = '4.4.4'  # 安卓手机设备版本号
        desired_capabilities['deviceName'] = 'MuMu'  # 设备名字  通过adb devices获取
        desired_capabilities['appPackage'] = 'com.qiezzi.eggplant'  # apk的包名
        desired_capabilities['appActivity'] = 'com.qiezzi.eggplant.base.WelcomeActivity'  # 启动activity名字
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_capabilities)


    def testA(self):
        d=self.driver
        d.implicitly_wait(30)
        w=d.get_window_size()['width']
        h=d.get_window_size()['height']
        for i in range(10):
            d.swipe(w*0.5,h*0.9,w*0.5,h*0.1)

    def testB(self):
        d=self.driver
        d.implicitly_wait(30)
        str_city=d.find_element_by_id('com.sankuai.meituan:id/city_button').text
        print(str_city)
        self.assertEqual('北京',str_city)
    def testC(self):#点击美食
        d = self.driver
        #通过xpath获取元素 android.widget.TextView为class @text代表通过文本方式，
        xpath='//android.widget.EditText[@resource-id=\"com.qiezzi.eggplant:id/edt_frist_login_accout\"]'
        Xpath=(By.XPATH,xpath)
        WebDriverWait(d,30,0.5).until(EC.presence_of_all_elements_located(Xpath))
        foods = d.find_element_by_xpath(xpath)
        foods.send_keys(u'兰京京')
        pw=d.find_element_by_xpath('//android.widget.EditText[@resource-id=\"com.qiezzi.eggplant:id/edt_frist_login_password\"]')
        pw.send_keys(u'娃娃')

        sleep(10)

    # def testD(self):#点击输入框输入，测试能否搜索
    #     d = self.driver
    #     d.implicitly_wait(30)
    #     # 通过xpath获取元素 android.widget.TextView为class @text代表通过文本方式，
    #
    #     food = d.find_element_by_xpath('//android.view.View[contains(@index,1)]')
    #     food.click()
    #     d=self.driver
    #     d.implicitly_wait(30)
    #     food = d.find_element_by_id('com.sankuai.meituan:id/tv_search_text')
    #     food.click()
    #     d.find_element_by_id('com.sankuai.meituan:id/search_edit').send_keys('米线')
    #     d.find_element_by_id('com.sankuai.meituan:id/search').click()



    def tearDown(self):

            for i in range(10):  # 按back键退出acticity
                print('第%s点击back键' % i)
                self.driver.keyevent(4)
