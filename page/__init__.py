
from selenium.webdriver.common.by import By

"""以下是登录数据"""
# phone = (By.XPATH, '//*[@placeholder="登录手机号"]')  # 定位用户名
phone = By.XPATH, '//*[@placeholder="登录手机号"]'  # 定位用户名，去掉括号也是元组，python语法
password = (By.XPATH, '//*[@placeholder="登录密码"]')  # 定位密码
verify_code = (By.XPATH, '//*[@placeholder="请输入验证码"]')  # 定位验证码
login_btn = (By.XPATH, '//*[@id="app"]/div[2]/div[2]/div[2]/div/form/div[4]/div/button/span')  # 定位登录按钮
home_page = By.XPATH,'//*[@role="tab"]'  # 首页


"""以下是xxx数据"""