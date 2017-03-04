#!/usr/bin/env python
#coding:utf-8
from CreditCard import function_base as fun

fun.show_info(31, '欢迎来到电子商城')

account_name = fun.bank_login()
balance = fun.get_account_balance(account_name)
Break_flag = ''

while 'n' != Break_flag:
    
    print '''\n\t请选择您要进行的操作：\n\t\t\t1.购物 \n\t\t\t2.修改或查看购物车\n\t\t\t3.结账\n\t\t\t4.返回\n'''         
    user_choise = fun.get_user_choice('请输入您的选择:',4,1) 
    if 1 == user_choise:
        #购物
        fun.account_shop()
    elif 2 == user_choise:   
        #修改或查看购物车
        fun.account_shop_car(account_name)
    elif 3 == user_choise:
        #结账
        #显示购物车清单 
        fun.DicTra()            
        fun.user_payment(account_name)
    else:
        #返回主函数
        fun.exit_system()    
            
            