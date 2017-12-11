import unittest
from ChromeTest.Businness import businessAction



class Chrometest(unittest.TestCase):
    def setUp(self):
        self.server=businessAction('com.google.android.apps.chrome.Main', 'com.android.chrome')
        self.server.inputURL()

    def testSearch(self):

        print('hello')
        self.server.Search()

    def tearDown(self):
        self.server.BackToGoole()


