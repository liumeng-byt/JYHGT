import re
import time
from PIL import Image, ImageEnhance
from pytesseract import pytesseract
from selenium import webdriver

from utils.pytesseract_verify_code import VerifyCodeIdentify


class CarSalesEnterprise(object):
    def __init__(self):
        """仓储系统"""
        self.url = "http://jyh-test.happywine.cn/#/login"
        self.driver = webdriver.Chrome()
        self.verifycode = VerifyCodeIdentify()


    def login(self,username, password):
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_xpath('//*[@placeholder="登录手机号"]').send_keys(username)
        self.driver.find_element_by_xpath('//*[@placeholder="登录密码"]').send_keys(password)

        while True:
            self.driver.find_element_by_xpath('//*[@id="app"]/div[2]/div[2]/div[2]/div/form/div[3]/div/div/div[1]/div/input').clear()  # 里面可能存在已识别的错的验证码
            screenImg = "./b.png"
            self.driver.save_screenshot(screenImg)# 截屏整个页面
            #  获取验证码框的位置.rect结果包含location和size
            rect= self.driver.find_element_by_xpath('//*[@id="app"]/div[2]/div[2]/div[2]/div/form/div[3]/div/div/div[2]/div/img').rect
            time.sleep(3)
            self.driver.find_element_by_xpath('//*[@placeholder="请输入验证码"]').send_keys(self.verifycode.verify_Code_identify(screenImg,rect))
            time.sleep(2)
            self.driver.find_element_by_xpath('//*[@id="app"]/div[2]/div[2]/div[2]/div/form/div[4]/div/button/span').click() # 点击登录
            print(self.driver.get_cookies())

            # 2定位登录后的页面元素，如果定位到说明登录成功，否则登录失败，重新识别验证码
            try:
                self.driver.find_element_by_xpath('//*[@placeholder="请输入搜索内容" and @popperclass="my-autocomplete"]')
            except:
                print("验证码错误，正在刷新验证码后重试...")
                # print("异常信息：", e)
                # self.driver.find_element_by_xpath("//button[@value=*]").click()  # 本系统验证码输入后点击登录，输入错误，则系统不会自动刷新验证码，需手动点击刷新
                try:
                    self.driver.find_element_by_xpath(
                    '//*[@id="app"]/div[2]/div[2]/div[2]/div/form/div[3]/div/div/div[2]/div/img').click()# 点击验证码刷新
                except:
                    print("找不到元素")

            else:
                print("登录成功，已终止循环识别")
                self.driver.refresh()
                print(self.driver.get_cookies())
                break


if __name__ == '__main__':
    car = CarSalesEnterprise()
    car.login("store2","store123!")