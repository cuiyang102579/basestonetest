# -*- coding:utf-8 -*-
# @author: cuiyang
# @Date: 2022/1/11 15:11
# @Software:basestonetest
# @file: test_rescouce_mypage.py
import json

from Common.Request import BasicRequest

'''
资源配置服务-resource接口
我的页面资源查询接口
'''

class TestMypage:
    def test_aresource_mypage(self,AssertInit,userLoginGetTicket):
        print(userLoginGetTicket)
        url='https://api-test.hobby666.com/api/v1/resource/mypage'
        headers = {"content-type": "application/x-www-form-urlencoded"}
        headers = dict(headers, **userLoginGetTicket)
        print(headers)
        resp = BasicRequest.apireq(url=url, method="GET", header=headers, data=None)
        result = json.loads(resp)
        # print(result['code'])
        AssertInit.assert_code(result['code'],200)