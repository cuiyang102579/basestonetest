# -*- coding:utf-8 -*-
# @author: cuiyang
# @Date: 2022/1/9 14:10
# @Software:basestonetest
# @file: Config.py

from configparser import ConfigParser
from Common import Log
from enum import Enum
import os


class Config:
    # path
    path_dir = str(os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir)))

    def __init__(self):
        """
        初始化
        """
        self.config = ConfigParser()
        self.log = Log.MyLog()
        self.xml_report_path = Config.path_dir + '/Report/xml'
        self.html_report_path = Config.path_dir + '/Report/html'


class Environment(Enum):
    # 开发环境，swagger默认服务环境
    DEV = 0
    # 测试环境
    FAT = 1
    # 生产环境
    PRE = 2


# 默认全局配置环境变量
env = Environment.DEV



# 桥接模式
class EntryPoint:
    _ENV_URL = {
        Environment.DEV: "https://",
        Environment.FAT: "http://",
        Environment.PRE: "https://"
    }

    @property
    def URL(self):
        return self._ENV_URL[env]

if __name__ == '__main__':
    en = Config()
    print(en.xml_report_path)
    print(en.html_report_path)