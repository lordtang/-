# -*- coding: utf-8 -*-
"""
Created on Thu May 16 11:09:38 2019

@author: T
"""

import hashlib

CHUNKSIZE = 2048
def hashFile(filename):
    hashObj = hashlib.sha256()
    with open(filename,'rb') as f:
        while True:
            chunk = f.read(CHUNKSIZE)
            hashObj.update(chunk)
            if not chunk:
                break
            
    return hashObj.hexdigest()


def hashStr(s):
    hashObj = hashlib.sha256()
    hashObj.update(s.encode('utf-8'))
    return hashObj.hexdigest()


if __name__=="__main__":
    print(hashStr("123456"))
            