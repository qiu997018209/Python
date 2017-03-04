#!/usr/bin/env python
#coding:utf-8
import time
import pickle
import os
#本模块提供函数调用库
#按照用户名-密码-余额格式,每个开通信用卡的人默认额度位15000元
account_dict = {'测试1':[123,15000],'测试2':[456,15000]}
#被锁住的用户
account_lock = []
#记录用户的消费明细，按照名字-时间-类型-金额
account_consume_list = {}

#打印提示信息
def show_info(clolor,print_info):
    print '''\t\t\033[%d;1m%s\033[0m'''%(clolor,print_info) 

#在Bank_infoBase里生成账户信息，通过pickle序列化功能，提供简单加密功能
def create_account_info(): 
    show_info(33,'''\n\t\t\033测试程序,创建银行账户，账户名为:测试1，密码为:123，余额为15000\033[0m\n''')
    pickle.dump(account_dict,open('Bank_infobase.txt','w'))
    pickle.dump(account_lock,open('Bank_lock.txt','w'))
    pickle.dump(account_consume_list,open('consume_list.txt','w'))
#获取当前账户信息    
def get_account_info():
    return pickle.load(open('Bank_infobase.txt','r'))

#设置当前账户余额
def set_account_balance(account_name,balance):
    account = pickle.load(open('Bank_infobase.txt','r'))
    account[account_name][1] = balance
    pickle.dump(account,open('Bank_infobase.txt','w'))
    
#显示余额
def show_account_balance(account_name):
    account = pickle.load(open('Bank_infobase.txt','r'))
    show_info(32,'您当前的余额为:%d'%(account[account_name][1]))
    
#获取当前余额
def get_account_balance(account_name):
    account = pickle.load(open('Bank_infobase.txt','r'))
    return account[account_name][1]
               
#查看当前用户是否被锁定
def check_account_islock(user_name):
    account = pickle.load(open('Bank_lock.txt','r'))
    if account.count(user_name):
        return True
    else:
        return False
#查看当前用户是否存在
def check_account_isexit(user_name):
    account = pickle.load(open('Bank_infobase.txt','r'))
    if account.has_key(user_name):
        return True
    else:
        return False
#将当前用户锁定
def set_account_lock(user_name):
    if not check_account_islock(user_name):
        account = pickle.load(open('Bank_lock.txt','r'))
        account.append[user_name]
        pickle.dump(account,open('Bank_lock.txt','w'))
        
#银行用户登陆
def bank_login():
    show_info(32,'''请先登陆''')
    while True: 
        Account = raw_input('请输入您的账户:')
        Password = get_user_choice('请输入您的密码:',99999999,1)         
        #检查用户是否被锁住
        if check_account_islock(Account):
            show_info(32,'''此账户已经被锁定，请拿本人身份证取银行柜台解锁！''') 
            if 'n'== BreakFlag():
               #退出系统
               exit_system()
            else:
                continue   
        #读取数据库里的账户信息
        account_info = get_account_info()
        for i in range(3):
            if account_info.has_key(Account): 
                if account_info[Account][0] == Password:
                    show_info(32,'''登陆成功''')
                    return Account
                elif i != 2:
                    show_info(32,'''密码错误，您还有%d次机会'''%(2-i))
                    break
                else:
                    #账户被锁定
                    set_account_lock(Account)
                    if 'n'== BreakFlag():
                       #退出系统
                       exit_system()
                    else:
                        continue
            else:
                show_info(32,'''账户不存在，请重新输入''')
                break
                
#是否需要退出循环
def BreakFlag():
    while True:
        Flag = raw_input('是否需要继续y/n:')
        if Flag =='y'or Flag =='n':
            return Flag
        else:
            print '输入错误，请输入y/n！'
#打印指定的信息并获取用户的选择
def get_user_choice(print_info,max,min):
    while True:
        try:
            user_choice = int(raw_input("%s"%(print_info)))
            if user_choice < min or user_choice > max:
                show_info(32,'输入错误，请输入正确的数值')
            else:
                return user_choice  
        except:
            show_info(32,'输入错误，请输入正确的数值')
