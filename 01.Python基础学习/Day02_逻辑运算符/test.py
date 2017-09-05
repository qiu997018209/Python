#coding=utf-8

#if使用
age = 6
if age > 18 and age < 80:
	print("满足条件")
elif age <= 6 or age>90:
	print("满足部分条件")
else:
	print("不满足条件")

#while使用
i = 0
while i<3:
	print("while第%d次"%i)
	i+=1
	if(i==1):
		break
#for的使用:range是0到9
for i in range(10):
	if(i==2):
		break
	else:
		print("for第%d次"%i)
		continue