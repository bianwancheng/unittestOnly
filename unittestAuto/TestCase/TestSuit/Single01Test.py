#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2019/3/12 14:06
# @Author  :  wancheng.b
# @Site     : 
# @File     : Single01Test.py
# @Software  : PyCharm
import os
import time
import unittest
import warnings

from unittestAuto.lib.adbUtils import ADB
from unittestAuto.public.FileOperate import getTest_info
from unittestAuto.public.LogUtils import Logging
import uiautomator2 as u2


class SingleTest(unittest.TestCase):
    devices = '12132'

    @classmethod
    def setUpClass(cls):
        '''
       安装atx和apk

       :return:
        '''
        warnings.simplefilter('ignore', ResourceWarning)
        package_name = getTest_info('test_package_name', 'package_name')
        package_atx = getTest_info('test_package_name', 'package_atx')
        if not ADB().is_install(package_name):
            ADB().install_app(package_name)
            Logging.info('install' + package_name + 'success')

        if not ADB().is_install(package_atx):
            os.system('python -m uiautomator2 init')
            Logging.info('install' + package_atx + 'success')
        else:
            pass

    def setUp(self):
        print("每个testCase之前执行setUp")

    def tearDown(self):
        print("每个tesTest执行完执行")

    @classmethod
    def tearDownClass(cls):
        # 退出app，返回apk主页面
        ADB().quit_app(getTest_info('test_package_name', 'package_name'))
        ADB().start_activity('com.android.launcher3/.Launcher')

    def test_first(self):
        self.assertEqual(8 / 2, 3)
        print(SingleTest().devices)
        print("test_first")

    def test_second(self):
        self.assertEqual(1 + 2, 3)
        print("test_second")
        Logging.info('test_second')

    def test_01_frst(self):
        device = "55cac15d"
        d = u2.connect(device)
        d.app_start('com.test.ui.activities.nihao')
        d(text='测试工具').click(timeout=10)
        time.sleep(1)
        try:
            d(text='测试').click(timeout=10)
        except:
            print('失败截图')
            d.screenshot()

    @unittest.skip
    def test_skip(self):
        print("skip")

    @unittest.skipIf(2 + 2 == 4, "成立")
    def test_skipIf(self):
        print("skipIf")


if __name__ == '__main__':
    unittest.main()
