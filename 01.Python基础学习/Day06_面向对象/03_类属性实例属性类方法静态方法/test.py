#coding:utf-8

class Test:
	#类属性
	num = 100
	time = "old"
	def __init__(self):
		#实例属性
		self.age = 20
	#实例方法 
	def show_age(self):
		print "age is %d"%self.age
	def show_num(self):
		print "num is %d"%self.num
	#类方法
	@classmethod
	def Set_Num(cls,num):
		cls.num = num
	#静态方法,可以没有参数
	@staticmethod
	def test():
		print('静态方法%s'%time)
	@classmethod
	def show_Time(cls):
		print('类方法时间:%s'%cls.time)

test_1 = Test()
test_1.age = 30
test_1.show_age()
test_1.show_num()

#如果通过实例来访问一个与类属性一样的变量，那么这个时候实例会创建一个一样的实例变量
test_1.num = 1
#显示实例属性,优先于类属性
test_1.show_num()
del test_1.num
#显示类属性
test_1.show_num()

#改变类属性
Test.num = 200
test_2 = Test()
test_2.show_num()

#测试类方法与类属性
print '...........测试类方法与类属性.......'
test_3 = Test()
#不可改变类属性
test_3.num = 200
test_3.show_num()
print "类属性:%d"%Test.num
#使用类方法:可改变类属性
Test.Set_Num(500)
print "类属性:%d"%Test.num
#实例对象可以调用类方法改变类属性,类不能直接调用实例方法
test_3.Set_Num(5)
print "类属性:%d"%Test.num

print '...........测试静态方法.......'
#静态方法实例和类均可调用
Test.test()
test_3.test()
print '...........静态方法与类方法的区别.......'
#区别:类方法可以访问类成员,静态方法不可以，类方法有继承的概率，静态方法没有
#在C++中静态方法等于类方法
#在python中类方法必须有cls参数，静态方法可以什么都没有
#那么在继承的时候,子类的cls可以直接指向子类
class Test2(Test):
	time = "now"

Test2.show_Time()

