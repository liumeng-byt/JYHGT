# from selenium.webdriver.common.by import By
#
# from base.base import Base
# from utils.driverutil import DriverUtil
#
# # from JUi.utils.driver_util import DriverUtil
#
# """
# 登录
# """
# import page
#
#
# class LoginObject(Base):
#     """对象层"""
#     # 定位用户名
#     def find_phone(self):
#         # return self.driver.find_element(self.phone[0], self.phone[1])
#         # return self.driver.find_element(*page.phone)  # 自动解包元组
#         return self.base_find_element(page.phone)
#
#     # 定位密码
#     def find_password(self):
#         # return self.driver.find_element(self.password[0], self.password[1])
#         # return self.driver.find_element(*page.password)  # 自动解包元组
#         return self.base_find_element(page.password)
#
#     # 定位验证码
#     def find_verify_code(self):
#         # return self.driver.find_element(self.verify_code[0], self.verify_code[1])
#         # return self.driver.find_element(*self.verify_code)  # 自动解包元组
#         # return self.driver.find_element(*page.verify_code)  # 自动解包元组
#         return self.base_find_element(page.verify_code)
#
#     # 定位登录按钮
#     def find_login_btn(self):
#         # return self.driver.find_element(self.login_btn[0], self.login_btn[1])
#         # return self.driver.find_element(*self.login_btn)  # 自动解包元组
#         # return self.driver.find_element(*page.login_btn)  # 自动解包元组
#         return self.base_find_element(page.login_btn)
#
#
# class LoginHandle(LoginObject):
#     """操作层"""
#     # 输入用户名
#     def input_phone(self, phone):
#         # self.login_object.find_phone().send_keys(phoone)
#         self.base_input(page.phone, phone)
#
#     # 输入密码
#     def input_password(self, password):
#         # self.login_object.find_password().send_keys(password)
#         self.base_input(page.password, password)
#
#     # 输入验证码
#     def input_verify_code(self, code):
#         # self.login_object.find_verify_code().send_keys(code)
#         self.base_input(page.verify_code, code)
#
#     # 点击登录
#     def click_login(self):
#         # self.login_object.find_login_btn().click()
#         self.base_click(page.login_btn)
#
#
# class LoginTask(object):
#     """业务层"""
#     def __init__(self):
#         """获取操作曾对象"""
#         self.login_operate = LoginHandle()
#
#     def excute_login(self, phone, password, verify_code):
#         self.login_operate.input_phone(phone)  # 执行用户名输入
#         self.login_operate.input_password(password)  # 执行密码输入
#         self.login_operate.input_verify_code(verify_code)  # 执行验证码输入
#         self.login_operate.click_login()  # 执行登录
