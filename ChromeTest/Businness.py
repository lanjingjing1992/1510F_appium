from ChromeTest.UI import loginUIAction
class businessAction:
    '''初始化方法'''
    def __init__(self,activity,package):
        self.action=loginUIAction(activity,package)


    def inpustURL(self):
        '''输入网址'''
        '''点击网址框'''
        self.action.Click('com.android.chrome:id/ntp_content')
        self.action.InputUrl('com.android.chrome:id/url_bar','http://www.baidu.com')
    def inputAppium(self):
        '''在百度的搜索栏输入appium 并且点击搜索'''
        self.action.InputToBaidu('index-kw','appium')
        self.action.Click('index-bn')
    def BackToGoole(self):
        self.action.tearDown()