#取现
def get_account_cash(account_name):
    account = pickle.load(open('Bank_infobase.txt','r'))
    show_account_balance(account_name)
    cash_num = get_user_choice('请输入您要取现的额度:',get_account_balance(account_name),1)
    if (cash_num * 1.05) > account[account_name][1]:
        show_info(34, '对不起，您的余额不足！')
        return 0
    elif cash_num * 0.05 < 1:
        cash_num = cash_num + 1
        account[account_name][1] -= cash_num
        show_info(34, '取现成功，收您手续费：%d！'%(1))
    else:
        account[account_name][1] -= cash_num * 1.05 
        show_info(34, '取现成功，收您手续费：%d！'%(cash_num * 0.05)) 
        cash_num = cash_num * 1.05       
    #最新信息记录到文件中    
    pickle.dump(account,open('Bank_infobase.txt','w'))
    return cash_num
#还款
def push_account_cash(account_name):
    account = pickle.load(open('Bank_infobase.txt','r'))
    #欠款额度为：
    own_num = 15000 - account[account_name][1]
    #考虑到转账功能，用户余额可能超过15000
    if own_num <= 0:
        show_info(34, '本月欠款已还清，无需还款！')
        return 0
    else:
        show_info(34, '本月欠款额度为：%d'%(own_num))
        
    user_choise = get_user_choice('请输入您想还款的额度:',own_num,1)
    account[account_name][1] += user_choise 
    own_num -= user_choise
    #写入数据库
    pickle.dump(account, open('Bank_infobase.txt','w'))
    show_info(34, '还款成功，本月欠款额度为：%d'%(own_num))
    return user_choise 
#转账
def transfer_account_cash(account_name):
    #显示余额
    show_account_balance(account_name)
    balance = get_account_balance(account_name)    
    while True:
        other_name = raw_input('请输入转账人的名字:')
        if not check_account_isexit(other_name):
            show_info(31,"用户不存在，测试版本可以使用用户名：测试2") 
            continue
        elif other_name == account_name:
            show_info(31,"请不要转账给自己") 
            continue            
        transfer_num = get_user_choice('请输入想转账的金额:',balance,1)
        if transfer_num > balance:
            show_info(31,"余额不足！")
            continue
        else:
            #设置转账人的余额
            set_account_balance(other_name,get_account_balance(other_name) + transfer_num)
            #设置自己的余额
            set_account_balance(account_name,balance - transfer_num)
            show_info(31,"转账成功！")
            return other_name,transfer_num

#获取当前时间
def get_local_time():
    return time.strftime("%Y-%m-%d-%H-%S")    
#记录消费明细
def record_consume_list(user_name,user_num,user_type):
    #读取数据库
    consume_list = pickle.load(open('consume_list.txt','r')) 
    if consume_list.has_key(user_name):
        consume_list[user_name]['%s'%(get_local_time())] = {'类型':user_type,'金额':user_num}
    else:
        consume_list[user_name] = {
            '%s'%(get_local_time()):{'类型':user_type,'金额':user_num}}
    #写入数据库
    pickle.dump(consume_list,open('consume_list.txt','w'))

#显示最近30天的消费明细
def show_consume_list(account_name):
    consume_list = pickle.load(open('consume_list.txt','r'))    
    #显示格式为：时间：类型：金额
    if consume_list:
        for i in consume_list[account_name].keys():
            print '时间:%s 类型：%s 金额：%d'%(i,consume_list[account_name][i]['类型'],consume_list[account_name][i]['金额'])    
    else:
        show_info(33, '最近30天无消费记录')
#退出系统  
def exit_system():
    for i in range(3):
        print '''\n\t\t\t\033[34;5m系统将于%s秒后退出！\033[0m'''%(3-i)
        time.sleep(1)   
    exit()  
    
    
    
    
    
    
'''以上是网上银行的库函数，以下是购物商场的库函数'''
#商城物品清单
shop_list = {'mac':5888,'bike':200,'car':10000,'clothes':500}
#购物车
shop_car = {}

#显示商品清单
def show_shop_list():
    for x,y in shop_list.items():
        print '\t\t\t%s:%d'%(x,y)

#商品是否存在
def goods_existed(shop_dict,choose_good):
    if shop_dict.has_key(choose_good):
       return True
    else:
        show_info(31,'没有这项商品，请输入正确的商品名称！')
        return False 
