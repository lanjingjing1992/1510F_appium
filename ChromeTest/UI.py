from ChromeTest.Tool import BaseTestManager
class loginUIAction:

    '''这是用来做一步步的动作 操作'''
    def __init__(self,activity,package):
        self.baseFind=BaseTestManager(activity,package)
    def SearchBawei(self,id,content):
        '''搜索八维'''
        self.baseFind.FindById(id).send_keys(content)
    def ClickSearchBtn(self,id):

        self.baseFind.FindById(id).click()


    def tearDown(self):
        for i in range(10):
            self.baseFind.Mydriver().keyevent(4)

    def inputURL(self,id,url):
        self.baseFind.FindById(id).send_keys(url)#输入百度网址
        self.baseFind.Mydriver().keyevent(66)#输入回车键





