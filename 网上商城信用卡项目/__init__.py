#!/usr/bin/env python
#coding:utf-8

#函数主入口

from function_base import im
import os
#程序开始时，创建临时测试账户
fun.create_account_info()

while True:
    try:
        print '''\n\t\n\t\t\t\033[31;1m1.网上银行 \n\t\t\t2.购物商城\n\t\t\t3.退出\033[1m\n''' 
        account_choice = fun.get_user_choice("请选择您要进行的操作:",3,1)
        #用户选择1，进行网上银行
        if 1 == account_choice: 
           #os.system('python Internet_bank.py') 
           import Internet_bank
        #用户选择2，进入购物商城
        elif 2 == account_choice:
           #os.system('python shopping.py') 
           import shopping 
        else:
            #退出系统
            fun.exit_system()
    except:
        #输入错误,打印提示信息
        continue   