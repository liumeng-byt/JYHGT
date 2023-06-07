import time
from selenium.webdriver.support.wait import WebDriverWait
from config.conf import ConfYaml
from utils.driver import DriverUtil
from utils.log import GetLogger


class Base(object):
    def __init__(self):
        self.driver = DriverUtil.get_driver(ConfYaml().get_config_url()['url_admin'])
        self.log = GetLogger().get_logger()

    # 查找元素
    def base_find_element(self, loc, timeout=20, poll=0.5):
        try:
            element = WebDriverWait(self.driver, timeout=timeout, poll_frequency=poll).until(lambda x: x.find_element(*loc))
            # self.driver.execute_script("arguments[0].click();",element)
            # TODO 存在元素覆盖问题，找到元素了，却点击不了，可以试试把WebDriverWait分离出来，再通过execute_script运行
            return element
        except Exception as e:
            self.log.error("NoSuchElementError",e)

    # 点击
    def base_click(self, loc):
        self.base_find_element(loc).click()

    # 输入
    def base_input(self, loc, value):
        el = self.base_find_element(loc)
        el.clear()  # 输入前清空
        el.send_keys(value)

    # 获取文本
    def base_get_text(self, loc):
        return self.base_find_element(loc).text

    # 截图方法(全屏)
    def base_get_image_full_screen(self,path):
        # self.driver.get_screenshot_as_file("../image/{}.png".format(time.strftime("%Y_%m_%d %H-%M-%S")))
        # image = "../image/xxx.png"
        self.driver.get_screenshot_as_file(path)

    # 截图（元素）
    def base_get_image_element(self,loc,path):
        self.base_find_element(loc,timeout=2).screenshot(path)

    # 判断元素是否存在
    def base_element_if_exit(self, loc):
        try:
            self.base_find_element(loc, timeout=1)  # 假如找登陆按钮，则需要先退出，如果退出是失败的，则需要等待30秒，这种情况下直接指定2秒，无需等待待太久
            return True
        except:
            return False
