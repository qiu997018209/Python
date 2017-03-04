#!/usr/bin/env python
#coding:utf-8

#本模块负责处理网上银行
from CreditCard import function_base as fun


#打印欢迎信息
fun.show_info(32,'''欢迎来到网上银行''')
#银行用户登陆
user_name = fun.bank_login()

Break_flag = ''

while 'n' != Break_flag and user_name:
    
    print '''\n\t请选择您要进行的操作：\n\t\t\t1.取现 \n\t\t\t2.查询\n\t\t\t3.还款\n\t\t\t4.转账\n\t\t\t5.返回\n''' 
    #获取用户的输入
    user_choise = fun.get_user_choice('请输入您的选择:',5,1)
    if 1 == user_choise:
        cash_num = fun.get_account_cash(user_name)
        if cash_num:
            #记录消费明细
            fun.record_consume_list(user_name,cash_num,'取现')            
        #是否退出循环
        Break_flag = fun.BreakFlag()
    elif 2 == user_choise:
        #查询
        print '''\n\t请选择您要进行的操作：\n\t\t\t1.查询余额\n\t\t\t2.查询最近30日的消费明细\n''' 
        #获取用户的输入
        user_choise = fun.get_user_choice('请输入您的选择:',2,1) 
        if 1 == user_choise:
            #显示余额
            fun.show_account_balance(user_name)
        else:
            #显示消费明细
            fun.show_consume_list(user_name)
        #是否退出循环
        Break_flag = fun.BreakFlag()      
    elif 3 == user_choise:
        #还款
        repay_num = fun.push_account_cash(user_name)
        if repay_num > 0:
            #记录消费明细
            fun.record_consume_list(user_name,repay_num,'还款')            
        #是否退出循环
        Break_flag = fun.BreakFlag() 
    elif 4 == user_choise:
        #转账
        other_name,transfer_num = fun.transfer_account_cash(user_name)
        if other_name and transfer_num:
            #生成消费明细
            fun.record_consume_list(user_name,transfer_num,'转账') 
            fun.record_consume_list(other_name,transfer_num,'转账') 
        #是否退出循环
        Break_flag = fun.BreakFlag()        
    else:
        #返回主函数
        fun.exit_system()
        break
else:
    #返回主函数
    fun.exit_system()                 
    