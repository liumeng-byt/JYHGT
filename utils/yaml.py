import os
import yaml

from utils.log import GetLogger


class YamlOperate(object):

    def __init__(self, path):
        self.log = GetLogger()
        if os.path.exists(path):
            self.path = path
        else:
            self.log.get_logger().error(FileNotFoundError)
            raise FileNotFoundError('FileNotFoundError')
        self._data_single = None
        self._data_more = None

    # 读取单段内容
    def yaml_read_single(self):
        if not self._data_single:
            try:
                with open(self.path, 'r', encoding='utf-8') as f:
                    self._data_single = yaml.safe_load(f)
            except Exception as e:
                self.log.get_logger().error("YamlSingleReadError:{}".format(e))
                return
        return self._data_single

    # 读取多段内容
    def yaml_read_more(self):
        if not self._data_more:
            try:
                with open(self.path, 'r', encoding='utf-8') as f:
                    self._data_more = list(yaml.safe_load_all(f))
            except Exception as e:
                self.log.get_logger().error("YamlMoreReadError:{}".format(e))
        return self._data_more

    # 写入yaml文件
    def yaml_write(self, data):
        try:
            with open(self.path, mode='a', encoding='utf-8') as f:
                # f.write(data) # 会从尾部追加
                yaml.dump(data, stream=f, allow_unicode=True)  # 换行追加
        except Exception as e:
            self.log.get_logger().error("WriteError:{}".format(e))
            raise
        return None

    # 清空yaml文件
    def yaml_clear(self):
        try:
            with open(self.path, mode='w', encoding='utf-8') as f:
                f.truncate()
        except Exception as e:
            self.log.get_logger().error("ClearError:{}".format(e))
            raise
        return None


if __name__ == '__main__':
    res = YamlOperate(r"E:\Code\AutomationApi\RRW\relevance1.yml")
    res.yaml_write("2")
    res.yaml_clear()
