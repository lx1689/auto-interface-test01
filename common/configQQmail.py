# coding=utf-8
import smtplib
from email.mime.text import MIMEText

class sendEmail():
    def __init__(self,sender,password,resever,subject,content):
        self.sender = sender
        self.password = password           #qq邮箱授权码
        self.reserver = resever
        self.subject = subject
        self.content = content

    def send(self):
        message = MIMEText(self.content)
        message["subject"] = self.subject
        message["from"] = self.sender
        message["to"] = self.reserver
        try:
            server = smtplib.SMTP_SSL("smtp.qq.com",465)
            server.login(self.sender,self.password)
            server.sendmail(self.sender,self.reserver,message.as_string())
            print("邮件发送成功")
        except Exception as e:
            print("邮件发送失败")
        finally:
            server.quit()