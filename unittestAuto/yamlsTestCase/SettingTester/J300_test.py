import unittest
import uiautomator2 as u2
from unittestAuto.po.Page import PagePo
from unittestAuto.po.Process import Process
from unittestAuto.public.Decorator import teststep
from unittestAuto.public.FileOperate import getOneCaseYamlPath, FileOperate


class MyTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        Process().testInit()

    @teststep
    def test_J300(self):
        device = "55cac15d"
        test_J300_path = getOneCaseYamlPath('SettingTester', 'J300.yaml')
        print('test_J300_path:' + test_J300_path)
        page = PagePo(device, FileOperate().path, test_J300_path)
        page.main()
        # u2.connect(device).screenshot()

    @classmethod
    def tearDownClass(cls):
        Process().testEnd()


if __name__ == '__main__':
    unittest.main()
