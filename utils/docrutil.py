import ddddocr
from PIL import Image


class DOcr(object):
    def __init__(self):
        self.docr_ocr = ddddocr.DdddOcr()

    def docr(self, image_path):
        with open(image_path, 'rb') as f:
            img_bytes = f.read()
        return self.docr_ocr.classification(img_bytes)

    def docr_rect(self, image_path, rect):
        left = rect['x']
        top = rect['y']
        right = left + rect['width']
        bottom = top + rect['height']
        img = Image.open(image_path).crop((left, top, right, bottom))  # 通过原图把验证码位置截取出来
        img.save(image_path)  # 替换原图

        with open(image_path, 'rb') as f:
            img_bytes = f.read()
        return self.docr_ocr.classification(img_bytes)
