from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from appium import webdriver

class MyFind:
    def __init__(self):
        '''初始化 连接手机到appium'''

        self.chrome = {}
        self.chrome['platformName'] = 'Android'
        self.chrome['platformVersion'] = '6.0.1'
        self.chrome['deviceName'] = '32d0d84a'
        self.chrome['appPackage'] = 'cn.com.gsh.guoshihui'
        self.chrome['appActivity'] = 'cn.com.gsh.guoshihui.activity.SlideActivity'
        # self.chrome['appPackage'] = 'com.android.chrome'
        # self.chrome['appActivity'] = 'com.google.android.apps.chrome.Main'
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', self.chrome)
        print('连接成功')

    def FindId(self,id):
        ID = (By.ID, id)
        WebDriverWait(self.driver, 30, 0.1).until(EC.presence_of_all_elements_located(ID))
        return self.driver.find_element_by_id(id)


    def FindXpath(self,xpath):
        XPATH=(By.XPATH,xpath)
        WebDriverWait(self.driver,30,0.1).until(EC.presence_of_all_elements_located(XPATH))
        return  self.driver.find_element_by_xpath(xpath)

    def getAll(self,tag):
        TEG=(By.TAG_NAME,tag)
        WebDriverWait(self.driver,30,0.1).until(EC.presence_of_all_elements_located(TEG))
        return self.driver.find_elements_by_tag_name(tag)
    def MyDriver(self):
        return self.driver

