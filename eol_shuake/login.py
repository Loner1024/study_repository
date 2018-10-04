#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests
import time
import getpass
usename=input('请输入学号：')
password= getpass.getpass('请输入密码：')
print(password)
class_url=input('请输入要刷的课程地址：')
t=input('输入课程刷新的间隔（单位：秒）：')
jg=int(t)
def start(): #
    url='http://eol.shzu.edu.cn/meol/loginCheck.do'
    data={
    'logintoken': '1525515101110',
    'IPT_LOGINUSERNAME': usename,
    'IPT_LOGINPASSWORD': password
    }
    s = requests.Session()
    s.post(url,data)
    r = s.get(class_url).text
    #print(r)
def t(t):
    n=0
    while True:
        start()
        n=n+1
        print('已循环'+str(n)+'次')
        time.sleep(t)
t(jg)
