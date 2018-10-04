# -*- encoding: utf-8 -*-
import sys
import json
import requests
import os

def get_data():  #获取json数据
    page_num = 1
    for page_num in range(24):
        page_num = page_num + 1
        url = 'https://api.vc.bilibili.com/link_draw/v2/Photo/list?category=cos&type=hot&page_num=' + str(page_num) + '&page_size=20'
        #上面是构造json的数据地址
        json_data = requests.get(url) #获取
        del_json(json_data.text)  #传入处理函数

def del_json(json_data): #处理json
    frist_json = json.loads(json_data)
    del2_json = frist_json['data']['items']
    for a in del2_json:
        for d in del2_json:
            f = d['item']['pictures']
            for g in f:
                img_src=g['img_src']
                download_img(img_src)
#上面是乱七八糟的处理，我也说不明白了

def download_img(img_src):  #下载图片保存
    img_name=img_src[31:]  #保存文件名
    print('正在下载：'+img_name)
    r = requests.get(img_src, stream=True)
    with open(img_name, 'wb') as fd:
        for chunk in r.iter_content():
            fd.write(chunk)

get_data() #启动