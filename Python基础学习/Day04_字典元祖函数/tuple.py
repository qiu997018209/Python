#coding:utf-8
tuple2 = ("hello",100,99)
print(tuple2)

#修改:元祖中的元素不允许修改,删除
#tuple[1] = 10
print(tuple2)
#合并
tuple1=("nice",1)
print(tuple2+tuple1)
#del tuple[1]
#print(tuple)
#
print(100 in tuple2)
for value in tuple2:
	print value

print(tuple2[-1])
print(tuple2[1:])

print((1,2)*4)

#元祖的内置函数
print cmp(tuple2,tuple1)
print max(tuple2)
#将列表转化为元祖
li = [1,2]
print (tuple(li))