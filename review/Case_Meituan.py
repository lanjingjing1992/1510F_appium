import time
import unittest
from appium.webdriver.common.touch_action import TouchAction
from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
class Meituan(unittest.TestCase):
    def setUp(self):
        qiezi = {}
        qiezi['platformName'] = 'Android'
        qiezi['platformVersion'] = '4.4.4'
        qiezi['deviceName'] = 'MuMu'
        qiezi['appPackage'] = "com.sankuai.meituan"
        qiezi['appActivity'] = "com.sankuai.meituan.activity.Welcome"
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', qiezi)
    def testA_click(self):
        CLASSNAME=(By.CLASS_NAME,'android.view.View')
        WebDriverWait(self.driver,100,0.1).until(EC.presence_of_all_elements_located(CLASSNAME))
        list=self.driver.find_elements_by_class_name('android.view.View')
        '''通过断点（通过坐标 找下标）得知下标为4的是view 调用touchaction的tap方法，方法中参数的意义可以参照源码'''
        action=TouchAction(self.driver)
        '''方法中参数的可以参照源码'''
        action.tap(list[4],130,90).perform()
        time.sleep(10)

    def tearDown(self):
        self.driver.quit()
