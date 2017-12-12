from ChromeTest.Tool import BaseTestManager
class loginUIAction:

    '''这是用来做一步步的动作 操作'''
    def __init__(self,activity,package):
        self.baseFind=BaseTestManager(activity,package)

    def Click(self,id):
        self.baseFind.FindById(id).click()#输入网址

    def InputUrl(self,id,url):
        self.baseFind.FindById(id).send_keys(url)
        self.baseFind.Mydriver().keyevent(66)#点击确定

    def InputToBaidu(self,id,content):
        '''在百度搜索栏输入apppium'''
        self.baseFind.FindById(id).send_keys(content)




    def tearDown(self):
        for i in range(10):
            self.baseFind.Mydriver().keyevent(4)#返回









