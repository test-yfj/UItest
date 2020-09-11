# -*- coding: utf-8 -*-
# @Department: 测试
# @Author: 杨凤娇
# @Description:
import unittest
from utils.config import Config
from utils.log import logger
from test.pages.login_page import Login


class TestLogin(unittest.TestCase):
    url = Config().get("URL")

    def setUp(self):
        self.page = Login().get(self.url, maximize_window=True)

    def tearDown(self):
        self.page.quit()

    def test_login_success(self):
        """ 正确登录 """
        res = Login(self.page).login_success("530000sys", "12345678")
        self.assertEqual(res, "云南省妇幼保健院")

    def test_login_error1(self):
        """ 账号错误登录 """
        res = Login(self.page).login_error_uname("530000", "12345678")
        self.assertEqual(res, "当前用户名不存在！")

    def test_login_error2(self):
        """ 密码错误登录 """
        res = Login(self.page).login_error_uname("530000sys", "123456")
        self.assertEqual(res, "用户名或者密码错误")


if __name__ == "__main__":
    unittest.main()
