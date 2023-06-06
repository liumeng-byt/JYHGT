from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

from config.conf import ConfYaml


class SendEmail:
    def __init__(self, smtp_addr, username, authorization, recv, title=None, password=None, content=None, file=None):
        self.smtp_addr = smtp_addr
        self.username = username
        self.password = password
        self.authorization = authorization
        self.recv = recv
        self.title = title
        self.content = content
        self.file = file

    # 发送邮件方法
    def send_mail(self):
        # MIME
        msg = MIMEMultipart()
        # 初始化邮件信息
        msg.attach(MIMEText(self.content, _charset="utf-8"))
        msg["Subject"] = self.title
        msg["From"] = self.username
        msg["To"] = self.recv
        # 邮件附件
        # 判断是否附件
        if self.file:
            # MIMEText读取文件
            try:
                att = MIMEText(open(self.file, "rb").read(), "base64", "utf-8")
            except Exception as e:
                raise FileNotFoundError(e)
            att["Content-Type"] = 'application/octet-stream'  # 设置内容类型
            att["Content-Disposition"] = 'attachment;filename="%s"' % self.file  # 设置附件头
            msg.attach(att)  # 将内容附加到邮件主体中

        # 登录邮件服务器
        self.smtp = smtplib.SMTP(self.smtp_addr, port=25)
        self.smtp.login(self.username, self.authorization)
        # 发送邮件
        try:
            self.smtp.sendmail(self.username, self.recv, msg.as_string())
        except Exception as e:
            raise Exception(e)
        else:
            print("Email send successful")


if __name__ == "__main__":
    smtp_addr = "smtp.163.com"
    username = "yls_lm@163.com"
    # password = "YLS@lm_00xx"
    authorization = ConfYaml().get_email_info()["authorization"]  # 从配置文件读取
    # authorization = "YIBCXCKZZHNENHVQ"  # 163邮箱密码登录无效，需要使用授权码
    recv = "yls_lm@163.com"
    email = SendEmail(smtp_addr=smtp_addr, username=username, authorization=authorization, recv=recv, title="标题1",
                      content="contant",
                      file=r"./a.png")
    email.send_mail()
