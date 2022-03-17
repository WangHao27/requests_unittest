# -*- coding: utf-8 -*-
"""
@Auth ： WangHao
@File ：testBaseCase.py
@Email：whang27@163.com
"""
from api import log
import unittest

class TestBaseCase(unittest.TestCase):
    """
    测试用例的基类，被所有用例继承
    """

    def setUp(self):
        """
        单个用例执行前的操作
        :return:
        """
        log.info("=======================================Start Test========================================")

    @classmethod
    def setUpClass(cls):
        """
        所有用例执行前的操作
        :return:
        """
        log.info("======================================Start TestCase======================================")

    def tearDown(self):
        """
        单个用例执行后的操作
        :return:
        """
        log.info("========================================End Test======================================== \n")

    @classmethod
    def tearDownClass(cls):
        """
        所有用例执行后的操作
        :return:
        """
        log.info("======================================End TestCase====================================== \n")