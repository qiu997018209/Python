#coding=utf-8
import time
#函数
def show_time():
	a=time.time()
	print("%s"%a)
	#将unix时间转化为本地时间
	a=time.localtime(a)
	print("%s"%(a))
	#调整时间格式
	a=time.asctime(a)
	print("%s"%(a))
show_time()
'''
#raw_input输入得到的全是字符串，但是input不是
a = input("请输入数字:")
print("%d"%(a))
print("%f"%(a))
#保留2位小数
print("%.2f"%(a))
'''
#字符串下标使用
name = 'abcdef'
print(name[0])
print(name[0:5:2])


#字符串常见操作
name = '!!!!hello,nice to meet you!!!!'
print(name.find("nice"))
#从指定下标查找
print(name.find("nice",1,5))
#从指定下标开始统计
print(name.count("nice",1,8))
print(len(name))
print(name.replace('h','H'))
#以空格做切分
print(name.split(' '))
#可以控制切几次
print(name.split(' ',1))
print(name.startswith('hello'))

print(name.upper())
#取出首尾的指定字符
print(name.strip('!'))

print(name.index('he'))
#以"——"作为连接符
my_list = name.split(' ')
print("-".join(my_list))
#先将qiu切成list
print("-".join("qiu"))