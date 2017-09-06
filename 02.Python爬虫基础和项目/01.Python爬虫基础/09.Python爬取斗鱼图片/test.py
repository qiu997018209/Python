#coding:utf-8

import urllib
from bs4 import BeautifulSoup
import re
'''
f = urllib.urlopen('http://www.douyu.com')
print(f.readline())
print(f.geturl())
print(f.info())
'''
'''
#将url定位到的html文件下载到你本地的硬盘中。
urllib.urlretrieve('https://rpic.douyucdn.cn/acrpic/170906/280072_1441.jpg','./1.jpg')
'''
'''
#使用简单的正则来处理数据
import re
def getHtml(html):
	#(pattern),匹配pattern并获取这一匹配
	#.,匹配除“\n"之外的任何单个字符
	#*,匹配前面的子表达式零次或多次
	#?,匹配前面的子表达式零次或一次,当该字符紧跟在任何一个其他限制符（*,+,?，{n}，{n,}，{n,m}）后面时，匹配模式是非贪婪的。非贪婪模式尽可能少的匹配所搜索的字符串
	imglist = re.findall(r'src="(.*?\.(jpg|png))"',html)
	x=0
	print imglist
	for imgurl in imglist:
		print('正在下载%s'%imgurl[0])
		urllib.urlretrieve(imgurl[0],'./download/%d.jpg'%x)
		x+=1

f = urllib.urlopen('http://www.douyu.com')
htmlcode = f.read()
getHtml(htmlcode)
f.close()
'''

html = """<html><head><title>The Dormouse's story</title></head>
    <body>
    <p class="title" name="dromouse"><b>The Dormouse's story</b></p>
    <p class="story">Once upon a time there were three little sisters; and their names were
    <a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
    <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
    <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
    and they lived at the bottom of a well.</p>
    <p class="story">...</p>"""

soup = BeautifulSoup(html)
'''
打印一下 soup 对象的内容，格式化输出
print soup.prettify()
'''
#方法1:直接打印标签
#获取文字 print soup.b.string
#print soup.p['class']
#print soup.a['href']
#print soup.a.attrs
#方法2:CSS选择器 
#(1)通过标签
#print soup.select('title')
#print soup.select('a')
#(2)通过类名:.代表类
#print soup.select('.sister')
#(3)通过ID:#代表ID
#print soup.select('#link3')
#(4)组合查找:p标签中ID值为link1的内容
#print soup.select('p #link1')
print soup.select('a[class="sister"]')

