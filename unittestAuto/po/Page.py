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
import time
import os
import uiautomator2 as u2

from unittestAuto.public.FileOperate import getTest_info
from unittestAuto.public.LogUtils import Logging
from unittestAuto.public.PageMethod import getYaml, clickByXY, clickByText


class PagePo:
    def __init__(self, device, all_result_path, yaml_path):
        self.device = device
        self.all_result_path = all_result_path
        self.yaml_path = yaml_path
        self.driver = u2.connect(self.device)

    def analysis(self):
        pass

    def main(self):
        '''
        存log，其实adb抓log也没有什么实际意义，不如直接存储代码的执行日志和异常情况，把log操作放在HTMLTestReport.py里面了
        执行测试用例
        '''
        # 也可以在这里加上adb抓取log的操作，暂时省略了
        self.operate(self.driver, self.yaml_path)

    def operate(self, driver, yaml_path):
        '''
        这个yaml对应操作的流程
        @:param driver, yaml路径
        '''
        driver.app_start(getTest_info('test_package_name', 'package_name'))
        Logging.success('start app success')
        Logging.debug(yaml_path)
        # for yaml in yaml_list:
        caseYaml = getYaml(yaml_path)
        testinfo = caseYaml['testinfo']
        testcases = caseYaml['testcase']
        checks = caseYaml['check']

        for testcase in testcases:
            element_info = testcase['element_info']
            elementList = element_info.split(', ')
            # print(elementList)

            if testcase['operate_type'] == 'click':
                Logging.success(testcase['operate_type'] + testcase['info'])
                # 如果可以转换成float说明是坐标，否则就是str
                try:
                    # 可能出现异常的代码
                    elementList[0] = float(elementList[0])
                    elementList[1] = float(elementList[1])
                    clickByXY(driver, elementList)
                    time.sleep(1)
                except:
                    # 出现异常后执行的代码
                    # print('element_info内容为字符串：text='', outTime=''')
                    clickByText(driver, elementList)
                    time.sleep(1)
                else:
                    # 如果没有异常执行的代码
                    pass
                finally:
                    # 不管是否出现异常都会执行finally 具体放在那里是否可以和else一起用？
                    pass

            elif testcase['operate_type'] == 'scroll':
                Logging.success(testcase['operate_type'] + testcase['info'])
                pass

            elif testcase['operate_type'] == 'sentkey':
                Logging.success(testcase['operate_type'] + testcase['info'])
                driver(text="Settings").set_text("你好")
                pass

            else:
                Logging.warn('没有改操作请在此添加' + os.getcwd())
                # 每执行一个操作就会截图
            # ADB().screen_shot(self.all_result_path + '\img' + '\\' + testcase['info'] + '.png')
            for check in checks:
                pass
                # 可以研究下具体有什么检查方式
                # if check['operate_type'] == 'click':
                #     print(check['operate_type'] + check['info'])
                #     d(test='').click()
                # if check['operate_type'] == 'scroll':
                #     print(check['operate_type'] + check['info'])
                #     pass
                # if check['operate_type'] == 'sentkey':
                #     print(check['operate_type'] + check['info'])
                #     pass
                # else:
                #     print('没有改操作请在此添加' + os.getcwd())

        Logging.info('第n个yaml文件测试完成')


if __name__ == '__main__':
    # 返回字典
    homeyaml = getYaml('D:\pycharm\PycharmWorkSpase\\unittestAuto\yamls\Home\home01.yaml')
    print(homeyaml)
    # print(getTest_info('test_package_name', 'package_name'))
