#coding=utf-8

from config import globalparam
import time
from public.common.log import Log
from selenium.common.exceptions import TimeoutException
from public.common.pyselenium import PySelenium

logger = Log()
success = "SUCCESS   "
fail = "FAIL   "


# 截图放到report下的img目录下
def get_img(filename):
    path = globalparam.img_path
    PySelenium.take_screenshot(path + '/' + filename)

def assertExists(self,css):
    """验证元素是否存在"""
    t1 = time.time()
    try:
        PySelenium.element_wait(self,css)
        PySelenium.my_print("{0} Element: <{1}> is exist, Spend {2} seconds".format(success, css, time.time() - t1))
        return True
    except TimeoutException:
        PySelenium.my_print("{0} Element: <{1}> is not exist, Spend {2} seconds".format(fail, css, time.time() - t1))
        return False