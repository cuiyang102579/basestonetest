# -*- coding:utf-8 -*-
# @author: cuiyang
# @Date: 2022/1/9 14:09
# @Software:basestonetest
# @file: conftest.py
# pytest添加识别环境信息的命令
# 注册自定义参数 env 到配置对象
import json

import pytest as pytest
from pydantic import BaseModel

from Common.Request import BasicRequest
from Model.data_model import DataTemplate



@pytest.fixture(scope="session")
def SendSmsReq():
    class SendSms(BaseModel):
        mobile: str = "18900000001"

    return DataTemplate(SendSms)



@pytest.fixture(scope="session")
def SendSms(SendSmsReq):
    url = 'https://api-test.hobby666.com/api/v1/user/sms/sendSms'
    requestBody = SendSmsReq.default
    headers = {"content-type": "application/x-www-form-urlencoded"}
    resp = BasicRequest.apireq(url=url, method="POST", header=headers, data=requestBody)
    result = json.loads(resp)
    assert result['code'] == 200  or result['code']==81010001



@pytest.fixture(scope="session")
def LoginReq():
    class Login(BaseModel):
        mobile: str = "18900000001"
        msgCode: str = "123456"

    return DataTemplate(Login)


@pytest.fixture(scope="session")
def userLoginGetTicket(SendSms,LoginReq):
    url = 'https://api-test.hobby666.com/api/v1/user/registerLogin'
    requestBody = LoginReq.default
    headers = {"content-type": "application/json; charset=UTF-8"}
    resp = BasicRequest.apireq(url=url, method="POST", header=headers, json=requestBody)
    result = json.loads(resp)
    assert result['data']['token'] is not None
    return {'userid':result['data']['userId'],'Token':result['data']['token']}
