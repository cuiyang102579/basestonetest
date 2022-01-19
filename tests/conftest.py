# -*- coding:utf-8 -*-
# @author: cuiyang
# @Date: 2022/1/9 14:09
# @Software:basestonetest
# @file: conftest.py
# pytest添加识别环境信息的命令
# 注册自定义参数 env 到配置对象
import json

import pytest as pytest
from Common.Assert import Assertions



def pytest_addoption(parser):
    # _env_point = EntryPoint()
    parser.addoption("--env", action="store", default="DEV",
                     help="my option: DEV or FAT or PRO or (fatCockpit：11) or (proCockpit：10)")
    # parser.addini("url", type="args", default=_env_point.URL, help="添加 url 访问地址参数，默认是DEV环境访问地址")


@pytest.fixture(scope="session")
def env(pytestconfig):
    return pytestconfig.getoption("--env")

# 断言类
@pytest.fixture
def AssertInit():
    assertion = Assertions()
    return assertion

