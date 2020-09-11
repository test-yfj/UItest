# -*- coding: utf-8 -*-
# @Department: 测试
# @Author: 杨凤娇
# @Description: 页面封装类
from .browser import Browser
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Page(Browser):
    def __init__(self, page=None, browser_type='chrome'):
        if page:
            self.driver = page.driver
        else:
            super(Page, self).__init__(browser_type=browser_type)

    def get_driver(self):
        return self.driver

    def find_element(self, *loc):
        return self.driver.find_element(*loc)

    def find_elements(self, *loc):
        return self.driver.find_elements(*loc)

    def frame(self, frame_id):
        return self.driver.switch_to.frame(frame_id)

    def frame_back(self):
        return self.driver.switch_to.parent_frame()

    def frame_out(self):
        return self.driver.switch_to.default_content()

    def script(self, src):
        return self.driver.execute_script(src)

    def accept(self):
        return self.driver.switch_to.alert.accept()

    # 滑动滚动条
    def execute_script(self):
        return self.driver.execute_script("window.scrollBy(0,1000)")

    def refresh(self):
        return self.driver.refresh()

    # def back(self):
    #     self.driver.switch_to.default_content()
    #     self.driver.switch_to.frame("true")
    #     self.driver.switch_to.frame("frmain")
    def vb_find(self, *element):
        if len(self.driver.find_elements(*element)) > 0:
            return True
        else:
            return False

    def wait_find(self, loc):
        return WebDriverWait(self.driver, 20, 1).until(EC.presence_of_all_elements_located(loc))
