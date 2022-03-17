# -*- coding: utf-8 -*-
"""
@Auth ： WangHao
@File ：login_test.py
@Email：whang27@163.com
"""
import os
import unittest
import warnings
import jsonpath
from parameterized import parameterized
import config
from api.common.testBaseCase import TestBaseCase
from api.login.login_api import LoginApi
from testcase.login import log
from utils.fileUtils import FileUtils

login_data = os.path.join(config.TEST_DATA, "login_test.yaml")
data = FileUtils(login_data).read_yaml_byTuple("login_test")
class TestLogin(TestBaseCase):
    """
    登录测试
    """

    def setUp(self):
        self.loginApi = LoginApi()
        # 忽略资源警告信息
        warnings.simplefilter('ignore', ResourceWarning)

    @parameterized.expand(data)
    def test_login(self, phone, password, expect_value):
        response = self.loginApi.login(phone, password)
        actual_value = jsonpath.jsonpath(response, "$.message")[0]
        log.info(f"期望值：{expect_value}")
        log.info(f"实际值：{actual_value}")
        self.assertEqual(expect_value, actual_value)
