# -*- coding: utf-8 -*-
# @Department: 测试
# @Author: 杨凤娇
# @Description:
import unittest
from utils.config import Config
from utils.log import logger
from test.pages.login_page import Login
from test.pages.zhuanjie_page import Zhuanjie


class TestZhuanjie(unittest.TestCase):
    url = Config().get("URL")

    def setUp(self):
        self.page = Login().get(self.url, maximize_window=True)
        Login(self.page).login_success("530103sys", "12345678")
        Zhuanjie(self.page).menu_enter()

    def tearDown(self):
        self.page.quit()

    def test_1_add(self):
        """ 转介新增测试 """
        res = Zhuanjie(self.page).zhuanjie_add("小芳", "530101199009172578", "BH00001", "15845254565", "云南省昆明市盘龙区",
                                               "王琛", "15254556974", "转介原因tttt", "提供的服务tttt", "备注tttt", "2020-09-01")
        self.assertEqual(res, "添加成功")

    def test_2_update(self):
        """ 转介修改测试 """
        res = Zhuanjie(self.page).zhuanjie_update("陈晓芳", "", "", "", "", "", "", "", "", "", "2020-09-10")
        self.assertEqual(res, "修改成功")

    def test_3_submit(self):
        """ 转介提交测试 """
        res = Zhuanjie(self.page).zhuanjie_submit()
        self.assertEqual(res, "提交成功")

    def test_4_see(self):
        """ 转介查看测试 """
        Zhuanjie(self.page).zhuanjie_see()

    def test_5_back(self):
        """ 已提交转介撤回测试 """
        res = Zhuanjie(self.page).zhuanjie_back()
        self.assertEqual(res, "撤回成功")

    def test_6_del(self):
        """ 转介删除测试 """
        res = Zhuanjie(self.page).zhuanjie_del()
        self.assertEqual(res, "删除成功")


if __name__ == "__main__":
    unittest.main()
