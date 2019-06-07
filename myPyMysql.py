# -*- coding: utf-8 -*-
"""
Created on Fri May 17 16:54:47 2019

@author: T
"""

import pymysql
import myLogger

class DBHelper(object):
    def __init__(self,
                 host="127.0.0.1",
                 user="root",
                 pwd="123456",
                 port=3306,
                 charset='utf8',
                 db = 'maoyan'
                 ):
        self.host = host
        self.user=user
        self.pwd=pwd
        self.port=port
        self.charset = charset
        self.db=db
        self.cur = None
        self.conn = None
    
    def connDatabase(self):
        try:
            self.conn = pymysql.connect(host=self.host,user = self.user,password = self.pwd,db = self.db,charset = self.charset,port = self.port)
        except:
            return False
        self.cur = self.conn.cursor()
        return True
    
    def execute(self,sql,params=None):
        if self.connDatabase()==False:
            return False
        try:
            if self.conn and self.cur:
                self.cur.execute(sql,params)
                self.conn.commit()
        except Exception as e:
            print(e)
            print('excute: '+sql+'error')
            return False
            
        return True
            
    
    def close(self):
        if self.cur:
            self.cur.close()
        if self.conn:
            self.conn.close()
    
if __name__ == '__main__':
    dbhelper = DBHelper()
    sql = "INSERT INTO `maoyan`.`maoyan_top` ( `name`, `star`, `releasetime`) VALUES (%s,%s,%s);"
    params = ('一人','tang','2017-1-5')
    dbhelper.execute(sql,params=params)
    