# coding=utf-8
'''
@author: derek
'''

from public.common import mytest
from public.common.log import Log
from public.pages import repositoryDetailPage
from config.globalparam import img_path,data_path
import unittest

class TestRepositoryDetail(mytest.MyTest):
    """测试一个repository的详情页面的功能"""
    def test_01_into_setting_page(self):
        """vx.x-003 验证进入一个已经存在名为testlzr的repository详情页面"""
        self.logger = Log()
        self.logger.info('----开始测试repository详情页面功能----')
        gh = repositoryDetailPage.repositoryDetailPage(self.dr)
        gh.into_RepositoryPage_page()
        self.imgs.append(self.dr.origin_driver.get_screenshot_as_base64())
        self.assertIn('testlzr',self.dr.get_text('css->#js-repo-pjax-container > div.pagehead.repohead.instapaper_ignore.readability-menu.experiment-repo-nav > div > h1'))

    def test_02_delete_repository(self):
        """vx.x 删除名称为testlzr的repository"""
        gh = repositoryDetailPage.repositoryDetailPage(self.dr)
        gh.into_settingPage_name()
        gh.click_deleteRepostory_button()
        gh.input_deleteRepository_name("testlzr")
        gh.click_confirmDelete_Button()
        self.imgs.append(self.dr.origin_driver.get_screenshot_as_base64())
        self.assertIn('Discover interesting projects',self.dr.get_text('css->#dashboard > div > div.Box.p-5.mt-3 > h2'))

if __name__ == '__main__':
    suite = unittest.makeSuite(TestRepositoryDetail, 'test')
    unittest.TextTestRunner(verbosity=2).run(suite)