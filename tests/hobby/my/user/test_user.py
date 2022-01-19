# -*- coding:utf-8 -*-
# @author: cuiyang
# @Date: 2022/1/11 17:00
# @Software:basestonetest
# @file: test_user.py
import json

from Common.Request import BasicRequest

'''
用户个人信息response
"properties": {
        "avatarImageUrl": {
          "type": "string",
          "description": "头像地址",
          "refType": null
        },
        "birthday": {
          "type": "string",
          "format": "date-time",
          "description": "出生日期",
          "refType": null
        },
        "contentNum": {
          "type": "integer",
          "format": "int32",
          "description": "内容数、投稿数",
          "refType": null
        },
        "description": {
          "type": "string",
          "description": "个性签名",
          "refType": null
        },
        "fansCount": {
          "type": "integer",
          "format": "int32",
          "description": "粉丝数量",
          "refType": null
        },
        "fansUrl": {
          "type": "string",
          "description": "粉丝Url",
          "refType": null
        },
        "followCount": {
          "type": "integer",
          "format": "int32",
          "description": "关注数量",
          "refType": null
        },
        "followUrl": {
          "type": "string",
          "description": "关注Url",
          "refType": null
        },
        "gender": {
          "type": "integer",
          "format": "int32",
          "description": "用户性别",
          "refType": null
        },
        "isVerified": {
          "type": "boolean",
          "description": "是否实名",
          "refType": null
        },
        "likeNum": {
          "type": "integer",
          "format": "int32",
          "description": "获赞数量",
          "refType": null
        },
        "likeUrl": {
          "type": "string",
          "description": "获赞Url",
          "refType": null
        },
        "medalImageUrl": {
          "type": "string",
          "description": "铭牌",
          "refType": null
        },
        "newFansCount": {
          "type": "integer",
          "format": "int32",
          "description": "新粉丝数量",
          "refType": null
        },
        "newLikeNum": {
          "type": "integer",
          "format": "int32",
          "description": "新获赞数量",
          "refType": null
        },
        "nickname": {
          "type": "string",
          "description": "用户昵称",
          "refType": null
        },
        "rank": {
          "type": "integer",
          "format": "int32",
          "description": "用户等级",
          "refType": null
        },
        "recommendNum": {
          "type": "integer",
          "format": "int32",
          "description": "安利数量",
          "refType": null
        },
        "recommendUrl": {
          "type": "string",
          "description": "安利Url",
          "refType": null
        },
        "shareNum": {
          "type": "integer",
          "format": "int32",
          "description": "分享数",
          "refType": null
        },
        "starFlag": {
          "type": "boolean",
          "description": "是否达人",
          "refType": null
        },
        "starIconUrl": {
          "type": "string",
          "description": "达人icon",
          "refType": null
        },
        "starType": {
          "type": "integer",
          "format": "int32",
          "description": "达人类型  0 不是达人；1 个人达人；2主理人",
          "refType": null
        },
        "subscribeState": {
          "type": "integer",
          "format": "int32",
          "description": "0:无关注关系 1: 仅关注 2：仅被关注 3：互相关注",
          "refType": null
        },
        "topicNum": {
          "type": "integer",
          "format": "int32",
          "description": "话题数",
          "refType": null
        },
        "totalCoin": {
          "type": "number",
          "description": "积分余额",
          "refType": null
        },
        "widgetImageUrl": {
          "type": "string",
          "description": "头像挂件",
          "refType": null
        }
      }
'''

class TestUser:
    '''
    获取用户个人信息
    '''
    def test_user_loadUserInfo(self,AssertInit,userLoginGetTicket):
        print(userLoginGetTicket)
        url='https://api-test.hobby666.com/api/v1/user/loadUserInfo'
        headers = {"content-type": "application/x-www-form-urlencoded"}
        headers = dict(headers, **userLoginGetTicket)
        resp = BasicRequest.apireq(url=url, method="POST", header=headers, data=None)
        result = json.loads(resp)
        AssertInit.assert_code(result['code'],200)

    '''
    用户信息
    '''
    def test_user_loadUserInfoCommon(self, AssertInit, userLoginGetTicket):
        print(userLoginGetTicket)
        url = 'https://api-test.hobby666.com/api/v1/user/loadUserInfoCommon'
        headers = {"content-type": "application/x-www-form-urlencoded"}
        headers = dict(headers, **userLoginGetTicket)
        requestBody={"targetUserId":userLoginGetTicket['userid']}
        resp = BasicRequest.apireq(url=url, method="POST", header=headers, data=requestBody)
        result = json.loads(resp)
        AssertInit.assert_code(result['code'], 200)

    '''
    获取目标用户信息
    '''
    def test_user_loadTargetUserInfo(self, AssertInit, userLoginGetTicket):
        print(userLoginGetTicket)
        url = 'https://api-test.hobby666.com/api/v1/user/loadTargetUserInfo'
        headers = {"content-type": "application/x-www-form-urlencoded"}
        headers = dict(headers, **userLoginGetTicket)
        requestBody={"targetUserId":userLoginGetTicket['userid']}
        resp = BasicRequest.apireq(url=url, method="POST", header=headers, data=requestBody)
        result = json.loads(resp)
        AssertInit.assert_code(result['code'], 200)