# -*- coding: utf-8 -*-
# @Department: 测试
# @Author: 杨凤娇
# @Description: 登录页面
from test.common.page import Page
from selenium.webdriver.common.by import By
from time import sleep


class Login(Page):

    txtUserName = (By.XPATH, '//*[@id="login_main"]/div/div[2]/div[2]/form/div[1]/div/input')  # 用户名
    txtPassword = (By.XPATH, '//*[@id="login_main"]/div/div[2]/div[2]/form/div[2]/div/input')  # 密码
    btnSubmit = (By.XPATH, '//*[@id="login_main"]/div/div[2]/div[2]/div[2]/button')  # 登录按钮
    loginText = (By.XPATH, '//*[@id="app"]/div/div[1]/div[4]/div/span')  # 登录单位
    errorText = (By.XPATH, '/html/body/div[2]/div/div[2]/div[1]/div/p')  # 登陆失败弹窗文字

    def txtUserName_loc(self, txtUserName):
        self.find_element(*self.txtUserName).clear()
        self.find_element(*self.txtUserName).send_keys(txtUserName)

    def txtPassword_loc(self, txtPassword):
        self.find_element(*self.txtPassword).clear()
        self.find_element(*self.txtPassword).send_keys(txtPassword)

    def btnSubmit_loc(self):
        self.find_element(*self.btnSubmit).click()

    def loginText_loc(self):
        self.wait_find(self.loginText)
        return self.find_element(*self.loginText).text

    def errorText_loc(self):
        self.wait_find(self.errorText)
        return self.find_element(*self.errorText).text

    # 正常登录
    def login_success(self, userName, password):
        self.txtUserName_loc(userName)  # 用户名
        self.txtPassword_loc(password)  # 密码
        sleep(2)
        self.btnSubmit_loc()  # 提交按钮
        sleep(5)
        return self.loginText_loc()

    # 错误登录
    def login_error_uname(self, userName, password):
        self.txtUserName_loc(userName)
        self.txtPassword_loc(password)
        sleep(2)
        self.btnSubmit_loc()
        sleep(5)
        return self.errorText_loc()
