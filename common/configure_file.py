import os
import configparser #系统自带的引用配置文件模块

current_path = os.path.dirname(__file__)  # 获取当前路径
cfg_path = os.path.join(current_path, '..\Conf\local_config.ini') #找到配置文件config.ini并进入
class ConfigUtils:
    def __init__(self,config_path=cfg_path):
        self.__config_path = config_path   #传路径
        self.__conf = configparser.ConfigParser() #先创建一个对象
        self.__conf.read(self.__config_path, encoding="utf-8") #read方法
    #读取配置文件下的文件的方法
    def read_ini(self,sec,option):
        value = self.__conf.get(sec,option)
        return value
    #调用 configure_path 就能打印路径
    @property #属性的方法变成属性方法，少了括号()
    def configure_path(self):
        value = self.read_ini('default','URL')
        return value

config = ConfigUtils()  # 全局对象Config
if __name__ == '__main__':
    config_u = ConfigUtils()
    print(config_u.configure_path)

