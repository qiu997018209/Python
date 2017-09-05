#coding:utf-8
def show():
	print "this is show functiion"

def show2():
	print "this is show2 functiion"

def main():
	show()
	show2()
#自己执行时显示main,别人调用时显示文件名
if __name__ == '__main__':
	main()