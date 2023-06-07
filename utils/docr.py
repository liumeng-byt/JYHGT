import os

import ddddocr
from PIL import Image

from utils.log import GetLogger


class DOcr(object):
    def __init__(self):
        self.docr_ocr = ddddocr.DdddOcr()
        self.logger = GetLogger()

    def docr(self, image_path):
        try:
            with open(image_path, 'rb') as f:
                img_bytes = f.read()
            return self.docr_ocr.classification(img_bytes)
        except Exception as e:
            self.logger.get_logger().error(e)
        finally:
            self.delete_file(image_path)

    def docr_rect(self, image_path, rect):
        left = rect['x']
        top = rect['y']
        right = left + rect['width']
        bottom = top + rect['height']
        img = Image.open(image_path).crop((left, top, right, bottom))  # 通过原图把验证码位置截取出来
        img.save(image_path)  # 替换原图
        try:
            with open(image_path, 'rb') as f:
                img_bytes = f.read()
            return self.docr_ocr.classification(img_bytes)
        except Exception as e:
            self.logger.get_logger().error(e)
        finally:
            self.delete_file(image_path)

    def delete_file(self,image_path):
        os.remove(image_path)

