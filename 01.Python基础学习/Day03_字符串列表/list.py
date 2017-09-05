#coding=utf-8

#列表

names = ["qiu","jia","hao"]

lenth = len(names)
i=0
while i < lenth:
	print(names[i])
	i+=1

for i in names:
	print(i)

#列表的相关操作
#增
names.append("china")
print(names)
#删
index = raw_input("请输入删除的字符串序号:")
index = int(index)
del names[index]
print(names)
#删除最后一个
names.pop()
print(names)
index = raw_input("请输入删除的字符串:")
if index in names:
	names.remove(index)
	print(names)