#!/usr/bin/env python

# -*- coding: utf-8 -*-

import json


goods = [{"no":0,"name": "电脑", "price": 1999},{"no":1,"name": "鼠标", "price": 10},{"no":2,"name": "游艇", "price": 20},{"no":3,"name": "美女", "price": 998}]

buy_list = []

with open('user_data.txt','r') as f:
	user_data = json.loads(f.read())  #从文件中读取用户数据
while True:
	username = input('输入用户名：')
	if username not in user_data:
		print('请输入正确用户名')
	else:
		user_now_data = eval(user_data[username])
		password = input('输入密码：')
		if password == user_now_data['password']:
			money = int(input('请输入你的工资：'))
			while True:
				print('您的当前余额为：',user_now_data['money'])
				print('输入编号来购买商品，输入q退出，输入c查询')
				print('——————商品目录——————')
				print('编号', '名称', '价格')
				for good in goods:
					print(good['no'], good['name'], good['price'])
				buy = input('输入你想要的商品编号：')
				if buy == 'q':
					exit()
				elif buy == 'c':
					print('你好，',username)
					print('你的当前余额为：',user_now_data['money'])
					print('你购买过这些东西：')
					for i in list(user_now_data['buy']):
						print(goods[i]['name'])
				else:
					money = money - goods[0]['price']
					if money < 0:
						print('余额不足')
						exit()
					else:
						buy_list.append(int(buy))
						user_now_data['buy'] = buy_list
						user_now_data['money'] = money
						user_data[username] = user_now_data
						print(user_data)
						continue
		else:
			print('密码错误')

