from review.UI import loginUIAction
class businessAction:
    '''初始化方法'''
    def __init__(self,activity,package):
        self.action=loginUIAction(activity,package)
    def Login(self):
        '''输入用户名'''
        self.action.enterName('//android.widget.EditText[@text=\"输入用户名/手机号\"]','13718400263')
        '''输入密码'''
        self.action.enterPw('android.widget.EditText','123456123456')

        '''点击登陆'''
        self.action.clickBtn('//android.widget.TextView[contains(@text,\'登录\')]','xpath')

    def ClickMe(self):
        '''点击我的'''
        self.action.clickBtn('//android.widget.TextView[@text=\"我的\"]','xpath')
    def returnclickMe(self):
        return self.action.baseFind.FindByXpath('//android.widget.TextView[@text=\"我的\"]')
    def ClickLoginbtn(self):
        '''点击登陆按钮'''
        self.action.clickBtn('//android.widget.TextView[@text=\"登录/注册\"]','xpath')
    def ClickCancel(self):
        '''点击取消按钮'''
        self.action.clickBtn('com.syoogame.yangba:id/cancel','id')

    def Clickattention(self):
        '''点击关注按钮'''
        self.action.clickBtn('//android.widget.TextView[@text=\"关注\"]','xpath')

    def ClickToTeardown(self):
        '''退出清除'''
        self.action.tearDown()




    def ClickSetting(self):
        '''点击搜索'''
        self.action.clickBtn('//android.widget.TextView[@text=\"设置\"]','xpath')

    def ClickAboutZhibo(self):
        '''点击关于'''
        self.action.clickBtn('//android.widget.TextView[@text=\"关于\"]','xpath')
    def VersionZhibo(self):
        '''直播的版本号'''
        return  self.action.selectVersion('//android.widget.TextView[@text=\"关于\"]')
    def clickLoginBtn(self):
        '''点击登陆的按钮'''
        self.action.clickBtn('//android.widget.TextView[@text=\"登录/注册\"]','xpath')