# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     RunOneCase.py
   Description :
   Author :       bianwancheng
   date：          2019/3/18
-------------------------------------------------
   Change Activity:
                   2019/3/18:
-------------------------------------------------
__author__ = 'wancheng.b'
"""
import os
import subprocess
import sys
import unittest
from unittestAuto.public import HTMLTestRunner
from unittestAuto.public import HTMLTestReport
from unittestAuto.public.LogUtils import Logging
from unittestAuto.public import LogUtils as U
from unittestAuto.public.FileOperate import getTest_info, existCase, FileOperate


@U.l()
def getDevices():
    '''
    换行分割截取掉头和尾，然后用\T（Tab）截取
    :return: devices_list
    '''
    devices = []
    devicesName = subprocess.getoutput('adb devices')
    devicesName = devicesName.split("\n")[1: -1]
    for deviceName in devicesName:
        deviceName = deviceName.split('\tdevice')
        devices.append(deviceName[0])
    if len(devices) > 0:
        return devices
    else:
        Logging.warn('设备未连接')


def run():
    '''discover = unittest.defaultTestLoader.discover('D:\pycharm\PycharmWorkSpase\\unittestOnly\\unittestAuto\po', pattern="Process.py")
    # print(discover)
    # discover相当于在指定的case所在的路径里寻找所有名称模式匹配pattern的文件并加载其内容，相当于suite的集合
    runner = unittest.TextTestRunner(verbosity=2)  # verbosity控制输出的执行结果的详细程度，可为0，1，2，其中0最简单，1是默认值，2最详细
    runner.run(discover)
    discover()方法时递归整个包下的文件，注意是Package不是Directory

    '''

    process_path = getTest_info('test_case', 'caseYaml')
    discover = unittest.defaultTestLoader.discover(process_path,
                                                   pattern="*test.py")
    print(discover)
    html_path = FileOperate().path + '\html' + '\\result.html'
    fp = open(html_path, "wb")
    runner = HTMLTestReport.HTMLTestRunner(stream=fp,
                                           title=u'自动化测试报告,测试结果如下：',
                                           description=u'用例执行情况：')
    # runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='da', description='df')
    runner.run(discover)
    fp.close()


if __name__ == '__main__':
    if len(existCase(getTest_info('test_case', 'caseYaml'))) > 0:
        run()

    else:
        Logging.error("测试案例不存在")
    pass
