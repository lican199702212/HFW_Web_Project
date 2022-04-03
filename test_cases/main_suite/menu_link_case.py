import os
import time
import unittest
from selenium import webdriver
import HTMLTestRunner
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from common.set_driver import set_devier
from common.login import login

class MenuLinkCase(unittest.TestCase):
    def setUp(self) -> None:  #把selenium 的初始值配置在setup里面
        # 调用driver.get('https://hfw.sj56.com.cn/tes/main/index.html#')  # 打开网站
        self.driver = set_devier()
        time.sleep(3)
    def tearDown(self) -> None: #测试清理操作
        time.sleep(2)
        self.driver.quit()
    def test_link_case(self):
        '''使用test_link_case 能跳转到内部版'''
        login(self.driver, '18874209921', 'Lc19970212..')  # 调用登录模块
        self.driver.find_element_by_xpath('//span[text()="内部版"]').click()
        self.assertTrue(EC.title_is("内部版"))
        time.sleep(2)
    def test_link_case_01(self):
        '''使用test01 是否能登录'''
        login(self.driver, '18874209921', 'Lc19970212..')  # 调用登录模块
        self.driver.find_element_by_xpath('//span[text()="内部版"]').click()
        time.sleep(3)
        self.driver.find_element_by_xpath('//span[text()="网点维护"]').click()
        self.assertTrue(EC.title_is("网点维护"))
        time.sleep(2)
if __name__ == '__main__':
    unittest.main()
