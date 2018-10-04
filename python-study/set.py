'''
set和dict类似，也是一组key的集合，但不存储value。由于key不能重复，所以，在set中，没有重复的key。
'''
s=set([1,2,3,4,5,1,1,1]) #创建set，需要输入一个list作为集合,重复元素将被自动过滤
print(s)
s.add(6) #通过add(key)添加元素
print(s)
s.remove(6) #通过remove()移除元素
print (s)
print("————————————————————————")
'''
set可以看成数学意义上的无序和无重复元素的集合，因此，两个set可以做数学意义上的交集、并集等操作：
'''
s1=set([1,2,3])
s2=set([3,4,5])
print(s1&s2) #求交集
print(s1|s2) #求并集