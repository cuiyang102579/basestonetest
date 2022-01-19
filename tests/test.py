# -*- coding:utf-8 -*-
# @author: cuiyang
# @Date: 2022/1/9 15:33
# @Software:basestonetest
# @file: test.py
import json

from Common.Request import BasicRequest

url = 'https://api-test.hobby666.com/api/v1/user/sms/sendSms'
requestBody = {'mobile': '18900000001'}
headers = {"content-type": "application/x-www-form-urlencoded"}
resp = BasicRequest.apireq(url=url, method="POST", header=headers, data=requestBody)
result = json.loads(resp)
if result['code'] == 200 or result['code'] ==81010001 :
    print('msg send success')
print(result['code'])


url = 'https://api-test.hobby666.com/api/v1/user/registerLogin'
requestBody = {'mobile': '18900000001','msgCode':'123456'}
headers = {"content-type": "application/json; charset=UTF-8"}
resp = BasicRequest.apireq(url=url, method="POST", header=headers, json=requestBody)
result2 = json.loads(resp)
print(result2)