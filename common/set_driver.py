import os
from selenium import webdriver
# from configure_file import config #调用配置文件的封装方法

def set_devier():
    current_path = os.path.dirname(__file__)  # 获取当前路径
    webdriber_path = os.path.join(current_path, '..\webdriver\chromedriver.exe')
    driver = webdriver.Chrome(executable_path=webdriber_path)
    driver.implicitly_wait(10)  # 隐式等待
    driver.maximize_window()
    driver.get('https://hfw.sj56.com.cn/tes/main/index.html#')  # 打开网站
    return driver
