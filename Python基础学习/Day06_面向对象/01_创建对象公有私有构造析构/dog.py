#coding:utf-8


class dog:
	#属性:公有
	color = "红色"
	#属性:私有
	__age = 15
	#构造
	def __init__(self):
		self.price = "10"
		print "构造函数被调用"
	#析构
	def __del__(self):
		print "析构函数被调用"
	#方法
	def SetColor(self,dog_color):
		self.color = dog_color
	def run(self):
		print ("%s的狗在run"%self.color)
	def GetAge(self):
		return self.__age
	#私有方法
	def __SetPrice(self):
		self.price = 100
		print ("Price is %d"%self.price)

	def SetPrice(self):
		self.__SetPrice()
d=dog()
d.SetColor("绿色")
d.run()
print (d.GetAge())
d.SetPrice()