import time

from base.base import Base
import page


#  新增样品
class NewSampleHandle(Base):
    # 点击样品菜单
    def page_click_sample_menu(self):
        self.base_click(page.sample_menu)

    # 点击样品管理
    def page_click_sample_manage_menu(self):
        self.base_click(page.sample_manage_menu)

    # 点击新增按钮
    def page_new_btn(self):
        self.base_click(page.new_btn)

    # 输入样品名称
    def page_input_sample_name(self, data):
        self.base_input(page.sample_name, data)

    # 点击所属酒厂输入框
    def page_click_winery(self):
        self.base_click(page.winery_box)

    # 选择酒厂
    def page_select_winery(self):
        self.base_click(page.winery_name)

    # 选择收样品方式
    def page_select_receive_sample_way(self):
        self.base_click(page.receive_sample_way)

    def page_input_qr_code_amount(self,data):
        self.base_input(page.qr_code_amount,data)

    # 点击提交按钮
    def page_click_submit_btn(self):
        self.base_click(page.submit_btn)

    # 业务层(组装操作层）
    def page_excute_new_sample(self, data):
        self.page_click_sample_menu()
        self.page_click_sample_manage_menu()
        self.page_new_btn()
        self.page_input_sample_name(data)
        self.page_click_winery()
        self.page_select_winery()
        self.page_select_receive_sample_way()
        self.page_input_qr_code_amount(1)
        self.page_click_submit_btn()

