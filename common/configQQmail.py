import unittest
import smtplib
import HTMLTestRunner
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header


class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        """判断 foo.upper() 是否等于 FOO"""
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        """ 判断 Foo 是否为大写形式 """
        self.assertTrue('Foo'.isupper())


def get_case_result():
    """ 获取测试用例报告 """
    suite = unittest.makeSuite(TestStringMethods)
    # file_path = r'M:\tests\report.html'
    file_path = r'D:\pycharm\test02\result\report.html'
    with open(file_path, 'wb') as f:
        HTMLTestRunner.HTMLTestRunner(
            stream=f,
            title='HTMLTestRunner版本关于upper的测试报告',
            description='判断upper的测试用例执行情况').run(suite)
    f1 = open(file_path, 'r', encoding='utf-8')
    res = f1.read()
    f1.close()
    return res


def send_email():
    """ 发送邮件 """

    # 第三方 SMTP 服务
    mail_host = "smtp.qq.com"  # 设置服务器
    mail_user = "773041105@qq.com"  # 用户名
    mail_pass = "bactjjbbeodlbebh"  # 口令

    # 设置收件人和发件人
    sender = '773041105@qq.com'
    receivers = ['773041105@qq.com', '407933240@qq.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱

    # 创建一个带附件的实例对象
    message = MIMEMultipart()

    # 邮件主题、收件人、发件人
    subject = '请查阅--测试报告'  # 邮件主题
    message['Subject'] = Header(subject, 'utf-8')
    message['From'] = Header("{}".format(sender), 'utf-8')  # 发件人
    message['To'] = Header("{}".format(';'.join(receivers)), 'utf-8')  # 收件人

    # 邮件正文内容 html 形式邮件
    send_content = get_case_result()  # 获取测试报告
    html = MIMEText(_text=send_content, _subtype='html', _charset='utf-8')  # 第一个参数为邮件内容

    # 构造附件
    att = MIMEText(_text=send_content, _subtype='base64', _charset='utf-8')
    att["Content-Type"] = 'application/octet-stream'
    file_name = 'result.html'
    att["Content-Disposition"] = 'attachment; filename="{}"'.format(file_name)  # # filename 为邮件附件中显示什么名字
    message.attach(html)
    message.attach(att)

    try:
        smtp_obj = smtplib.SMTP()
        smtp_obj.connect(mail_host, 25)  # 25 为 SMTP 端口号
        smtp_obj.login(mail_user, mail_pass)
        smtp_obj.sendmail(sender, receivers, message.as_string())
        smtp_obj.quit()
        print("邮件发送成功")

    except smtplib.SMTPException:
        print("Error: 无法发送邮件")


# if __name__ == '__main__':
    # send_email()