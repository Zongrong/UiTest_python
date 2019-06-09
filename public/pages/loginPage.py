#coding=utf-8
'''
Created on 2019年4月17日

@author: RobinLiang
'''

from public.common import basepage
from config.globalparam import Env_Url

class loginPage(basepage.Page):
    '''
    登录页面
    '''
    def into_login_page(self):
        """打开登录页面"""
        self.dr.open(Env_Url)

    def input_username(self,userName):
        """输入用户名"""
        self.dr.clear_type('id->login_field',userName) #通过id属性获取元素

    def input_password(self,password):
        """输入密码"""
        self.dr.clear_type('id->password',password)
        
    def click_login_button(self):
        """点击登录按钮"""
        #self.dr.click('xpath->//input[@name="commit"]') #通过xpath方式获取元素
        #self.dr.click('css->input.btn.btn-primary.btn-block')#通过css的属性方式获取元素
        self.dr.click('name->commit') #通过name属性获取元素

    def return_title(self):
        """返回浏览器标题"""
        return self.dr.get_title()


    
