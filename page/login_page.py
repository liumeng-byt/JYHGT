from base.base import Base
import page


# 登录
class LoginHandle(Base):
    """业务层与操作层合并"""

    # 输入用户名
    def input_phone(self, phone):
        self.base_input(page.phone, phone)

    # 输入密码
    def input_password(self, password):
        self.base_input(page.password, password)

    # 输入验证码
    def input_verify_code(self, code):
        self.base_input(page.verify_code, code)

    # 点击登录
    def click_login(self):
        self.base_click(page.login_btn)

    # 业务层(组装操作层）
    def excute_login(self, phone, password, verify_code):
        self.input_phone(phone)  # 执行用户名输入
        self.input_password(password)  # 执行密码输入
        self.input_verify_code(verify_code)  # 执行验证码输入
        self.click_login()  # 执行登录
