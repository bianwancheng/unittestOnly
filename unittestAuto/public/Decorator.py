import time

from functools import wraps
import os
import uiautomator2 as u2

from unittestAuto.RunAllcase import getDevices
from unittestAuto.public.FileOperate import FileOperate
from unittestAuto.public.LogUtils import Logging

'''
为每个test_ 设置一个装饰器
'''

flag = 'IMAGE:'
log = Logging()


def _screenshot(name):
    date_time = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
    screenshot = name + '-' + date_time + '.PNG'
    # path = ReportPath().get_path() + '/' + screenshot
    path = os.path.join(FileOperate().path + '/img', screenshot)
    devive = getDevices()[0]   #这里先这么写吧以后会整理
    driver = u2.connect(devive)
    driver.screenshot(path)
    return screenshot


def teststep(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            Logging.info('--> %s' % func.__qualname__)
            ret = func(*args, **kwargs)
            return ret
        except AssertionError as e:
            Logging.error('AssertionError, %s'+ str(e))
            Logging.error('\t<-- %s, %s, %s' + func.__qualname__ + 'AssertionError'+ 'Error')

            if flag in str(e):
                raise AssertionError(e)
            else:
                raise AssertionError(flag + _screenshot(func.__qualname__))
        except Exception as e:
            Logging.error('Exception, %s'+ str(e))
            Logging.error('\t<-- %s, %s, %s'+ func.__qualname__+ 'Exception'+ 'Error')

            if flag in str(e):
                raise Exception(e)
            else:
                raise Exception(flag + _screenshot(func.__qualname__))

    return wrapper


def teststeps(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            Logging.info('--> %s' % func.__qualname__)
            ret = func(*args, **kwargs)
            Logging.debug('  <-- %s, %s', func.__qualname__, 'Success')
            return ret
        except AssertionError as e:
            Logging.error('AssertionError, %s', e)
            Logging.error('  <-- %s, %s, %s', func.__qualname__, 'AssertionError', 'Error')

            if flag in str(e):
                raise AssertionError(e)
            else:
                raise AssertionError(flag + _screenshot(func.__qualname__))
        except Exception as e:
            Logging.error('Exception, %s', e)
            Logging.error('  <-- %s, %s, %s', func.__qualname__, 'Exception', 'Error')

            if flag in str(e):
                raise Exception(e)
            else:
                raise Exception(flag + _screenshot(func.__qualname__))

    return wrapper


def _wrapper(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            Logging.debug('--> %s', func.__qualname__)
            ret = func(*args, **kwargs)
            Logging.debug('<-- %s, %s\n', func.__qualname__, 'Success')
            return ret
        except AssertionError as e:
            Logging.error('AssertionError, %s', e)
            Logging.error('<-- %s, %s, %s\n', func.__qualname__, 'AssertionError', 'Fail')

            if flag in str(e):
                raise AssertionError(e)
            else:
                raise AssertionError(flag + _screenshot(func.__qualname__))
        except Exception as e:
            Logging.error('Exception, %s', e)
            Logging.error('<-- %s, %s, %s\n', func.__qualname__, 'Exception', 'Error')

            if flag in str(e):
                raise Exception(e)
            else:
                raise Exception(flag + _screenshot(func.__qualname__))

    return wrapper


def testcase(func):
    return _wrapper(func)


def setup(func):
    return _wrapper(func)


def teardown(func):
    return _wrapper(func)


def setupclass(func):
    return _wrapper(func)


def teardownclass(func):
    return _wrapper(func)
