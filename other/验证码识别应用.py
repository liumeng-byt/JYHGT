import time
from selenium import webdriver
from selenium.webdriver.common.by import By

from utils.docrutil import DOcr


class CarSalesEnterprise(object):
    def __init__(self):
        """仓储"""
        self.url = "http://jyh-test.happywine.cn/#/login"
        self.driver = webdriver.Chrome()
        self.docr = DOcr()

        self.vertify_input = By.XPATH, '//*[@placeholder="请输入验证码"]'  # 验证码输入框
        self.vertify = By.XPATH, '//*[@id="app"]/div[2]/div[2]/div[2]/div/form/div[3]/div/div/div[2]/div/img'  # 验证码文本位置
        self.login_btn = By.XPATH, '//*[@id="app"]/div[2]/div[2]/div[2]/div/form/div[4]/div/button/span'  # 登录按钮
        self.search = By.XPATH, '//*[@placeholder="请输入搜索内容" and @popperclass="my-autocomplete"]'  # 搜索框
        self.username = By.XPATH, '//*[@placeholder="登录手机号"]'  # 用户名输入框
        self.code = By.XPATH, '//*[@placeholder="登录密码"]'  # 密码输入框

    def login(self, username, password):
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.driver.find_element(*self.username).send_keys(username)
        self.driver.find_element(*self.code).send_keys(password)

        while True:
            self.driver.find_element(*self.vertify_input).clear()  # 里面可能存在已识别的错的验证码
            screenImg = "./image.png"
            self.driver.save_screenshot(screenImg)  # 截屏整个页面
            #  获取验证码框的位置.rect结果包含location和size
            rect = self.driver.find_element(*self.vertify).rect
            self.driver.find_element(*self.vertify_input).send_keys(self.docr.docr_rect(screenImg, rect))
            self.driver.find_element(*self.login_btn).click()  # 点击登录
            # 2定位登录后的页面元素，如果定位到说明登录成功，否则登录失败，重新识别验证码
            try:
                self.driver.find_element(*self.search)
            except:
                print("验证码错误，正在刷新验证码后重试...")
                try:
                    self.driver.find_element(*self.vertify).click()  # 点击验证码刷新
                except:
                    print("找不到元素")
            else:
                print("登录成功，已终止循环")
                print("cookie:", self.driver.get_cookies())
                break


if __name__ == '__main__':
    car = CarSalesEnterprise()
    car.login("store2", "store123!")