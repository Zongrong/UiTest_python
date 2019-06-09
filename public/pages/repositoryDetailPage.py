#coding=utf-8
'''
Created on 2017年10月25日

@author: derek
'''

import time
from public.common import basepage
from time import sleep

now_time = time.strftime('%Y%m%d%H%M%S')
class repositoryDetailPage(basepage.Page):
    '''
    进入一个repository的详情页面
    '''
    def into_RepositoryPage_page(self):
        '''进入新建的名为testlzr的repository详情页面'''
        sleep(2)
        self.dr.click('xpath->//span[@title="testlzr"]')
        sleep(0.5)

    def into_settingPage_name(self):
        '''进入repository详情的setting页面'''
        time.sleep(2)
        self.dr.click('xpath->//*[@id="js-repo-pjax-container"]/div[1]/nav/a[4]')
        time.sleep(1)

    def click_deleteRepostory_button(self):
        '''点击删除Repository按钮'''
        time.sleep(0.5)
        self.dr.click('xpath->//*[@id="options_bucket"]/div[9]/ul/li[4]/details/summary')
        time.sleep(1)

    def input_deleteRepository_name(self,repostoryName):
        '''输入要删除的repository的名称'''
        self.dr.clear_type('xpath->//*[@id="options_bucket"]/div[9]/ul/li[4]/details/details-dialog/div[3]/form/p/input',repostoryName)
        time.sleep(0.5)

    def click_confirmDelete_Button(self):
        '''点击再次确认删除repository按钮'''
        time.sleep(2)
        self.dr.click('xpath->//*[@id="options_bucket"]/div[9]/ul/li[4]/details/details-dialog/div[3]/form/button')
        time.sleep(3)









