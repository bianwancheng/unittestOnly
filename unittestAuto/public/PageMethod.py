# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     PageMethod
   Description :
   Author :       bianwancheng
   date：          2019/3/18
-------------------------------------------------
   Change Activity:
                   2019/3/18:
-------------------------------------------------
__author__ = 'wancheng.b'
"""

import yaml
from unittestAuto.public import LogUtils
from unittestAuto.public.FileOperate import FileOperate
from unittestAuto.public.LogUtils import Logging



'''
解析yaml，return：dict
'''


@LogUtils.l()
def getYaml(path):
    with open(path, 'r', encoding='utf-8')as f:
        deviceYaml = yaml.load(f)
    return deviceYaml


'''
给页面操作加装饰器（点击，滑动等等）
带参数的装饰器装饰带参数的函数
path：截屏存储地址
'''
def operateDecorate():

    def Decorate(func):
        """
            打印log
            文件名+函数名,return
            :return:
            """
        def operate(arg, *args):
            func(arg, *args)
            path = FileOperate().path + '\img' + '\\' + list(*args)[0] +'.png'
            arg.screenshot(path)
        #     截图
        return operate
    return Decorate





'''
@ description 通过X, Y 坐标滑动

'''

@operateDecorate()
def scrollByXY(driver, elementList):
    pass

'''
@ description 通过X, Y 坐标点击
@:parameter driver, elementinfo_List

'''

@operateDecorate()
def clickByXY(driver, elementList):
    try:
        driver.click(elementList[0], elementList[1])
        Logging.success('driver click' + elementList[0] + 'success by XY')
    except Exception as e:
        raise e


'''
@description 通过text点击
@:parameter driver, elementinfo_List
'''

@operateDecorate()
def clickByText(driver, elementList):
    try:
        driver(text=elementList[0]).click(timeout=int(elementList[1]))
        Logging.success('driver click' + elementList[0] + 'success by Text')
    except Exception as e:
        raise e

if __name__ == '__main__':
    '''d = u2.connect('55cac15d')
    d.app_start('com.test.ui.activities.nihao')
    list = ['测试工具', 10]
    clickByText(d, list)
    print('装饰器没有问题')
    '''
    pass