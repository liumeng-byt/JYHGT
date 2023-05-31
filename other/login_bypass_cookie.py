import json
import time
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("http://b.test.jyhg.com/#/wel/index")
driver.maximize_window()
driver.implicitly_wait(5)

dick = [{'domain': 'jyh-test.happywine.cn', 'httpOnly': False, 'name': 'saber-refresh-token', 'path': '/',
         'sameSite': 'Lax', 'secure': False,
         'value': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJpc3MiOiJpc3N1c2VyIiwiYXVkIjoiYXVkaWVuY2UiLCJ1c2VyX2lkIjoiMTY0OTAzMzcwNzY0OTg2Nzc3OCIsInJvbGVfaWQiOiIxNTkwMTczMTYyODcxOTQ3MjY1IiwidG9rZW5fdHlwZSI6InJlZnJlc2hfdG9rZW4iLCJkZXB0X2lkIjoiMTEyMzU5ODgxMzczODY3NTIwMSIsImNsaWVudF9pZCI6InNhYmVyIiwiZXhwIjoxNjg1NDI1ODgwLCJuYmYiOjE2ODQ4MjEwODB9.St0f3az_eEY-JPf_7Kd6M4LKNEvAFMlr3XfJL3tQCl_LaRB33AUipx4wi9qGVmhTG6cpJMkrv0k6wy72FxfYnQ'
         },

        {'domain': 'jyh-test.happywine.cn', 'httpOnly': False, 'name': 'saber-access-token', 'path': '/',
         'sameSite': 'Lax', 'secure': False,
         'value': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJpc3MiOiJpc3N1c2VyIiwiYXVkIjoiYXVkaWVuY2UiLCJ0ZW5hbnRfaWQiOiIwMDAwMDAiLCJyb2xlX25hbWUiOiLku5PlupPnrqHnkIblkZgiLCJwb3N0X2lkIjoiMTEyMzU5ODgxNzczODY3NTIwMSIsInVzZXJfaWQiOiIxNjQ5MDMzNzA3NjQ5ODY3Nzc4Iiwicm9sZV9pZCI6IjE1OTAxNzMxNjI4NzE5NDcyNjUiLCJ1c2VyX25hbWUiOiJzdG9yZTIiLCJuaWNrX25hbWUiOiJzdG9yZSIsImRldGFpbCI6eyJ0eXBlIjoid2ViIn0sInRva2VuX3R5cGUiOiJhY2Nlc3NfdG9rZW4iLCJkZXB0X2lkIjoiMTEyMzU5ODgxMzczODY3NTIwMSIsImFjY291bnQiOiJzdG9yZTIiLCJjbGllbnRfaWQiOiJzYWJlciIsImV4cCI6MTY4NDgyNDY4MCwibmJmIjoxNjg0ODIxMDgwfQ.b4GakhffQLTctAgVbTlmnTe82ez86gaVSYuTm2zfJjobcN_V3Tw9zwQrY89z7X0auOzf3fZsRn-9ewjgE55Iqg'
         }
        ]

driver.delete_all_cookies()  # //先清除原有的
# cookies = dick # //这里把第一步的cookie复制上就行
cookiese = json.dumps(dick) # //这里把第一步的cookie复制上就行
cookies = json.loads(cookiese) # //这里把第一步的cookie复制上就行
driver.get("http://b.test.jyhg.com/#/wel/index")
for cookie in cookies:
    cookie_dict = {
        'domain':cookie.get('domain'),  # //这里是固定的每个网站都不同
        'name': cookie.get('name'),
        'value': cookie.get('value'),
        "expires": cookie.get('value'),
        'path': '/',
        'httpOnly': False,
        'HostOnly': False,
        'Secure': False}
    driver.add_cookie(cookie_dict)
driver.refresh()  # //带着cookie重新加载

time.sleep(2)
driver.refresh()
time.sleep(5)
