# -*- coding:utf-8 -*-
# @author: cuiyang
# @Date: 2022/1/9 14:37
# @Software:basestonetest
# @file: test_login.py
import pytest

from Conf.Config import Config


class TestLogin:
    def test_android_login(self,AssertInit,userLoginGetTicket):
        assert userLoginGetTicket['userid'] is not None


if __name__ == '__main__':

    conf = Config()
    xml_report_path = conf.xml_report_path
    pytest.main(["-vs", "test_login.py",'--alluredir', xml_report_path])
