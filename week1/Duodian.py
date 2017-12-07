import unittest
from week1.MyFind import Find

class Duodian(unittest.TestCase):
    def setUp(self):
        self.find=Find()
        self.find.Myinit('com.wm.dmall','com.wm.dmall.LaunchActivity')
    def testA_clickME(self):#点击我的提示登陆
        myfind=self.find
        myfind.MyXapth('//android.widget.TextView[@text=\"我的\"]').click()#点击我的跳转到登陆界面
        #点击登陆/注册按钮
        myfind.MyXapth('//android.widget.TextView[@text=\"登录/注册\"]').click()
        myfind.MyXapth('//android.widget.EditText[@resource-id=\"com.wm.dmall:id/et_phone_num\"]').send_keys('15901337131')#输入手机号
        myfind.MyXapth('//android.widget.EditText[@resource-id=\"com.wm.dmall:id/et_phone_pwd\"]').send_keys('123456')#输入密码
        myfind.MyXapth('//android.widget.TextView[@text=\"登录\"]').click()#点击登陆

    def testB_aboutDuodian(self):#关于多点的测试
        myfind=self.find

        # 先点击我的
        myfind.MyXapth('//android.widget.TextView[@text=\"我的\"]').click()
        myfind.MyXapth('//android.widget.TextView[@text=\"关于多点\"]').click()#点击关于多点
        #关于多点的页面
        str_version=myfind.MyXapth('//android.widget.TextView[@text=\"当前版本：3.8.0\"]').text
        self.assertIn('3.8.0',str_version)#验证是否包含版本号，也就是版本号是否正确

    def tearDown(self):
        for i in range(10):
            self.find.myDriver().keyevent(4)




