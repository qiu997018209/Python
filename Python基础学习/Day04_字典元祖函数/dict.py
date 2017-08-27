#coding=utf-8

#字典
info = {'name':'qiu','age':18,'sex':'man'}
print(info['name'])
#字典的常见操作
del info['name']
print(info)
#可直接删除字典del info 
#清空
info.clear()
print(info)

info = {'name':'qiu','age':18,'sex':'man'}
print(len(info))
print(info.keys())
print(info.values())
#将每一个键值对以元祖返回
print(info.items())
print(info.has_key('age'))

for key in info.keys():
	print key
for value in info.values():
	print value
for item in info.items():
	print item
for key,value in info.items():
	print key,value