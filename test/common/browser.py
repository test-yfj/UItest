# -*- coding: utf-8 -*-
# @Department: 测试
# @Author: 杨凤娇
# @Description: 浏览器的调用
import time
import os
from selenium import webdriver
from utils.config import REPORT_PATH


TYPES = {'firefox': webdriver.Firefox, 'chrome': webdriver.Chrome, 'ie': webdriver.Ie}


class UnSupportBrowserTypeError(Exception):
    pass


class Browser(object):

    def __init__(self, browser_type='chrome'):
        self._type = browser_type.lower()
        if self._type in TYPES:
            self.browser = TYPES[self._type]
        else:
            raise UnSupportBrowserTypeError('仅支持%s!' % ', '.join(TYPES.keys()))
        self.driver = None

    def get(self, url="", maximize_window=True, implicitly_wait=30):
        self.driver = self.browser()
        self.driver.get(url)
        if maximize_window:
            self.driver.maximize_window()
        self.driver.implicitly_wait(implicitly_wait)
        return self

    def getImage(self):
        '''
        截取图片,并保存在images文件夹
        :return: 无
        '''
        timestrmap = time.strftime('%Y%m%d_%H.%M.%S')
        imgPath = os.path.join(REPORT_PATH+'\image', '%s.png' % str(timestrmap))

        self.driver.save_screenshot(imgPath)
        print('screenshot:', timestrmap, '.png')

    # 关闭当前窗口
    def close(self):
        self.driver.close()

    # 关闭所有窗口
    def quit(self):
        self.driver.quit()
