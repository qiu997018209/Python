#coding:utf-8
f=open("1.txt",'w')
f.write('test by qiu\nhello world\n')
f.close()
'''
r不创建新文件
w会创建新的
a追加,会创建文件
r+,读写,文件指针在文件开头,必须存在文件(+号代表增加写,其余与r一样)
w+,读写,会创建新的文件(+号代表增加读,其余与w一样)
a+,读写,会创建新的文件(+号代表增加读,其余与a一样)
'''
f=open("1.txt",'r')

print(f.read(4))
print(f.read(4))

f.seek(0)
print(f.readlines())
f.close()
#删除,重命名文件
import os
os.rename("1.txt","2.txt")
os.remove("2.txt")


#批量重命名文件
try:
	os.mkdir('movies')
except NameError:
	print "我是except"
#存在异常,但是没有捕捉到时,不会走else
else:
	print "我是else"
finally:
	print "我是finally"



name = os.listdir('./movies')
for temp in name:
	os.rename(temp,"2.txt")

print os.getcwd()

print os.listdir('./')
