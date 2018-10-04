#!/usr/bin/env python
# -*- coding: utf-8 -*-
menu = {'北京':{'海淀':{'五道口':{'soho':{},'网易':{},'google':{}},'中关村':{'爱奇艺':{},'汽车之家':{},'youku':{},},'上地':{'百度':{},},},'昌平':{'沙河':{'老男孩':{},'北航':{},},'天通苑':{},'回龙观':{},},'朝阳':{},'东城':{},},'上海':{'闵行':{"人民广场":{'炸鸡店':{}}},'闸北':{'火车站':{'携程':{}}},'浦东':{},},'山东':{},}
level = menu
save_level = []
while True:
    for place in level:
        print(place)
    choice = input('输入back返回上一级\n输入exit退出\n请输入地名：')
    if choice in level:
        save_level.append(level)
        level = level[choice]
    elif choice == 'back':
        if len(save_level) != 0:level=save_level.pop()
        else:continue
    elif choice == 'exit':exit()
    else:print('请输入正确地名')
        