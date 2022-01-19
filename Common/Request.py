# -*- coding:utf-8 -*-
# @author: cuiyang
# @Date: 2022/1/9 13:43
# @Software:basestonetest
# @file: Request.py

import logging
import cchardet
import requests
from requests import request, RequestException


class BasicRequest:
    """
    request二次封装
    """

    @staticmethod
    def apireq(url, method=None, header=None, timeout=None, binary=False, flag=False, **kwargs):
        """
        :param url:
        :param method:
        :param header:
        :param timeout:
        :param binary:
        :param verify: 关闭证书校验
        :param flag: True是返回requests.models.Response对象；False则返回str对象
        :param kwargs:
        :return:
        """
        # 默认超时
        _maxTimeout = timeout if timeout else 5
        # 自定义ticket,便于调试
        _headers = header if header else {"content-type": "application/json;charset=UTF-8"}
        # 默认请求方法
        _method = 'GET' if not method else method
        # 日志记录
        log = logging.getLogger()

        # verify=False，访问HTTPS时移除SSL认证，目前直接移除警告
        requests.packages.urllib3.disable_warnings()

        try:
            response = request(url=url, method=_method, headers=_headers, verify=False, **kwargs)

            # 解决乱码问题
            if flag is not True:
                encoding = cchardet.detect(response.content)['encoding']
                if response.status_code == 200:
                    log.info("\n RESPONSE: {0}".format(response.json()))
                    # 把response对象转成字符串类型
                    return response.content if binary else response.content.decode(encoding)
                elif 200 < response.status_code < 400:
                    log.error(f"Redirect_URL: {response.url}")
                log.error('Get invalid status code %s while scraping %s', response.status_code, url)
                return response

            # 增加通过response对象获取cookie, 增加标志位flag实现
            return response

        except RequestException as e:
            log.error(f'Error occurred while scraping {url}, Msg: {e}', exc_info=True)
