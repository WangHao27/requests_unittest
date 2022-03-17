# -*- coding: utf-8 -*-
"""
@Auth ： WangHao
@File ：fileUtils.py
@Email：whang27@163.com
"""

import csv
import json
import os
from json import JSONDecodeError
import yaml
from yaml.parser import ParserError
from yaml.scanner import ScannerError
from yamlinclude.constructor import YamlIncludeConstructor
import config
from utils import log


# 用于yaml文件嵌套
YamlIncludeConstructor.add_to_loader_class(loader_class=yaml.FullLoader)
PATH = lambda p: os.path.abspath(os.path.join(os.path.dirname(__file__), p))

class FileUtils:
    """
    文件读取与写入工具类，处理一些解析异常
    """

    def __init__(self, filePath):
        """
        文件路径初始化
        """
        if os.path.isfile(PATH(filePath)):
            self.file = PATH(filePath)
        else:
            raise FileNotFoundError("文件不存在")


    def read_yaml(self):
        """
        读取yaml文件数据
        :return:
        """
        try:
            with open(self.file, 'r', encoding='utf-8') as f:
                data = yaml.safe_load(f)
                f.close()
            return data
        except (ScannerError, ParserError) as error:
            log.error(f"yaml文件格式存在问题，请检查：{type(error)}：{error}")

    def read_yaml_byTuple(self, find=None):
        """
        读取yaml文件数据，按照[(1,2),(2,3),(4,5)]格式输出
        :return:
        """
        try:
            with open(self.file, 'r', encoding='utf-8') as f:
                if find is None:
                    data = yaml.safe_load(f)
                else:
                    data = yaml.safe_load(f)[find]
                result = []
                for case_data in data:
                    result.append(tuple(case_data))
                f.close()
            return result
        except (ScannerError, ParserError) as error:
            log.error(f"yaml文件格式存在问题，请检查：{type(error)}：{error}")

    def write_yaml(self, message):
        """
        数据写入yaml文件
        :param message:
        :return:
        """
        if type(message) == dict:
            # 此模式为追加模式,若想直接重写则将open函数中的模式'a+'改为'w'
            with open(self.file, "a+", encoding="utf-8") as f:
                yaml.dump(message, f)
            f.close()
        else:
            log.error("非字典类型的数据！")

    def read_json(self):
        """
        读取json文件数据
        :return:
        """
        try:
            with open(self.file, 'r', encoding='utf-8') as f:
                data = json.load(f)
                f.close()
            return data
        except JSONDecodeError as error:
            log.error(f"json文件格式存在问题，请检查：{type(error)}：{error}")

    def write_json(self, message):
        """
        json文件的数据写入
        :param message:
        :return:
        """
        if type(message) in (str, dict, list):
            with open(self.file, 'w', encoding="utf-8") as j:
                json.dump(message, j, ensure_ascii=False)
        else:
            log.error("非字典或列表类型的数据！")

    def write_csv(self, headers, rows):
        """
        数据格式：
        表头(列表)[key1, key2, ...]，
        行(列表嵌套字典)[{'key1': 'val1', 'key2': 'val2'}，{...}, ...]
        :param headers:
        :param rows:
        :return:
        """
        if type(headers) and type(rows) in (str, list):
            with open(self.file, "w", encoding='utf-8', newline="") as w:
                writer = csv.DictWriter(w, headers)
                writer.writeheader()
                writer.writerows(rows)
                w.close()
        else:
            log.error("非列表类型数据！")

if __name__ == '__main__':
    # login_data = os.path.join(config.TEST_DATA, "login_test.yaml")
    # file = FileUtils(login_data).read_yaml_byTuple("login_test")
    # print(file)
    course = os.path.join(config.TEST_DATA, "saveCourse_test.json")
    file2 = FileUtils(course).read_json()
    print(file2)