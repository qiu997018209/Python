#coding:utf-8

class animal:
	def __init__(self):
		self.age = 10
		self.sex = "man"
		print ("animal的构造函数")
	def __del__(self):
		print ("animal的析构函数")
	def run(self):
		print ("animal的run")
#继承
class cat(animal):
	#重写了父类的__init__,此处与C++不一样
	def __init__(self):
		self.age = 20
		self.sex = "woman"
		#调用父类的函数,需要加参数self
		animal.__init__(self)
		print ("cat的构造函数")	
	def __del__(self):
		print ("cat的析构函数")	

	def catch(self):
		print ("抓鱼")	


cat=cat()

#多继承:多继承函数重名，按照继承顺序从左到右查找，找到了就不再继续找了,如果C自己有，那么优先找自己的
class A:
	def test1(self):
		print ("test1")
	def test(self):
		print ("test in A")	
class B:
	def test2(self):
		print ("test2")	
	def test(self):
		print ("test in B")

class C(A,B):
	pass

c = C()
c.test1()
c.test2()
c.test()

#多态:Python是弱类型语言,几乎是感觉不到多态的存在
class D:
	def show(self):
		print ("D.show")
class E(D):
	def show(self):
		print ("E.show")
class F(D):
	def show(self):
		print ("F.show")	
#弱类型,因此感觉不到多态的存在
def show(obj):
	obj.show()

f = F()
e = E()
show(e)
show(f)

#当子类没有构造函数的时候，默认是去调父类的构造函数的