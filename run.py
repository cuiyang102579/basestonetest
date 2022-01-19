# -*- coding:utf-8 -*-
# @author: cuiyang
# @Date: 2022/1/9 13:47
# @Software:basestonetest
# @File    : run.py

"""
运行用例集：
    python3 run.py

'--allure_severities=critical, blocker'
'--allure_stories=测试模块_demo1, 测试模块_demo2'
'--allure_features=测试features'

"""
import os
import pytest
from Common import Log
from Conf import Config

if __name__ == '__main__':
    conf = Config.Config()
    log = Log.MyLog()

    xml_report_path = conf.xml_report_path
    html_report_path = conf.html_report_path

    for i in os.listdir(xml_report_path):
        #   模板文件都是json格式的
        if 'json' in i or 'txt' in i:
            os.remove(xml_report_path+'/'+i)

    # 定义测试集
    args = ['-vs',
            './tests/',
            '--alluredir', xml_report_path]
    pytest.main(args)

    cmd = 'allure generate %s -o %s --clean' % (xml_report_path, html_report_path)
    print(cmd)

    try:
        os.system(" %s" % cmd)
    except Exception:
        log.error('执行用例失败，请检查环境配置')
        raise