#显示购物车清单 
def DicTra(): 
        if not shop_car.values():
            #说明购物车是空的
            show_info(31,'您没有购买任何物品')  
        else:
            #显示购物车内容
            print '''\n\t\t\t\033[31;1m您购买的商品为：\033[0m\033[32;1m商品名称 商品数量 商品总价\033[0m'''
            for i in shop_car:
                print '''\n\t\t\t\t\t%s  \t%d   \t%d'''%(i,shop_car[i][0],shop_car[i][1])

#将指定商品删除出购物车并显示当前购物车内容
def remove_shop_car(goods_name):
        if goods_existed(shop_car,goods_name):
            shop_car.pop(goods_name) 
            
#计算购物车商品总价  
def count_total_price():
    if shop_car:
        for i in shop_car:
            return shop_car[i][0]*shop_car[i][1] 
    else:
        return 0    
#结账
def user_payment(account_name):
    #计算商品总价
    totai_num = count_total_price()
    if totai_num:
        #获取账户余额
        balance = get_account_balance(account_name)
        if totai_num <= balance:
            set_account_balance(account_name,balance-totai_num)
            #将购物车清零
            shop_car.clear()
            #生成消费明细
            record_consume_list(account_name,totai_num,'消费')
            show_info(35, '付款成功！')
            #返回主函数
            exit_system()
        else:
            show_info(35, '账户余额不足')          
#购物
def account_shop():
    Break_flag =''
    while Break_flag != 'n':
        #打印购物清单
        show_shop_list()
        choose_good = raw_input('请输入您想购买的商品:')
        #检查商品是否存在
        if goods_existed(shop_list,choose_good):            
            #检查购物车是否有同类商品，如果有，将数量加1,并增加该商品的总价
            #如果没有同类商品，则在购物车中新建
            if shop_car.has_key(choose_good):
                shop_car[choose_good][0] += 1
                shop_car[choose_good][1] += shop_list[choose_good]
            else:
                shop_car[choose_good] = [1,shop_list[choose_good]]
            show_info(35, '已成功加入购物车')
            
        Break_flag = BreakFlag()                        

#查看并修改购物车：
def account_shop_car(account_name):
    
    print '''\n\t请选择您要进行的操作：\n\t\t\t\t1.增加商品\n\t\t\t\t2.减少商品\n\t\t\t\t3.结账\n\t\t\t\t4.返回'''
    
    Shopping_Car_Choose = get_user_choice('请输入您的选择:',4,1)                 
    Break_flag = ''            
    if 1 == Shopping_Car_Choose:
        #用户想增加商品数量
        while Break_flag != 'n':
            #显示购物车清单
            DicTra()
            if shop_car:
                Shopping_Car_Modify = raw_input('\n\t\t请输入您想增加的商品名称：')
                #检查商品是否存在
                if goods_existed(shop_car,Shopping_Car_Modify):
                    Shopping_Car_Num = get_user_choice('请输入您增加的商品数量:',99999999,1)                                
                    shop_car[Shopping_Car_Modify][0] += Shopping_Car_Num
                    shop_car[Shopping_Car_Modify][1] = shop_car[Shopping_Car_Modify][0] * shop_list[Shopping_Car_Modify]
            #用户是否想继续
            Break_flag = BreakFlag()

        #用户想减少商品数量        
    elif 2 == Shopping_Car_Choose:
        while Break_flag != 'n':
            #显示购物车清单
            DicTra()
            if shop_car: 
                Shopping_Car_Modify = raw_input('\n\t\t请输入您想减少的商品名称：')
                #检查商品是否存在
                if goods_existed(shop_car,Shopping_Car_Modify):
                    Shopping_Car_Num = int(raw_input('\n\t\t请输入您想减少的商品数量：'))
                    #修改的数量必须小于等于当前的商品数量
                    if Shopping_Car_Num >= 0 and Shopping_Car_Num <= shop_car[Shopping_Car_Modify][0]:                           
                        shop_car[Shopping_Car_Modify][0] -= Shopping_Car_Num
                        shop_car[Shopping_Car_Modify][1] = shop_car[Shopping_Car_Modify][0]*shop_list[Shopping_Car_Modify]
                        #如果数量为0，需要从购物车中清除
                        if 0 == shop_car[Shopping_Car_Modify][0]:
                            remove_shop_car(Shopping_Car_Modify)                                    
            Break_flag = BreakFlag()
    #用户想结账
    elif 3 == Shopping_Car_Choose:
        #打印购物清单
        DicTra()
        user_payment(account_name)                
        Break_flag = BreakFlag()    
    else:
        return 
     