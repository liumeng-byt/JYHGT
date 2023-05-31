import os

import allure
import pytest
import time
import page
from config.conf import ConfYaml
from page.login_page import LoginHandle
from utils.assertutil import AssertUtil
from utils.driverutil import DriverUtil
from utils.logutil import GetLogger
from utils.windows_msg_pyautogui import WindowsMsg


@allure.feature("登陆")
class TestLogin(object):
    driver = None

    def setup_class(self):
        self.driver = LoginHandle()
        self.windows_msg = WindowsMsg()
        self.logger = GetLogger()
        self.ass = AssertUtil()

    def teardown_class(self):
        time.sleep(3)
        self.windows_msg.msg_alert(title="msg", text="点击关闭浏览器")
        DriverUtil().quit_driver()

    @pytest.mark.parametrize('username,password', [
        (ConfYaml().get_login_user_info()['warehouse']['username'],
         ConfYaml().get_login_user_info()['warehouse']['password'])])
    # @allure.severity(allure.severity_level.MINOR)
    @allure.title("登陆成功")
    def test_success_login(self, username, password):
        try:
            self.driver.excute_login(username, password, self.windows_msg.msg_input("Input Code"))
        except Exception as e:
            self.logger.get_logger().ERROR(e)
        else:
            res = self.driver.base_element_if_exit(page.home_page)  # 判断元素是否存在
            self.ass.assert_if_res_true(res, True)  # 根据元素返回断言


if __name__ == '__main__':
    pytest.main()
    os.system("allure generate ../report/result -o ../report/html --clean")
