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
    def test_scbQR(self):
        device = "55cac15d"
        test_ScbQR_path = getOneCaseYamlPath('ServiceTester', 'ScbQR.yaml')
        print('test_ScbQR_path:' + test_ScbQR_path)
        page = PagePo(device, FileOperate().path, test_ScbQR_path)
        page.main()
        # 手动截屏
        # u2.connect(device).screenshot()

    @classmethod
    def tearDownClass(cls):
        Process().testEnd()


if __name__ == '__main__':
    unittest.main()
