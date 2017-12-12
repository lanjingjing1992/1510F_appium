import unittest
from ChromeTest.Businness import businessAction
from time import sleep


class Chrometest(unittest.TestCase):
    def setUp(self):
        self.server=businessAction('com.google.android.apps.chrome.Main', 'com.android.chrome')


    def testSearch(self):
        '''输入百度网址 并且在百度搜索栏输入appium 点击搜索'''

        self.server.inpustURL()
        self.server.inputAppium()
        sleep(100)


    def tearDown(self):
        self.server.BackToGoole()


