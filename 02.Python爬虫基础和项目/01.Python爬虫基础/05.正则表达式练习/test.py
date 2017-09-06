#coding:utf-8
import re

#3位数字-3到8个数字  \d{3}-\d{3,8}
mr = re.match(r'\d{3}-\d{3,8}','010-223456')
print mr.string

#分组
mr = re.match(r'(\d{3})-(\d{3,8})$','010-223456')
print mr.groups()
print mr.group(0)
print mr.group(1)
print mr.group(2)

#处理时间
t = '20:15'
mr = re.match(r'^(0[0-9]|1[0-9]|2[0-3]|[0-9])\:(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|6[0-9])',t)
print mr.group(1)
print mr.group(2)

#分割字符串:以数字作为分隔符
p = re.compile(r'\d+')
print(p.split('one1two22three3333'))