from pytesseract import pytesseract
from PIL import Image
import re


class VerifyCodeIdentify(object):
    def verify_Code_identify(self, screenimage, rect):
        # rect = self.driver.find_element(By.XPATH, "//button[@value=*]").rect
        # 从截下来的图中获取验证码位置再保存（如果windows系统缩放比为125%，需每个点都乘以1.25，如果为100%则不乘）
        # left = rect['x'] * 1.25
        # top = rect['y'] * 1.25
        # right = left + rect['width'] * 1.25
        # bottom = top + rect['height'] * 1.25

        left = rect['x']
        top = rect['y']
        right = left + rect['width']
        bottom = top + rect['height']
        img = Image.open(screenimage).crop((left, top, right, bottom)) # 通过原图把验证码位置截取出来

        # 优化图片
        # img = img.convert('RGBA')  # 转换模式：L | RGB
        # img = img.convert('L')  # 转换模式：L | RGB
        # img = ImageEnhance.Contrast(img)  # 增强对比度
        # img = img.enhance(2.0)  # 增加饱和度
        img.save(screenimage) # 保存，替换原图了

        img = Image.open(screenimage) # 读取识别验证码
        code = pytesseract.image_to_string(img).strip()  # 去空格

        # 去特殊符号
        result_code = ''
        for i in code:
            pattern = re.compile(r'[a-zA-Z0-9]')
            m = pattern.search(i)
            if m != None:
                result_code += i
        return result_code
