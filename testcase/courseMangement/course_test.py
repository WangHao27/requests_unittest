# -*- coding: utf-8 -*-
"""
@Auth ： WangHao
@File ：course_test.py
@Email：whang27@163.com
"""
import os
import warnings
import jsonpath
import config
from api.common.testBaseCase import TestBaseCase
from api.courseManagement.course_api import CourseApi
from utils.fileUtils import FileUtils


class TestCourse(TestBaseCase):

    def setUp(self):
        self.courseApi = CourseApi()
        warnings.simplefilter('ignore', ResourceWarning)

    def test_queryCourseList(self):
        response = self.courseApi.queryCourseList()
        actual_value = jsonpath.jsonpath(response, "$.message")[0]
        self.assertEqual("响应成功", actual_value)

    def test_saveOrUpdateCourse(self):
        course = os.path.join(config.TEST_DATA, "saveCourse_test.json")
        course_data = FileUtils(course).read_json()
        response = self.courseApi.saveOrUpdateCourse(course_data)
        actual_value = jsonpath.jsonpath(response, "$.message")[0]
        self.assertEqual("响应成功", actual_value)
