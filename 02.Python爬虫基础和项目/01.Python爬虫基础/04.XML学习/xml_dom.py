#coding:utf-8
from xml.dom import minidom

doc = minidom.parse('book.xml')
#拿到根节点
root = doc.documentElement
print (type(root))
print (root.nodeName)
#查看方法
#print (dic(root))
books = root.getElementsByTagName('book')

for book in books:
	#继续获取下一层节点
	title = book.getElementsByTagName('title')
	print title[0].childNodes[0].nodeValue
