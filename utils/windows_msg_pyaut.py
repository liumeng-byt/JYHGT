import pyautogui


class WindowsMsg(object):
    # 消息提示框
    def msg_alert(self, title="标题", text="文本"):
        alert = pyautogui.alert(text, title)
        return alert

    # 消息确认框
    def msg_confirm(self, title="标题", text="文本"):
        confirm = pyautogui.confirm(text, title)
        return confirm

    # 自定义选择框 返回按钮值
    def msg_select(self, title, text, select_a, select_b, select_c):
        confirm = pyautogui.confirm(text, title, buttons=[select_a, select_b, select_c])
        return confirm

    # 消息输入框  返回值为用户输入的值 点击取消按钮 返回None
    def msg_input(self, text="文本", title="标题"):
        prompt = pyautogui.prompt(text, title, default="")
        return prompt

    # 密码输入框，输入的内容是隐藏的  后台获取的为明文
    def pwd_input(self):
        password = pyautogui.password('Enter password (text will be hidden)')
        return password


# if __name__ == '__main__':
#     print(WindowsMsg().msg_alert("马上开始", "通知"))
#     print(WindowsMsg().msg_confirm("请先确认", "通知"))
#     print(WindowsMsg().msg_select("请选择", "通知", "aa", "bb", "cc"))
#     print(WindowsMsg().msg_input("请输入内容", "通知"))
#     print(WindowsMsg().pwd_input())
