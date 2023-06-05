import os

from utils.yaml import YamlOperate

# 获取当前文件的绝对路径
current_file_absolute = os.path.abspath(__file__)
# print(current_file_absolute)

# 获取项目的绝对路径
PROJECT_PATH_ABSOLUTE = os.path.dirname(os.path.dirname(current_file_absolute))
# print(PROJECT_PATH_ABSOLUTE)

# config文件夹路径
_config_dir_path = PROJECT_PATH_ABSOLUTE + os.sep + "config"

# data文件夹路径
_data_dir_path = PROJECT_PATH_ABSOLUTE + os.sep + "data"

# conf.yml文件路径
_config_yaml_path = _config_dir_path + os.sep + "conf.yaml"

# login_data文件路径
_login_data_yml_path = _data_dir_path + os.sep + "login_data.yaml"

# logs日志文件夹路径
_config_logs_path = PROJECT_PATH_ABSOLUTE + os.sep + "logs"

# db_conf.yml文件路径
_db_config_yaml_path = _config_dir_path + os.sep + "db_conf.yml"

# report文件夹路径
_report_dir_path = PROJECT_PATH_ABSOLUTE + os.sep + "report"

# report_json文件夹路径
_report_json_path = _report_dir_path + os.sep + "json"

# report_index文件夹路径
_report_index_path = _report_dir_path + os.sep + "index"


# 返回report文件夹路径
def get_report_path():
    return _report_dir_path


# 返回report_json文件夹路径
def get_report_json_path():
    return _report_json_path


# 返回report_index文件夹路径
def get_report_index_path():
    return _report_index_path


# 返回data文件夹路径
def get_data_path():
    return _data_dir_path


# 返回login_data.yml路径
def get_login_data_path():
    return _login_data_yml_path


# 为私有变量返回给外部
def get_config_path():
    return _config_dir_path


# 为私有变量返回给外部
def get_config_yaml():
    return _config_yaml_path


def get_db_config_yaml():
    return _db_config_yaml_path


def get_logs_path():
    return _config_logs_path


class ConfYaml:
    def __init__(self):
        self.conf = YamlOperate(get_config_yaml()).yaml_read_single()  # 读取conf.yml
        # self.db_conf = YamlOperate(get_db_config_yaml()).yaml_read_single()  # 读取db_conf.yml

    def get_email_info(self):
        """
        :return: 邮箱信息
        """
        return self.conf['EMAIL']

    def get_excel_name(self):
        """
        返回测试用例文件名
        :return:
        """
        self.excel_name = self.conf['BASE']['EXCEL']['excel_name']
        return self.excel_name

    def get_excel_sheet_by(self):
        """
        返回测试用例文件的sheet名称
        :return:
        """
        self.sheet_by = self.conf['BASE']['EXCEL']['sheet_by']
        return self.sheet_by

    def get_config_url(self):
        """
        获取url
        :return:
        """
        self.url = self.conf['BASE']['url']
        # print(self.url)
        return self.url

    def get_config_person_url(self):
        """
        获取个人中心url
        :return:
        """
        self.url = self.conf['BASE']['url']['url_person']
        return self.url

    def get_config_loglevel(self):
        """
        获取日志级别
        :return:
        """
        self.log_level = self.conf['BASE']['url']['log_level']
        return self.log_level

    def get_config_extension(self):
        """
        获取日志扩展名
        :return:
        """
        self.log_extension = self.conf['BASE']['url']['log_extension']
        return self.log_extension

    def get_db_config_yml(self, db):
        """
        获取db_conf.yml文件内容,根据db_alias获取该名称下的数据信息
        :return:
        """
        return self.db_conf[db]

    def get_login_user_info(self):
        self.user_info = self.conf['USER_INFO']
        return self.user_info

    # if __name__ == '__main__':
    # ConfYaml().get_excel_sheet_by()
    # print(ConfYaml().get_email_info())
