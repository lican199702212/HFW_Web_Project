import os
import time
import unittest
from selenium import webdriver
import HTMLTestRunner
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from common.set_driver import set_devier


class LoginFailCase(unittest.TestCase):
    def setUp(self) -> None:  #把selenium 的初始值配置在setup里面
        self.driver = set_devier()
        time.sleep(2)
    def tearDown(self) -> None: #测试清理操作
        time.sleep(2)
        self.driver.quit()
    def test_login_fail(self):
        '''使用test_login_fai 是否能登录'''
        self.driver.find_element_by_xpath('//input[@id="phoneNumber"]').send_keys("18874209921")
        self.driver.find_element_by_xpath('//input[@id="loginPassword"]').send_keys("Lc19970212")
        self.driver.find_element_by_xpath('//button[@class="sjmain-btn sjmain-btn-block sub-button"]').click()
        self.assertTrue(EC.text_to_be_present_in_element(By.XPATH,'//span[@class="name"]'),'test_login用例执行失败')
        # self.assertTrue(WebDriverWait(self.driver,10)).until(EC.alert_is_present())
if __name__ == '__main__':
    unittest.main()
