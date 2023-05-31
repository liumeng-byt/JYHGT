from aip import AipOcr


class BaiDuIdentify(object):
    """免费赠送 1000次/月"""

    def baidu_identify(self, original_image):
        # 输入自己的百度ai账号ID密码
        APP_ID = '23167637'
        API_KEY = 'PtWCrqf2rD1EWgaOEcNuXpIB'
        SECRECT_KEY = 'burl95LeQHMAEW4C9e8POeNgQvgB1hEp'

        client = AipOcr(APP_ID, API_KEY, SECRECT_KEY)

        with open(original_image, 'rb') as picfile_read:
            img = picfile_read.read()
            result = client.basicAccurate(img)
        return result
