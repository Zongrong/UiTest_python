# -*- coding: utf-8 -*-

import unittest
import time
from config import globalparam
from public.common import sendmail
from public.common import HTMLTestRunner_CN

def run():
    test_dir = './testcase'
    suite = unittest.defaultTestLoader.discover(start_dir=test_dir, pattern='test*.py')

    now = time.strftime('%Y-%m-%d_%H-%M-%S')
    reportname = globalparam.report_path + '//' + 'TestReport_' + now + '.html'
    with open(reportname,'wb') as f:
        runner = HTMLTestRunner_CN.HTMLTestRunner(
            stream=f,
            title='GitHub平台测试报告_{0}'.format(now),
            description='详细测试用例结果'
                        '环境名称：{0}。 URL：{1}'.format(globalparam.Env_Name,globalparam.Env_Url),
            verbosity=2,
            retry=5,
            save_last_try=True
        )
        runner.run(suite)
    time.sleep(3)
    # 发送邮件
    mail = sendmail.SendMail()
    mail.send()

if __name__=='__main__':
    run()