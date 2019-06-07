# -*- coding: utf-8 -*-
"""
Created on Fri May 17 15:57:35 2019

@author: T
"""
import sys
import logging

class LoggerHelper(object):
    def __init__(self,name):
        self.name=name
        self.logger = logging.getLogger("testLog")
        formatter = logging.Formatter("%(asctime)s %(levelname)s %(message)s")
        
        self.file_handler = logging.FileHandler('testLog.log')
        self.file_handler.setFormatter(formatter)
        
        self.console_handler = logging.StreamHandler(sys.stdout)
        self.console_handler.setFormatter(formatter)
    
    def write_log(self,message,level=logging.DEBUG):
        self.logger.setLevel(level)
        self.logger.addHandler(self.file_handler)
        self.logger.addHandler(self.console_handler)
        
        if self.name=="error":
            self.logger.error(message)
        elif self.name=='debug':
            self.logger.debug(message)
        elif self.name=='info':
            self.logger.info(message)
        else:
            print("name值错误")
    
    def remove_log(self):
        self.logger.removeHandler(self.file_handler)
        self.logger.removeHandler(self.console_handler)
        
if __name__ == '__main__':
    logger = LoggerHelper('error')
    logger.write_log('test info ')
    logger.remove_log()
    
    