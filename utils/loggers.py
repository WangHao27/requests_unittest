# -*- coding: utf-8 -*-
"""
@Auth ： WangHao
@File ：loggers.py
@Email：whang27@163.com
"""

import logging
import os
import time
import config


# 日志存放路径
log_path = config.TEST_LOG
# 若不存在日志文件就新建一个
if not os.path.exists(log_path):os.mkdir(log_path)

class Logger:

    def __init__(self):
        # 文件的命名
        self.logName = os.path.join(log_path, "%s.run.log" % time.strftime("%Y%m%d%H%M%S"))
        # 日志输出格式
        self.formatter = logging.Formatter(f'%(asctime)s | %(levelname)s | : %(message)s')

    def create_logger(self):
        """
        创建logger并设置日志级别
        :return:
        """
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger

    def create_handler(self):
        """
        创建文件和控制台输出Handler,设置日志输出格式
        :return:
        """
        # 日志输出到文件
        file = logging.FileHandler(self.logName, "a", encoding='utf-8')
        file.setFormatter(self.formatter)
        # 日志输出到控制台
        console = logging.StreamHandler()
        console.setFormatter(self.formatter)

        return file, console

    def add_handler(self):
        """
        添加日志处理器
        :return:
        """
        log_handler = self.create_logger()
        # 防止日志重复输出
        log_handler.handlers.clear()

        log_handler.addHandler(self.create_handler()[0])
        log_handler.addHandler(self.create_handler()[1])
        return log_handler


logger = Logger().add_handler()

if __name__ == "__main__":
    log = Logger().add_handler()
    log.info("--测试开始--")
    log.info("操作步骤1，2,3")
    log.warning("--测试结束--")
    log.error("错误")