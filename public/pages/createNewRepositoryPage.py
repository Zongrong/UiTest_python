#coding=utf-8
'''
@author: RobinLiang
'''

import time
from time import sleep
from public.common import basepage

now_time = time.strftime('%Y%m%d%H%M%S')

class createNewRepositoryPage(basepage.Page):
    '''
    新建Repository页面
    '''

    def click_newRepository_button(self):
        '''点击新建Repository按钮'''
        sleep(2)
        self.dr.click("xpath->//a[@class='btn btn-sm btn-primary text-white']")
        sleep(3)

    def input_repository_name(self,repositoryName):
        '''输入repository的名称'''
        self.dr.wait(2)
        self.dr.clear_type('id->repository_name',repositoryName)
        sleep(1)

    def inpit_repository_description(self,repositoryDesc):
        '''输入repository的描述内容'''
        sleep(0.5)
        self.dr.clear_type('id->repository_description',repositoryDesc)
        sleep(0.5)

    def select_visibility_private(self):
        '''选择repository的属性为private'''
        sleep(1)
        self.dr.click('id->repository_visibility_private')
        sleep(0.5)

    def click_CreateRepository_button(self):
        '''点击Create repository按钮'''
        sleep(1)
        self.dr.click('xpath->//*[@id="new_repository"]/div[3]/button')
        sleep(1)

