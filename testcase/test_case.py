import os

import allure
import pytest
import time
import page
from config.conf import ConfYaml
from page.login_page import LoginHandle
from utils.ass import AssertUtil


from page.sample_page import NewSampleHandle
from utils.docr import DOcr
from utils.log import GetLogger
from utils.windows_msg_pyaut import WindowsMsg


@allure.feature("TestCase")
class TestCase(object):
    driver = None

    def setup_class(self):
        self.driver = LoginHandle()
        # self.driver_sample = NewSampleHandle()
        self.windows_msg = WindowsMsg()
        self.logger = GetLogger()
        self.ass = AssertUtil()
        self.docr = DOcr()

    # def teardown_class(self):
    #     self.windows_msg.msg_alert(title="msg", text="点击关闭浏览器")
    #     DriverUtil().quit_driver()

    @pytest.mark.parametrize('username,password', [
        (ConfYaml().get_login_user_info()['admin']['username'],
         ConfYaml().get_login_user_info()['admin']['password'])])
    @allure.title("登陆成功")
    def test_success_login(self, username, password):
        while True:
            self.driver.page_clear_verify_code()  # 清空验证码
            # 截图（元素）并识别
            time.sleep(1)
            image = "../image/{}.png".format(time.strftime("%Y_%m_%d %H-%M-%S"))
            self.driver.page_get_iamge_element(image)
            self.driver.page_excute_login(username, password, self.docr.docr(image))
            try:
                self.driver.base_find_element(page.search, timeout=0.05)  # 找到登录后的元素即登录成功
            except:
                print("正在刷新验证码后重试...")
                try:
                    self.driver.page_click_verify_code_rect()  # 点击验证码刷新
                except Exception as e:
                    self.logger.get_logger().info("找不到元素:", e)
            else:
                print("LoginSuccessfully")
                assert True
                break

    def test_new_sample(self):
        NewSampleHandle().page_excute_new_sample("样品名称")

if __name__ == '__main__':
    pytest.main()
    os.system("allure generate ../report/result -o ../report/html --clean")

