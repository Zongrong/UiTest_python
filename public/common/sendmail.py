# -*- coding: utf-8 -*-

import os
import smtplib
import time
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from public.common.log import Log
from config import globalparam

# 测试报告的路径
reportPath = globalparam.report_path
logger = Log()
# 配置收发件人,如果有多个用户邮箱，用英文逗号隔开
areceiver = 'test1@qq.com,test2@163.com'
acc = 'tester@126.com'
# 自己发件邮箱的用户名和密码
sender_name = 'tester@126.com'
sender_pswd = 'xxxxx'


class SendMail:
    def __init__(self, recver=None):
        """接收邮件的人：list or tuple"""
        if recver is None:
            self.sendTo = areceiver
        else:
            self.sendTo = recver

    def __get_report(self):
        """获取最新测试报告"""
        dirs = os.listdir(reportPath)
        dirs.sort()
        newreportname = dirs[-1]
        print('The new report name: {0}'.format(newreportname))
        return newreportname

    def __take_messages(self):
        """生成邮件的内容，和html报告附件"""
        newreport = self.__get_report()
        self.msg = MIMEMultipart()
        self.msg['Subject'] = 'GitHub平台自动化测试报告'
        self.msg['date'] = time.strftime('%a, %d %b %Y %H:%M:%S %z')

        with open(os.path.join(reportPath, newreport), 'rb') as f:
            mailbody = f.read()
        html = MIMEText(mailbody, _subtype='html', _charset='utf-8')
        self.msg.attach(html)

        # html附件
        att1 = MIMEText(mailbody, 'base64', 'gb2312')
        att1["Content-Type"] = 'application/octet-stream'
        att1["Content-Disposition"] = 'attachment; filename="GitHub-HealthManagement-TestReport.html"'  # 这里的filename可以任意写，写什么名字，邮件中显示什么名字
        self.msg.attach(att1)

    def send(self):
        """发送邮件"""
        self.__take_messages()
        self.msg['to'] = areceiver
        self.msg['Cc'] = acc
        self.msg['from'] = sender_name
        try:
            # tls加密方式，通信过程加密，邮件数据安全，使用正常的smtp端口
            smtp = smtplib.SMTP('WIN-exchange.kmhealthcloud.com', 2525)
            # smtp.set_debuglevel(True)
            smtp.ehlo()
            smtp.starttls()
            #smtp.ehlo()
            smtp.login(sender_name, sender_pswd)
            # smtp = smtplib.SMTP('smtp.126.com',25)
            # smtp.login(sendaddr_name,sendaddr_passwd)
            smtp.sendmail(self.msg['from'], areceiver.split(',') + acc.split(','), self.msg.as_string())
            smtp.close()
            logger.info("发送邮件成功")
        except Exception:
            logger.error('发送邮件失败')
            raise


if __name__ == '__main__':
    sendMail = SendMail()
    sendMail.send()
