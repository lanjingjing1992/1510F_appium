from ChromeTest.UI import loginUIAction
class businessAction:
    '''初始化方法'''
    def __init__(self,activity,package):
        self.action=loginUIAction(activity,package)

    def Search(self):
        '''通过百度搜索框搜索  八维'''
        self.action.SearchBawei('index-kw','appium')
        self.action.ClickSearchBtn('index-bn')
    def BackToGoole(self):
        self.action.tearDown()

    def inputURL(self):
        self.action.ClickSearchBtn('com.android.chrome:id/search_box_text')

        self.action.inputURL('com.android.chrome:id/url_bar','http://www.baidu.com')