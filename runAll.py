# -*- coding: utf-8 -*-
# @Department: 测试
# @Author: 杨凤娇
# @Description:
import unittest, time
from HTMLTestRunner import HTMLTestRunner
import os
from utils.send_email import SendEmail
from utils.config import Config, REPORT_PATH

send_mail = SendEmail(
    username=Config().get("email").get("sender"),  # 发件人
    passwd=Config().get("email").get("password"),  # 密码
    recv=['1028306133@qq.com'],  # 收件人,多个收件人用逗号隔开，如：['1@qq.com', '2@qq.com']
    title='UI自动化测试',  # 标题
    content='三病系统web测试',  # 正文
    file=os.path.join(REPORT_PATH, "report.html"),  # 附件  report.html
    ssl=True,
)
on_off = Config().get("email").get("on_off")

# 指定测试用例为当前文件夹下的test_case目录
test_dir = './test/case'
# 指定测试报告存放的目录
# test_report = REPORT_PATH  # 'D:\\Users\\yanghuan\\PycharmProjects\\YNJJSystem\\report'


# 查找测试报告目录，找到最新生成的测试报告文件
def new_report(test_report):
    list = os.listdir(test_report)
    list.sort(key=lambda fn: os.path.getatime(test_report + '\\' + fn))
    file_new = os.path.join(test_report, list[-1])
    return file_new


def create_suite():
    test_unit = unittest.TestSuite()
    # discover方法定义
    discover = unittest.defaultTestLoader.discover(test_dir, pattern='test_*.py', top_level_dir=None)
    # discover 方法筛选出来的用例，循环添加到测试套件中
    for test_suite in discover:
        for test_case in test_suite:
            test_unit.addTests(test_case)
    print(test_unit)
    return test_unit


if __name__ == '__main__':
    now = time.strftime('%Y-%m-%d %H_%M_%S')
    filename = REPORT_PATH + '\\' + now + 'result.html'
    fp = open(filename, 'wb')
    runner = HTMLTestRunner(stream=fp,
                            title='自动化测试报告',
                            description='运行环境：windows 10, Chrome',
                            tester="测试者"
                            )
    runner.run(create_suite())
    fp.close()
    new_report = new_report(REPORT_PATH)
    if on_off == "on":
        send_mail.send_email()
    else:
        print("邮件发送开关配置关闭，请打开开关后可正常自动发送测试报告")
