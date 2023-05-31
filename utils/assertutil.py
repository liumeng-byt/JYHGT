import json

from base.base import Base
from utils.logutil import GetLogger


class AssertUtil:
    def __init__(self):
        self.log = GetLogger()

    # 响应码相等
    def assert_res_code_equal(self, response_code, expected_code):
        try:
            assert int(response_code) == int(expected_code)
            return True
        except:
            self.log.get_logger().error("Error，响应码 %s 与期望响应码 %s 不相等" % (response_code, expected_code))
            raise

    # 响应错误码相等
    def assert_res_errorcode_equal(self, response_errorcode, expected_errorcode):
        try:
            assert int(response_errorcode) == int(expected_errorcode)
            return True
        except:
            self.log.get_logger().error("Error，返回errorcode %s 与期望errorcode %s 不相等" % (response_errorcode, expected_errorcode))
            raise

    # 响应体相等
    def assert_res_body_equal(self, response_body, expected_body):
        try:
            try:
                body = json.dumps(response_body)
            except Exception as e:
                self.log.get_logger().error("字典转换为json错误:{}".format(e))
            assert body == expected_body
            return True
        except:
            self.log.get_logger().error("失败，响应body：%s,期望body：%s" % (body, expected_body))
            raise

    # 响应体包含
    def assert_res_body_include(self, response_body, expected_body):
        try:
            # body = json.dumps(response_body) # 转换为json后，返回html中不会显示中文，所以需要对中文断言的，不用转换
            # assert expected_body in body
            assert expected_body in response_body
            return True
        except:
            self.log.get_logger().error("Error，期望body%s不在返回body%s中" % (expected_body, response_body))
            raise

    # True断言
    def assert_if_res_true(self,res,expected):
        try:
            assert res is expected
            # return True
        except:
            Base().base_get_image()
            self.log.get_logger().error("Error,返回属性不是True")
            raise
        # else:
        #     return True