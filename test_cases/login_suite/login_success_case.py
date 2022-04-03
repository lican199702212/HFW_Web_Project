import os
import time
import unittest
from selenium import webdriver
import HTMLTestRunner
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from common.set_driver import set_devier
# from common.configure_file import ConfigUtils
from common.login import login


class LoginSuccessCase(unittest.TestCase):
    def setUp(self) -> None:  #把selenium 的初始值配置在setup里面
        self.driver = set_devier()
    def tearDown(self) -> None: #测试清理操作
        time.sleep(2)
        self.driver.quit()
    def test_login_success(self):
        '''使用test_login_success 是否能登录'''
        login(self.driver,'18874209921','Lc19970212..') #调用登录模块
        self.assertTrue(EC.text_to_be_present_in_element(By.XPATH,'//span[@class="name"]'),'test_login用例执行失败')
if __name__ == '__main__':
    unittest.main(verbosity=2)