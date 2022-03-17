# -*- coding: utf-8 -*-
"""
@Auth ： WangHao
@File ：config.py
@Email：whang27@163.com
"""
import os

BASE_URL = "http://47.94.168.241:8080"
# 项目路径
BASE_PATH = os.path.dirname(os.path.abspath(__file__))
BASE_HEADERS = {
    "Content-Type": "application/json",
    "Authorization": "",
}
# 登录账号
acconut = ["15321919666", "123456"]

# 日志文件存放路径
TEST_LOG = os.path.join(BASE_PATH, "logs")
# 数据文件存放路径
TEST_DATA = os.path.join(BASE_PATH, "data")
# 测试报告存放路径
TEST_REPORT = os.path.join(BASE_PATH, "reports/")