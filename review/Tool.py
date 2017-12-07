from appium import webdriver
import unittest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as  EC
from selenium.webdriver.support.ui import WebDriverWait
class BaseTestManager:
    '''初始化方法 用来进行数据的初始化 创建类的对象的时候调用'''
    def __init__(self,activity,package):
        qiezi = {}
        qiezi['platformName'] = 'Android'
        qiezi['platformVersion'] = '4.4.4'
        qiezi['deviceName'] = 'MuMu'
        qiezi['appPackage'] = package
        qiezi['appActivity'] = activity
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', qiezi)



    '''通过id查找元素的方法  使用显示等待'''
    def FindById(self,id):
        ID = (By.ID,id)
        WebDriverWait(self.driver, 30, 0.1).until(EC.presence_of_all_elements_located(ID))
        return self.driver.find_element_by_id(id)

    '''通过xpath查找元素'''
    def FindByXpath(self,xpath):

        PATH=(By.XPATH,xpath)
        WebDriverWait(self.driver,30,0.1).until(EC.presence_of_all_elements_located(PATH))
        return self.driver.find_element_by_xpath(xpath)

    def Mydriver(self):
        return self.driver













