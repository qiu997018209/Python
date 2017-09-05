#coding:utf-8

#自己定义一个异常类
class ShortInputException(Exception):
	def __init__(self,length,atleast):
		Exception.__init__(self)
		self.length = length
		self.atleast = atleast
try:
	s = raw_input("请输入-->")
	if len(s) < 3:
		#引发一个异常
		raise ShortInputException(len(s),3)
except EOFError:
	print '/n你输入了一个结束标记符EOF'
except ShortInputException,x:#x这个变量被绑定到了错误的实例
	print ('ShortInputException:输入的长度是%d,长度至少是%d'%(x.length,x.atleast))
else:
	print "异常没有发生"