from time import sleep
from selenium import webdriver


class DriverUtil(object):
    """浏览器对象管理"""
    __driver = None  # 不用外界调用，所以私有

    @classmethod
    def get_driver(cls, url):
        # 获取浏览器对象
        if cls.__driver is None:
            cls.__driver = webdriver.Chrome()
            cls.__driver.get(url=url)
            cls.__driver.maximize_window()
            cls.__driver.implicitly_wait(10)
        return cls.__driver

    @classmethod
    def quit_driver(cls):
        if cls.__driver:
            sleep(3)
            cls.__driver.quit()
            cls.__driver = None  # 移除对象后，保留对象变量，以备下一次使用

# if __name__ == '__main__':
#     DriverUtil.get_driver()   # 定义为类方法后，可以直接由类对象调用，省略实例化对象过程
#     DriverUtil.quit_driver()
