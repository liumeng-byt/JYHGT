import datetime
import logging.handlers
import os


class GetLogger(object):
    logger = None

    @classmethod
    def get_logger(cls,file_path=None,log_level=logging.INFO):
        if cls.logger is None:
            cls.logger = logging.getLogger(file_path)  # 定义日志器+日志所在路径
            cls.logger.setLevel(log_level)  # 级别

            sh = logging.StreamHandler()  # 获取控制台处理器

            # 定义日志文件名称
            # current_file_absolute = os.path.abspath(__file__)  # 获取当前文件的绝对路径
            # PROJECT_PATH_ABSOLUTE = os.path.dirname(os.path.dirname(current_file_absolute))  # 获取项目的绝对路径
            # _config_logs_path = PROJECT_PATH_ABSOLUTE + os.sep + "logs"  # logs日志文件夹路径

            # log_path = _config_logs_path  # logs文件夹路径
            log_extension = ".log"  # log扩展名
            log_path = "../logs"  # logs文件夹路径
            current_time = datetime.datetime.now().strftime("%Y-%m-%d")  # 当前时间

            log_save_file = os.path.join(log_path, current_time + log_extension)  # 日志文件名称
            # 获取处理器--文件以时间分割
            th = logging.handlers.TimedRotatingFileHandler(filename=log_save_file,
                                                           when='midnight',
                                                           interval=1,
                                                           backupCount=30,
                                                           encoding='utf-8')
            # 日志显示内容
            fmt = "%(asctime)s %(levelname)s[%(name)s][%(filename)s (%(funcName)s:%(lineno)d] - %(message)s"
            fm = logging.Formatter(fmt)
            sh.setFormatter(fm)  # 输出到控制台
            th.setFormatter(fm)  # 输出到文件
            # 将处理器添加到日志器
            cls.logger.addHandler(sh)
            cls.logger.addHandler(th)

        return cls.logger
#
# if __name__ == '__main__':
#     logger = GetLogger()
#     logger.get_logger(logging.INFO).info("ss")
