# -*- coding: utf-8 -*-
"""
@Auth ： WangHao
@File ：course_api.py
@Email：whang27@163.com
"""
import config
from api.common.baseApi import BaseApi


class CourseApi(BaseApi):

    def __init__(self):
        """
        获取登录token的值
        """
        super().__init__()
        phone = config.acconut[0]
        password = config.acconut[1]
        # 将token的值初始化到请求头中
        config.BASE_HEADERS['Authorization'] = self.get_token(phone, password)
        self.s.headers = config.BASE_HEADERS

    def queryCourseList(self):
        """
        查询所有课程列表接口
        请求方式：POST
        请求地址：/ssm_web/course/findAllCourse
        :return:
        """
        courseList_url = f"{self.base_url}/ssm_web/course/findAllCourse"
        response = self.send("post", url=courseList_url, type='json')
        return response

    def saveOrUpdateCourse(self, course_data):
        saveOrUpdateCourse_url = f"{self.base_url}/ssm_web/course/saveOrUpdateCourse"
        response = self.send("post", url=saveOrUpdateCourse_url, type='json', course_data=course_data)
        return response

