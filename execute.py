# -*- coding: utf-8 -*-
"""
@Auth ： WangHao
@File ：execute.py
@Email：whang27@163.com
"""
import unittest
import time
import config
from utils import HTMLTestRunner_PY3
from testcase.login.login_test import TestLogin
from testcase.courseMangement.course_test import TestCourse


# 创建测试套件
suite = unittest.TestSuite()
# 测试用添加进测试套件
suite.addTests(unittest.defaultTestLoader.loadTestsFromTestCase(TestLogin))
suite.addTests(unittest.defaultTestLoader.loadTestsFromTestCase(TestCourse))

# 使用HTMLTestRunner运行测试套件
with open(config.TEST_REPORT + f"lagou_report{time.strftime('%Y%m%d %H%M%S')}.html", mode='wb') as f:
    # 实例化runner
    runner = HTMLTestRunner_PY3.HTMLTestRunner(f)
    # 运行测试套件
    result = runner.run(suite)
    # 得到测试结果
    runner.generateReport(suite, result=result)




