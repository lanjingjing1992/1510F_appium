from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium import webdriver
from time import sleep


class Find:
    def Myinit(self,appPackage,appActivity):
        qiezi = {}#参数
        qiezi['deviceName'] = 'MuMu'#手机型号
        qiezi['platformName'] = 'Android'
        qiezi['platformVersion'] = '4.4.4'
        qiezi['appPackage'] = appPackage
        qiezi['appActivity'] = appActivity
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', qiezi)#连接到appium服务器

        # 通过ID查找元素
    def MyfindId(self,id):

        ID=(By.ID,id)#通过id方式查找
        WebDriverWait(self.driver,30,0.5).until(EC.presence_of_all_elements_located(ID))#使用显示等待 每隔0。5秒检查一次 如果30秒内找到元素就执行下面代码，如果没有就报超时错误

        return self.driver.find_element_by_id(id)#返回该元素



       # 通过姓名查找元素
    def MyfindName(self):
        pass


      #通过xpath查找元素
    def MyXapth(self,xpath):
        XPATH = (By.XPATH, xpath)  # 通过id方式查找
        WebDriverWait(self.driver, 30, 0.1).until(
            EC.presence_of_all_elements_located(XPATH))  # 使用显示等待 每隔0。5秒检查一次 如果30秒内找到元素就执行下面代码，如果没有就报超时错误

        return self.driver.find_element_by_xpath(xpath)  # 返回该元素

    # 通过文本获取
    def MyPartialLink(self,str):
        PARTIAL_LINK_TEXT = (By.PARTIAL_LINK_TEXT, str)  # 通过id方式查找
        WebDriverWait(self.driver, 30, 0.1).until(
            EC.presence_of_all_elements_located(PARTIAL_LINK_TEXT))  # 使用显示等待 每隔0。5秒检查一次 如果30秒内找到元素就执行下面代码，如果没有就报超时错误

        return self.driver.find_element_by_partial_link_text(str)  # 返回该元素
    #向左滑动
    def leftScroll(self):
        width = self.driver.get_window_size()['width']
        height = self.driver.get_window_size()['height']
        for i in range(4):
            sleep(3)  # 等待
            self.driver.swipe(width * 0.9, height * 0.5, width * 0.1, height * 0.5)  # 起始的x.y 结束的x y 滑动
    def topScroll(self):
        pass

    def myDriver(self):
        return self.driver

