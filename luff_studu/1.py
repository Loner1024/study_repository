import json
user_info={'user1':'password1','user2':'password2','user3':'password3'}
with open('allow_status.txt','r') as f:
	allow_status=json.loads(f.read())
i=0
while i<3:
	i=i+1
	username=str(input('请输入用户名：'))
	if username in user_info:
		if allow_status[username]==0:
			print('你的账户已锁定')
			exit()
		else:
			password=str(input('请输入密码：'))
			if user_info[username]==password:
					print('欢迎回来,',username)
			else:
				print('密码错误!')
	else:
		print('用户不存在')
else:
	print('尝试次数过多！')
	allow_status[username]=0
	with open('allow_status.txt','wb') as f:
		f.write(json.dumps(allow_status).encode('utf-8'))
	exit()