# -*- coding: utf-8 -*-
# @Department: 测试
# @Author: 杨凤娇
# @Description: 医院 =》活动管理
from test.common.page import Page
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from time import sleep


class ActionManage(Page):
    # 定位元素
    menu1 = (By.XPATH, '//*[@id="menuGov"]/li[9]/a')  # 院内活动管理
    menu2 = (By.XPATH, '//*[@id="menu4"]/ul/li[1]/a')  # 活动管理
    btnAdd = (By.ID, 'btnAdd')  # 添加
    txtProName = (By.ID, 'txtProjName')  # 院内活动名称
    txtProNo = (By.ID, 'txtProjNo')  # 院内活动编号
    ddlKnowledgeType = (By.ID, 'ddlknowledgeType')  # 所在学科
    ddlParentCourse = (By.ID, 'ddlParentCourse')
    ddlChildCourse = (By.ID, 'ddlChildCourse')
    ddlHoldType = (By.ID, 'ddlHoldType')  # 举办方式
    txtStartDate = (By.ID, 'txtStartDate')  # 举办时间
    txtEndDate = (By.ID, 'txtEndDate')
    ddlCheckType = (By.ID, 'ddlCheckType')  # 考核方式
    txtPeriod = (By.ID, 'txtPeriod')  # 学时
    txtScores = (By.ID, 'txtScores')  # 拟授学分
    txtRemark = (By.ID, 'txtRemark')  # 备注
    btnCourse = (By.XPATH, '//*[@id="form1"]/div[3]/table/tbody/tr[9]/td/span[1]/a')  # 添加教师和课程
    teacher1 = (By.XPATH, '//*[@id="subjectList"]/table[1]/tbody/tr[1]/td[3]/input[2]')  # 教师姓名1
    title1 = (By.XPATH, '//*[@id="subjectList"]/table[1]/tbody/tr[1]/td[5]/input')  # 讲授题目1
    date1 = (By.XPATH, '//*[@id="subjectList"]/table[1]/tbody/tr[2]/td[2]/input')  # 学时1
    type1 = (By.XPATH, '//*[@id="subjectList"]/table[1]/tbody/tr[2]/td[4]/select')  # 教学方法1
    teacher2 = (By.XPATH, '//*[@id="subjectList"]/table[2]/tbody/tr[1]/td[3]/input[2]')  # 教师姓名2
    title2 = (By.XPATH, '//*[@id="subjectList"]/table[2]/tbody/tr[1]/td[5]/input')  # 讲授题目2
    date2 = (By.XPATH, '//*[@id="subjectList"]/table[2]/tbody/tr[2]/td[2]/input')  # 学时2
    type2 = (By.XPATH, '//*[@id="subjectList"]/table[2]/tbody/tr[2]/td[4]/select')  # 教学方法2
    delete = (By.XPATH, '//*[@id="subjectList"]/table[1]/tbody/tr[1]/td[1]')  # 删除
    next = (By.ID, 'next')  # 提交
    ddlYear = (By.ID, 'ddlYear')  # 年度
    select1 = (By.ID, 'KnowledgeSelect_ddlknowledge1')  # 所属学科
    select2 = (By.ID, 'KnowledgeSelect_ddlknowledge2')
    select3 = (By.ID, 'KnowledgeSelect_ddlknowledge3')
    btnSearch = (By.ID, 'btnSearch')  # 查询
    listSelect = (By.ID, 'listSelect')  # 选择

    def menu1_loc(self):
        self.find_element(*self.menu1).click()

    def menu2_loc(self):
        self.find_element(*self.menu2).click()

    def btnAdd_loc(self):
        self.find_element(*self.btnAdd).click()

    def txtProName_loc(self, txtProName):
        self.find_element(*self.txtProName).clear()
        self.find_element(*self.txtProName).send_keys(txtProName)

    def txtProNo_loc(self, txtProNo):
        self.find_element(*self.txtProNo).clear()
        self.find_element(*self.txtProNo).send_keys(txtProNo)

    def ddlKnowledgeType_loc(self, ddlKnowledgeType):
        Select(self.find_element(*self.ddlKnowledgeType)).select_by_visible_text(ddlKnowledgeType)

    def ddlParentCourse_loc(self, ddlParentCourse):
        Select(self.find_element(*self.ddlParentCourse)).select_by_visible_text(ddlParentCourse)

    def ddlChildCourse_loc(self, ddlChildCourse):
        Select(self.find_element(*self.ddlChildCourse)).select_by_visible_text(ddlChildCourse)

    def ddlHoldType_loc(self, ddlHoldType):
        Select(self.find_element(*self.ddlHoldType)).select_by_visible_text(ddlHoldType)

    def txtStartDate_loc(self, txtStartDate):
        self.find_element(*self.txtStartDate).clear()
        self.find_element(*self.txtStartDate).send_keys(txtStartDate)

    def txtEndDate_loc(self, txtEndDate):
        self.find_element(*self.txtEndDate).clear()
        self.find_element(*self.txtEndDate).send_keys(txtEndDate)

    def ddlCheckType_loc(self, ddlCheckType):
        Select(self.find_element(*self.ddlCheckType)).select_by_visible_text(ddlCheckType)

    def txtPeriod_loc(self, txtPeriod):
        self.find_element(*self.txtPeriod).clear()
        self.find_element(*self.txtPeriod).send_keys(txtPeriod)

    def txtScores_loc(self, txtScores):
        self.find_element(*self.txtScores).clear()
        self.find_element(*self.txtScores).send_keys(txtScores)

    def txtRemark_loc(self, txtRemark):
        self.find_element(*self.txtRemark).clear()
        self.find_element(*self.txtRemark).send_keys(txtRemark)

    def btnCourse_loc(self):
        self.find_element(*self.btnCourse).click()

    def teacher1_loc(self, teacher1):
        self.find_element(*self.teacher1).clear()
        self.find_element(*self.teacher1).send_keys(teacher1)

    def title1_loc(self, title1):
        self.find_element(*self.title1).clear()
        self.find_element(*self.title1).send_keys(title1)

    def date1_loc(self, date1):
        self.find_element(*self.date1).clear()
        self.find_element(*self.date1).send_keys(date1)

    def type1_loc(self, type1):
        Select(self.find_element(*self.type1)).select_by_visible_text(type1)

    def teacher2_loc(self, teacher2):
        self.find_element(*self.teacher2).clear()
        self.find_element(*self.teacher2).send_keys(teacher2)

    def title2_loc(self, title2):
        self.find_element(*self.title2).clear()
        self.find_element(*self.title2).send_keys(title2)

    def date2_loc(self, date2):
        self.find_element(*self.date2).clear()
        self.find_element(*self.date2).send_keys(date2)

    def type2_loc(self, type2):
        Select(self.find_element(*self.type2)).select_by_visible_text(type2)

    def delete_loc(self):
        self.find_element(*self.delete).click()

    def next_loc(self):
        self.find_element(*self.next).click()

    def ddlYear_loc(self, ddlYear):
        Select(self.find_element(*self.ddlYear)).select_by_visible_text(ddlYear)

    def select1_loc(self, select1):
        Select(self.find_element(*self.select1)).select_by_visible_text(select1)

    def select2_loc(self, select2):
        Select(self.find_element(*self.select2)).select_by_visible_text(select2)

    def select3_loc(self, select3):
        Select(self.find_element(*self.select3)).select_by_visible_text(select3)

    def btnSearch_loc(self):
        self.find_element(*self.btnSearch).click()

    # 添加活动
    def action_add(self, txtProName, txtProNo, ddlKnowledgeType, ddlParentCourse, ddlChildCourse, ddlHoldType, txtStartDate
                , txtEndDate, ddlCheckType, txtPeriod, txtScores, txtRemark, teacher1, title1, date1, type1, teacher2
                , title2, date2, type2):
        self.menu1_loc()  # 院内活动管理
        sleep(1)
        self.menu2_loc()  # 活动管理
        self.frame("centerIframeUnitManageAction")
        sleep(1)
        self.btnAdd_loc()  # 添加
        self.back()
        sleep(1)
        self.txtProName_loc(txtProName)  # 院内活动名称
        self.txtProNo_loc(txtProNo)  # 院内活动编号
        self.ddlKnowledgeType_loc(ddlKnowledgeType)  # 所在学科
        sleep(1)
        self.ddlParentCourse_loc(ddlParentCourse)
        sleep(1)
        self.ddlChildCourse_loc(ddlChildCourse)
        self.ddlHoldType_loc(ddlHoldType)  # 举办方式
        self.txtStartDate_loc(txtStartDate)  # 举办日期
        self.txtEndDate_loc(txtEndDate)
        self.ddlCheckType_loc(ddlCheckType)  # 考核方式
        self.txtPeriod_loc(txtPeriod)  # 学时
        self.txtScores_loc(txtScores)  # 拟授学分
        self.txtRemark_loc(txtRemark)  # 拟备注
        self.btnCourse_loc()  # 添加教师和课程
        sleep(1)
        self.teacher1_loc(teacher1)  # 教师姓名1
        self.title1_loc(title1)  # 讲授题目1
        self.date1_loc(date1)  # 学时1
        self.type1_loc(type1)  # 教学方法1
        self.teacher2_loc(teacher2)  # 教师姓名2
        self.title2_loc(title2)  # 讲授题目2
        self.date2_loc(date2)  # 学时2
        self.type2_loc(type2)  # 教学方法2
        self.delete_loc()  # 删除教师1
        sleep(1)
        self.next_loc()  # 提交按钮
        sleep(1)
        self.accept()
        sleep(1)
        self.driver.switch_to.default_content()
        self.frame("centerIframeUnitManageAction")
        sleep(1)

    # 活动验证
    def verify_action(self, txtProName, txtProNo, ddlYear, select1, select2, select3, txtStartDate, txtEndDate):
        self.txtProName_loc(txtProName)  # 院内活动名称
        self.txtProNo_loc(txtProNo)  # 院内活动编号
        if ddlYear != "":
            self.ddlYear_loc(ddlYear)  # 年度
        if select1 != "":
            self.select1_loc(select1)  # 所属学科
        sleep(1)
        if select2 != "":
            self.select2_loc(select2)
        sleep(1)
        if select3 != "":
            self.select3_loc(select3)
        if txtStartDate != "":
            self.txtStartDate_loc(txtStartDate)  # 举办日期
        if txtEndDate != "":
            self.txtEndDate_loc(txtEndDate)
        self.btnSearch_loc()  # 查询
        sleep(1)
        if self.vb_find(*self.listSelect) > 0:
            return True
        else:
            return False
