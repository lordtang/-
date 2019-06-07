# -*- coding: utf-8 -*-
"""
Created on Wed May 15 20:06:04 2019

@author: T
"""
import hashlib

sign = "hello"
hashObj = hashlib.sha256()
hashObj.update(sign.encode("utf-8"))
print(len(hashObj.hexdigest()))