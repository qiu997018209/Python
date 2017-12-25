#闭包
def w1(func):
    def inner():
        print("---正在验证权限----")
        if False:
            func()
        else:
            print("没有权限")
    return inner

#装饰器所起到的作用就是:f1 = w1(f1)
#当用户再次调用f1时，其实f1的内容已经被改变为inner函数
@w1
def f1():
    print("---f1---")

@w1
def f2():
    print("---f2---")

f1()
f2()
