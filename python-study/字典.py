"""
字典分为key部分和value部分，一个key只能对应一个value
多次对一个key放入value，后面的值会把前面的值冲掉
如果key不存在就会报错
"""
d={"laowang":95,"laozhang":66,"laochen":80} #这是一个字典
print(d["laowang"]) #在字典里查找并输出
d["laozhao"]=67 #在字典里面加入内容
print("lao" in d) #通过"in"确定key是否存在
print(d.get("lao")) #通过get()方法确定key是否存在，不存在会返回none
print(d)
