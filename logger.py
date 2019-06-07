# -*- coding: utf-8 -*-
"""
Created on Fri May 17 14:57:38 2019

@author: T
"""

import logging
import sys

#获取logger实例
logger = logging.getLogger("testLog")
#指定logger格式
formatter = logging.Formatter("%(asctime)s %(levelname)s %(message)s")
#时间-级别-自定义信息
#创建具体的日志handler
file_handler = logging.FileHandler('testLog.log')
file_handler.setFormatter(formatter)
#文件日志、终端日志

#在终端直接输出
console_handler = logging.StreamHandler(sys.stdout)
console_handler.setFormatter(formatter)
#把日志的handler添加到logger实例中


#高于等于默认级别才会被写,发布的时候记得将等级调高
logger.setLevel(logging.DEBUG)
#写日志

logger.addHandler(file_handler)
logger.addHandler(console_handler)

logger.debug('test')

#清空日志handler
logger.removeHandler(file_handler)
logger.removeHandler(console_handler)