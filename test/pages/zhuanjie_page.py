# -*- coding: utf-8 -*-
# @Department: 测试
# @Author: 杨凤娇
# @Description:
from test.common.page import Page
from selenium.webdriver.common.by import By
from time import sleep


class Zhuanjie(Page):
    menu1 = (By.XPATH, '//*[@id="app"]/div/div[2]/div[1]/div/div/div/div[1]/div[1]/span[2]')  # 个案转介管理
    menu2 = (By.XPATH, '//*[@id="app"]/div/div[2]/div[1]/div/div/div/div[1]/div[2]/div[1]/div/span[2]')  # IPMTCT阳性个案转介卡
    btnAdd = (By.XPATH, '//*[@id="rtBody"]/div/header/div[1]/button')  # 新增
    unit1 = (By.XPATH, '//*[@id="rtBody"]/div/div/div/div[2]/form/div/div[1]/div[2]/div/div/div/div/div[1]/input')  # 接受单位
    unit2 = (By.XPATH, '/html/body/div[3]/div[1]/div/div[1]/ul/li/span')  # 云南省妇幼保健院
    unit3 = (By.XPATH, '/html/body/div[3]/div[1]/div[2]/div[1]/ul/li[1]/span')  # 昆明市妇幼健康服务中心
    unit4 = (By.XPATH, '/html/body/div[3]/div[1]/div[3]/div[1]/ul/li[1]/span')  # 五华区妇幼保健院
    name = (By.XPATH, '//*[@id="rtBody"]/div/div/div/div[2]/form/div/div[2]/div[1]/div/div/div/input')  # 孕产妇姓名
    jibing1 = (By.XPATH, '//*[@id="rtBody"]/div/div/div/div[2]/form/div/div[2]/div[2]/div/div/div/div/input')  # 感染疾病
    jibing2 = (By.XPATH, '/html/body/div[4]/div[1]/div[1]/ul/li[1]/span')  # HIV
    jibing3 = (By.XPATH, '/html/body/div[4]/div[1]/div[1]/ul/li[2]/span')  # 梅毒
    identity = (By.XPATH, '//*[@id="rtBody"]/div/div/div/div[2]/form/div/div[3]/div[1]/div/div/div/input')  # 身份证号
    interNo = (By.XPATH, '//*[@id="rtBody"]/div/div/div/div[2]/form/div/div[3]/div[2]/div/div/div/input')  # 网络编号
    phone1 = (By.XPATH, '//*[@id="rtBody"]/div/div/div/div[2]/form/div/div[4]/div[1]/div/div/div/input')  # 联系电话
    address = (By.XPATH, '//*[@id="rtBody"]/div/div/div/div[2]/form/div/div[4]/div[2]/div/div/div/input')  # 住址
    contact = (By.XPATH, '//*[@id="rtBody"]/div/div/div/div[2]/form/div/div[5]/div[1]/div/div/div/input')  # 转介单位联系人
    phone2 = (By.XPATH, '//*[@id="rtBody"]/div/div/div/div[2]/form/div/div[5]/div[2]/div/div/div/input')  # 联系电话
    text1 = (By.XPATH, '//*[@id="rtBody"]/div/div/div/div[2]/form/div/div[6]/div/div[1]/textarea')  # 转介原因
    text2 = (By.XPATH, '//*[@id="rtBody"]/div/div/div/div[2]/form/div/div[7]/div/div/textarea')  # 需要接收单位提供的服务
    text3 = (By.XPATH, '//*[@id="rtBody"]/div/div/div/div[2]/form/div/div[8]/div/div/textarea')  # 备注
    time = (By.XPATH, '//*[@id="rtBody"]/div/div/div/div[2]/form/div/div[9]/div/div/div/div/input')  # 转介时间
    btn = (By.XPATH, '//*[@id="rtBody"]/div/div/div/div[3]/span/button[2]')  # 确定
    addSure = (By.XPATH, '/html/body/div[5]/div/div[3]/button[2]')  # 确定新增
    btnSub = (By.XPATH, '//*[@id="rtBody"]/div/main/div[1]/div[4]/div[2]/table/tbody/tr/td[12]/div/button[1]')  # 提交/查看
    btnSure = (By.XPATH, '/html/body/div[3]/div/div[3]/button[2]')  # 确定提交
    btnCancel = (By.XPATH, '//*[@id="rtBody"]/div/div/div/div[3]/span/button')  # 查看页面取消
    btnUpdate = (By.XPATH, '//*[@id="rtBody"]/div/main/div[1]/div[4]/div[2]/table/tbody/tr/td[12]/div/button[2]')  # 修改/撤回
    btnDel = (By.XPATH, '//*[@id="rtBody"]/div/main/div[1]/div[4]/div[2]/table/tbody/tr/td[12]/div/button[3]')  # 删除
    text = (By.XPATH, '/html/body/div[4]/p')  # 操作成功后弹窗文本

    def menu1_loc(self):
        self.find_element(*self.menu1).click()

    def menu2_loc(self):
        self.find_element(*self.menu2).click()

    def btnAdd_loc(self):
        self.find_element(*self.btnAdd).click()

    def unit1_loc(self):
        self.find_element(*self.unit1).click()

    def unit2_loc(self):
        self.find_element(*self.unit2).click()

    def unit3_loc(self):
        self.find_element(*self.unit3).click()

    def unit4_loc(self):
        self.find_element(*self.unit4).click()

    def name_loc(self, name):
        self.find_element(*self.name).click()
        self.find_element(*self.name).clear()
        self.find_element(*self.name).send_keys(name)

    def jibing1_loc(self):
        self.find_element(*self.jibing1).click()

    def jibing2_loc(self):
        self.find_element(*self.jibing2).click()

    def jibing3_loc(self):
        self.find_element(*self.jibing3).click()

    def identity_loc(self, identity):
        self.find_element(*self.identity).clear()
        self.find_element(*self.identity).send_keys(identity)

    def interNo_loc(self, interNo):
        self.find_element(*self.interNo).clear()
        self.find_element(*self.interNo).send_keys(interNo)

    def phone1_loc(self, phone1):
        self.find_element(*self.phone1).clear()
        self.find_element(*self.phone1).send_keys(phone1)

    def address_loc(self, address):
        self.find_element(*self.address).clear()
        self.find_element(*self.address).send_keys(address)

    def contact_loc(self, contact):
        self.find_element(*self.contact).clear()
        self.find_element(*self.contact).send_keys(contact)

    def phone2_loc(self, phone2):
        self.find_element(*self.phone2).clear()
        self.find_element(*self.phone2).send_keys(phone2)

    def text1_loc(self, text1):
        self.find_element(*self.text1).clear()
        self.find_element(*self.text1).send_keys(text1)

    def text2_loc(self, text2):
        self.find_element(*self.text2).clear()
        self.find_element(*self.text2).send_keys(text2)

    def text3_loc(self, text3):
        self.find_element(*self.text3).clear()
        self.find_element(*self.text3).send_keys(text3)

    def time_loc(self, time):
        self.find_element(*self.time).clear()
        self.find_element(*self.time).send_keys(time)

    def btn_loc(self):
        self.find_element(*self.btn).click()

    def addSure_loc(self):
        self.find_element(*self.addSure).click()

    def btnSub_loc(self):
        self.find_element(*self.btnSub).click()

    def btnSure_loc(self):
        self.find_element(*self.btnSure).click()

    def btnCancel_loc(self):
        self.find_element(*self.btnCancel).click()

    def btnUpdate_loc(self):
        self.find_element(*self.btnUpdate).click()

    def btnDel_loc(self):
        self.find_element(*self.btnDel).click()

    def text_loc(self):
        self.wait_find(self.text)
        return self.find_element(*self.text).text

    # 进入转介列表页面
    def menu_enter(self):
        self.menu1_loc()
        sleep(2)
        self.menu2_loc()
        sleep(10)

    # 新增
    def zhuanjie_add(self, name, identity, interNo, phone1, address, contact, phone2, text1, text2, text3, time):
        self.btnAdd_loc()
        sleep(2)
        self.unit1_loc()
        sleep(2)
        self.unit2_loc()
        sleep(2)
        self.unit3_loc()
        sleep(2)
        self.unit4_loc()
        sleep(2)
        self.name_loc(name)
        self.jibing1_loc()
        sleep(2)
        self.jibing2_loc()
        sleep(2)
        self.identity_loc(identity)
        self.interNo_loc(interNo)
        self.phone1_loc(phone1)
        self.address_loc(address)
        self.contact_loc(contact)
        self.phone2_loc(phone2)
        self.text1_loc(text1)
        self.text2_loc(text2)
        self.text3_loc(text3)
        self.time_loc(time)
        self.btn_loc()
        sleep(2)
        self.addSure_loc()
        sleep(2)
        return self.text_loc()

    # 修改
    def zhuanjie_update(self, name, identity, interNo, phone1, address, contact, phone2, text1, text2, text3, time):
        self.btnUpdate_loc()
        sleep(1)
        if name != "":
            self.name_loc(name)
        if identity != "":
            self.identity_loc(identity)
        if interNo != "":
            self.interNo_loc(interNo)
        if phone1 != "":
            self.phone1_loc(phone1)
        if address != "":
            self.address_loc(address)
        if contact != "":
            self.contact_loc(contact)
        if phone2 != "":
            self.phone2_loc(phone2)
        if text1 != "":
            self.text1_loc(text1)
        if text2 != "":
            self.text2_loc(text2)
        if text3 != "":
            self.text3_loc(text3)
        if time != "":
            self.time_loc(time)
        self.btnUpdate_loc()
        sleep(2)
        self.btnSure_loc()
        sleep(2)
        return self.text_loc()

    # 删除
    def zhuanjie_del(self):
        self.btnDel_loc()
        sleep(2)
        self.btnSure_loc()
        sleep(2)
        return self.text_loc()

    # 提交
    def zhuanjie_submit(self):
        self.btnSub_loc()
        sleep(2)
        self.btnSure_loc()
        sleep(2)
        return self.text_loc()

    # 查看
    def zhuanjie_see(self):
        self.btnSub_loc()
        sleep(2)
        self.btnCancel_loc()
        sleep(2)

    # 撤回
    def zhuanjie_back(self):
        self.btnUpdate_loc()
        sleep(2)
        self.btnSure_loc()
        sleep(2)
        return self.text_loc()
