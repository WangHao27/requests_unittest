# -*- coding: utf-8 -*-
"""
@Auth ： WangHao
@File ：baseApi.py
@Email：whang27@163.com
"""
import requests
import config
from api import log


class BaseApi:
    """
    接口基类封装
    """
    def __init__(self):
        """
        实例化Session(),初始化基础URL
        """
        self.s = requests.Session()
        self.base_url = config.BASE_URL
        self.s.headers = config.BASE_HEADERS

    def get_token(self, phone, password):
        """
        从登录接口获取token
        请求方式：POST
        请求地址：/ssm_web/user/login
        :param phone:
        :param password:
        :return:
        """
        login_url = f"{self.base_url}/ssm_web/user/login"
        response = self.send("post", url=login_url, type='params', phone=phone, password=password)
        token = response['content']['access_token']
        return token

    def send(self, method, url, type=None, **kwargs):
        """
        对传入的请求分类，调用不同的请求方式，作基本的异常处理操作
        :param method: 接口请求方式
        :param url: 请求URL
        :param type: 请求参数类型
        :param kwargs: 请求参数
        :return:
        """
        log.info("********************************* request details *********************************")
        result = ""
        try:
            if method == 'get':
                result = self.s.request('GET', url, params=kwargs)
                log.info("Method    ：GET")
            if method == 'post':
                if type == 'params':
                    result = self.s.request('POST', url, params=kwargs)
                elif type == 'json':
                    result = self.s.request('POST', url, json=kwargs)
                else:
                    result = self.s.request('POST', url, data=kwargs)
                log.info("Method    ：POST")
            if method == 'put':
                result = self.s.request('PUT', url, data=kwargs)
                log.info("Method    ：PUT")

            log.info(f"URL       ：{url}")
            log.info(f"Params    ：{kwargs}")
            log.info(f"Headers   : {self.s.headers} \n")
        except Exception as e:
            log.error(f"{method}请求错误：{e}")
            return e
        if result.status_code in range(400, 504):
            code = result.status_code
            log.error(f"{method}请求错误，响应码：{code}")
        else:
            log.info("********************************* response details *********************************")
            log.info(f"status_code: {result.status_code}")
            try:
                result = result.json()
            except:
                result = result.text
            log.info(f"Response   : {result} \n")
            return result


if __name__ == '__main__':
    res = BaseApi().get_token('15321919666', '123456')
    print(res)