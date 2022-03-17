# -*- coding: utf-8 -*-
"""
@Auth ： WangHao
@File ：login_api.py
@Email：whang27@163.com
"""
import config
from api.common.baseApi import BaseApi


class LoginApi(BaseApi):

    def __init__(self):
        super().__init__()
        self.s.headers = config.BASE_HEADERS

    def login(self, phone, password):
        """
        拉勾教育前台登录接口
        请求方式：POST
        请求地址：/ssm_web/user/login
        :param phone:
        :param password:
        :return:
        """
        login_url = f"{self.base_url}/ssm_web/user/login"
        response = self.send("post", url=login_url, type='params', phone=phone, password=password)
        return response