# -*- coding: utf-8 -*-
'''
@author: RobinLiang
'''
import unittest
from public.common import mytest
from public.common.log import Log
from public.pages import createNewRepositoryPage
from config.globalparam import img_path,data_path


class TestMyRepostory(mytest.MyTest):
    """我的repository"""
    def test_01_go_newRepostory_page(self):
        """vx.x-001 验证进入新建repository页面"""
        self.logger = Log()
        self.logger.info('----开始测试myRepository页面部分功能----')
        gh = createNewRepositoryPage.createNewRepositoryPage(self.dr)
        gh.click_newRepository_button()
        self.imgs.append(self.dr.origin_driver.get_screenshot_as_base64())
        self.assertEqual('Create a New Repository',self.dr.get_title())

    def test_02_create_repository(self):
        """vx.x-002 新建名称为testlzr的repository"""
        gh = createNewRepositoryPage.createNewRepositoryPage(self.dr)
        gh.input_repository_name("testlzr")
        gh.inpit_repository_description("Testing to create a repository")
        gh.select_visibility_private()
        gh.click_CreateRepository_button()
        self.imgs.append(self.dr.origin_driver.get_screenshot_as_base64())
        self.assertTrue('css->#js-repo-pjax-container > div.pagehead.repohead.instapaper_ignore.readability-menu.experiment-repo-nav > nav')

if __name__ == '__main__':
    suite = unittest.makeSuite(TestMyRepostory, 'test')
    unittest.TextTestRunner(verbosity=2).run(suite)