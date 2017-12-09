
import time
import unittest
from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
class QQ(unittest.TestCase):
    def setUp(self):
        '''连接qq'''
        qiezi = {}
        qiezi['platformName'] = 'Android'
        qiezi['platformVersion'] = '4.4.4'
        qiezi['deviceName'] = 'MuMu'
        qiezi['appPackage'] = "com.tencent.mobileqq"
        qiezi['appActivity'] = ".activity.SplashActivity"
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', qiezi)

    def testA_click(self):
        '''单元测试'''
        time.sleep(5)
        '''点击左上角的头像'''
        self.driver.find_element_by_id('com.tencent.mobileqq:id/conversation_head').click()#点击左上角的头像

        CLASS_NAME1 = (By.CLASS_NAME, 'android.widget.TextView')
        WebDriverWait(self.driver, 30, 0.1).until(EC.presence_of_all_elements_located(CLASS_NAME1))
        list = self.driver.find_elements_by_class_name('android.widget.TextView')
        list[10].click()  # 点击设置
        time.sleep(3)


        '''点击账号管理'''
        CLASS_NAME=(By.CLASS_NAME,'android.widget.RelativeLayout')
        WebDriverWait(self.driver,30,0.1).until(EC.presence_of_all_elements_located(CLASS_NAME))
        list2=self.driver.find_elements_by_class_name('android.widget.RelativeLayout')
        list2[4].click()#点击账号管理
        time.sleep(5)


        '''点击退出当前账号'''

        CLASS_NAME = (By.CLASS_NAME, 'android.widget.RelativeLayout')
        WebDriverWait(self.driver, 30, 0.1).until(EC.presence_of_all_elements_located(CLASS_NAME))
        list3 = self.driver.find_elements_by_class_name('android.widget.RelativeLayout')
        list3[13].click()  # 点击退出当前账号
        time.sleep(5)

        '''点击取消toast'''
        CLASS_NAME = (By.CLASS_NAME, 'android.widget.TextView')
        WebDriverWait(self.driver, 30, 0.1).until(EC.presence_of_all_elements_located(CLASS_NAME))
        list4 = self.driver.find_elements_by_class_name('android.widget.TextView')
        list4[2].click()  # 点击账号管理
        time.sleep(5)



    def tearDown(self):
        self.driver.quit()
