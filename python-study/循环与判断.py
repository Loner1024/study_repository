height = int(input("请输入身高cm"))*0.01
weight = int(input("请输入体重"))
bml =weight/height**2
print(bml)
if bml<18.5:
    print("过轻")
elif 18.5 < bml < 25 :
    print("正常")
elif bml>=25 and bml<28:
    print("过重")
elif bml>=28 and bml<32:
    print("过重")
elif bml>=32:
    print("严重肥胖")

#计算BML指数并判断