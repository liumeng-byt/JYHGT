from selenium.webdriver.common.by import By

"""以下是登录数据"""
# phone = (By.XPATH, '//*[@placeholder="登录手机号"]')  # 定位用户名
phone = By.XPATH, '//*[@placeholder="登录手机号"]'  # 定位用户名，去掉括号也是元组，python语法
password = (By.XPATH, '//*[@placeholder="登录密码"]')  # 定位密码
verify_code = (By.XPATH, '//*[@placeholder="请输入验证码"]')  # 定位验证码输入框
login_btn = (By.XPATH, '//*[@id="app"]/div[2]/div[2]/div[2]/div/form/div[4]/div/button/span')  # 定位登录按钮
verify_code_rect = (
    By.XPATH, '//*[@id="app"]/div[2]/div[2]/div[2]/div/form/div[3]/div/div/div[2]/div/img')  # 定位验证码框rect
search = By.XPATH, '//*[@placeholder="请输入搜索内容" and @popperclass="my-autocomplete"]'  # 搜索框
home_page = By.XPATH, '//*[@role="tab"]'  # 首页

"""以下是新增样品数据"""
sample_menu = By.XPATH, '//*[@id="app"]/div[2]/div[2]/div[1]/div/div[2]/div[1]/div/ul/div/li[9]/div/span'  # 样品菜单
sample_manage_menu = By.XPATH, '//*[@id="app"]/div[2]/div[2]/div[1]/div/div[2]/div[1]/div/ul/div/li[9]/ul/li[1]/span'  # 样品管理菜单
new_btn = By.XPATH, '//*[@id="avue-view"]/div/div/div/div/div[2]/div/div[1]/div[1]/button/span'  # 新增按钮
sample_name = By.XPATH, '//*[@class="el-dialog__body"]//*[@placeholder="请输入 样品名称"]'  # 样品名称输入框
winery_box = By.XPATH,'//*[@class="el-dialog__body"]//*[@placeholder="请选择 所属酒厂"]'#点击所属酒厂输入框
winery_name = By.XPATH,'/html/body/div[4]/div[1]/div[1]/ul/li[14]'# 选择酒厂01
receive_sample_way = By.XPATH,'/html/body/div[3]/div/div[2]/div/div/div/form/div/div/div/div[5]/div/div/div/label[1]/span[1]'# 选择收样方式
qr_code_amount=By.XPATH,'//*[@placeholder="请输入 生成罐坛二维码"]'#输入生产灌坛二维码数量
submit_btn = By.XPATH,'//*[@class="submit_btn_group"]//*[@class="el-button el-button--primary el-button--small"]'# 提交按钮
