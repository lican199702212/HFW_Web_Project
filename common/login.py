from selenium import webdriver
#登录模块
def login(driver,phone,passwd):
    driver.find_element_by_xpath('//input[@id="phoneNumber"]').send_keys(phone)
    driver.find_element_by_xpath('//input[@id="loginPassword"]').send_keys(passwd)
    driver.find_element_by_xpath('//button[@class="sjmain-btn sjmain-btn-block sub-button"]').click()
