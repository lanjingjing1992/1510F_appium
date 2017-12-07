from review.Tool import BaseTestManager
class loginUIAction:

    '''这是用来做一步步的动作 操作'''
    def __init__(self,activity,package):
        self.baseFind=BaseTestManager(activity,package)
    def enterName(self,locate,name):
        '''输入用户名'''
        self.baseFind.FindById(locate).send_keys(name)
    def enterPw(self,locate,pw):
        self.baseFind.FindById(locate).send_keys(pw)

    def clickBtn(self,locate,kind):
        if kind=='xpath':
            self.baseFind.FindByXpath(locate).click()
        elif kind=='id':
            self.baseFind.FindById(locate).click()
    '''后续的操作步骤自己写'''



    def tearDown(self):
        self.baseFind.Mydriver().quit()



    def selectVersion(self,xpath):
        str_version=self.baseFind.FindByXpath(xpath).text
        return str_version




