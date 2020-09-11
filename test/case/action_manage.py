# -*- coding: utf-8 -*-
# @Department: 测试
# @Author: 杨凤娇
# @Description: 登录
import unittest
from utils.config import Config, DATA_PATH, REPORT_PATH
from utils.log import logger
from utils.file_reader import ExcelReader
from test.pages.login_page import Login
from test.pages.action_manage import ActionManage
import HTMLTestRunner


class TestActionManage(unittest.TestCase):

    URL = Config().get('URL')

    def sub_setUp(self):
        self.page = Login().get(self.URL, maximize_window=True)

    def sub_tearDown(self):
        self.page.quit()

    def test_a(self):
        """ 活动添加测试 """
        data = ExcelReader(excel=DATA_PATH + '/pro_add.xlsx', sheet='添加').data
        for d in data:
            with self.subTest(data=d):
                self.sub_setUp()
                self.page.user_login("5221", "csxt2018", "")
                logger.info(self.page.loginText_loc())
                ActionManage(self.page).action_add(d.get('院内活动名称'), d.get('院内活动编号'), d.get('所在学科1')
                                                   , d.get('所在学科2'), d.get('所在学科3'), d.get('举办方式'), d.get('举办开始时间')
                                                   , d.get('举办结束时间'), d.get('考核方式'), d.get('学时'), d.get('拟授学分')
                                                   , d.get('备注'), d.get('教师姓名1'), d.get('讲授题目1'), d.get('学时1')
                                                   , d.get('教学方法1'), d.get('教师姓名2'), d.get('讲授题目2'), d.get('学时2')
                                                   , d.get('教学方法2'))
                res = ActionManage(self.page).verify_action(d.get('院内活动名称'), d.get('院内活动编号'), d.get('举办开始时间')[:4]+'年'
                                                            , d.get('所在学科1'), d.get('所在学科2'), d.get('所在学科3')
                                                            , d.get('举办开始时间'), d.get('举办结束时间'))
                # res = ActionManage(self.page).verify_action("00", "", "", "", "", "", "", "")
                if res:
                    self.page.getImage()  # 截图
                    logger.info("添加“"+d.get('院内活动名称')+"”院内活动成功！")
                else:
                    self.page.getImage()  # 截图
                    logger.warning("未查询到添加活动，可能添加失败或查询功能存在缺陷！")
                self.sub_tearDown()


if __name__ == "__main__":
    report = REPORT_PATH + '\\report.html'
    with open(report, 'wb') as f:
        runner = HTMLTestRunner.HTMLTestRunner(f, verbosity=2, title='自动化测试报告', tester='杨某某'
                                               , description='运行环境：windows 10 x64, Chrome')
        runner.run(TestActionManage('test_a'))
        f.close()
