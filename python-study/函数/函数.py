a=666
print(str(hex(a)))
#以上为调用内置函数

def my_function(x):
    if x>=0:
        return x
    else:
        return -x
#以上定义函数
print(my_function(-9)) #调用函数
def nop():
    pass
#以上是一个空函数
