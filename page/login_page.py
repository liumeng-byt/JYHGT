from base.base import Base
import page


# 登录
class LoginHandle(Base):
    """业务层与操作层合并"""

    # 输入用户名
    def page_input_phone(self, phone):
        self.base_input(page.phone, phone)

    # 输入密码
    def page_input_password(self, password):
        self.base_input(page.password, password)

    # 输入验证码
    def page_input_verify_code(self, code):
        self.base_input(page.verify_code, code)

    # 清空验证码输入框
    def page_clear_verify_code(self):
        self.base_find_element(page.verify_code).clear()

    # 获取验证码文本框位置
    def page_get_verify_code_rect(self):
        self.base_find_element(page.verify_code_rect)

    # 点击登录
    def page_click_login(self):
        self.base_click(page.login_btn)

    # 点击验证码
    def page_click_verify_code_rect(self):
        self.base_click(page.verify_code_rect)

    # 登录后判断元素是否存在
    def page_element_if_exit(self):
        self.base_element_if_exit(page.search)

    # 截图(全屏)
    def page_get_image_full_screen(self, path):
        self.base_get_image_full_screen(path)

    # 截图（元素）
    def page_get_iamge_element(self, path):
        self.base_get_image_element(page.verify_code_rect, path)

    # 业务层(组装操作层）
    def page_excute_login(self, phone, password, verify_code):
        self.page_input_phone(phone)  # 执行用户名输入
        self.page_input_password(password)  # 执行密码输入
        self.page_input_verify_code(verify_code)  # 执行验证码输入
        self.page_click_login()  # 执行登录
