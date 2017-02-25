#!/usr/bin/env python
#coding:utf-8
import time

#用户数字输入错误，提示信息
def show_wrong_number_info():
    print '''\t\t\033[31;1m输入错误，请输入正确的数值！\033[0m'''
#显示商品清单
def show_shop_list():
    for x,y in shop_list.items():
        print '\t\t\t%s:%d'%(x,y)
def exit_system():
    for i in range(3):
        print '''\n\t\t\t\033[34;5m系统将于%s秒后退出！\033[0m'''%(3-i)
        time.sleep(1)
    exit()            
#商品是否存在
def goods_existed(shop_dict,choose_good):
    if shop_dict.has_key(choose_good):
       return True
    else:
        print '''\n\t\t\t没有这项商品，请输入正确的商品名称！\n'''
        return False 
#是否需要退出循环
def BreakFlag():
    while True:
        Flag = raw_input('是否需要继续Y/N ?')
        if Flag =='Y'or Flag =='N':
            return Flag
        else:
            print '输入错误，请输入Y/N！'
#显示购物车清单 
def DicTra(): 
        if not shop_car.values():
            #说明购物车是空的
            print'''\n\t\t\t\033[31;1m您没有购买任何物品！\033[0m'''   
        else:
            #显示购物车内容
            print '''\n\t\t\t\033[31;1m您购买的商品为：\033[0m\033[32;1m商品名称 商品数量 商品总价\033[0m'''
            for i in shop_car:
                print '''\n\t\t\t\t\t%s  \t%d   \t%d'''%(i,shop_car[i][0],shop_car[i][1])

#将指定商品删除出购物车并显示当前购物车内容
def remove_shop_car(goods_name):
        if goods_existed(shop_car,goods_name):
            shop_car.pop(goods_name)
                               
#商城物品清单
shop_list = {'mac':5888,'bike':200,'car':10000,'clothes':500}
#购物车
shop_car = {}

print '''\n\t\t\t\t\033[31;5m欢迎来到电子商城\033[0m'''


while True:
    try:
        salary = int(raw_input("\t\t请输入您的工资:"))
        if salary < 200:
            print '''\t\t\033[31;1m屌丝，这不是你应该来的地方！\033[0m'''
        else:
            #记录当前余额为它的工资
            balance = salary
            break 
    except ValueError:
        show_wrong_number_info()
        
while True:
    Break_flag = ''
    print '''\n\t请选择您要进行的操作：\n\t\t\t1.购物 \n\t\t\t2.查看并修改购物车\n\t\t\t3.结账并退出\n'''
    
    while True:
        try:
            choice = int(raw_input('\t\t请输入您的选择：'))
            #用户输入只有1，2，3是有效的
            if choice <= 0 or choice > 3:
                show_wrong_number_info()
            else:
                break 
        #用户输入非整数，提示错误           
        except ValueError:
            show_wrong_number_info()
    
    #用户输入1，表示想购买商品
    if 1 == choice:
        while Break_flag != 'N':
            #打印购物清单
            show_shop_list()
            choose_good = raw_input('请输入您想购买的商品：')
            #检查商品是否存在
            if goods_existed(shop_list,choose_good):
                #用户余额不足
                if shop_list[choose_good] > balance:
                    print '\n\t\t\t\033[31;1m对不起，您的余额不足！\033[0m\n'
                    Break_flag = BreakFlag()
                else:
                    balance = balance - shop_list[choose_good]
                    #检查购物车是否有同类商品，如果有，将数量加1,并增加该商品的总价
                    #如果没有同类商品，则在购物车中新建
                    if shop_car.has_key(choose_good):
                        shop_car[choose_good][0] += 1
                        shop_car[choose_good][1] += shop_list[choose_good]
                    else:
                        shop_car[choose_good] = [1,shop_list[choose_good]]
                    print'\n\t\t\t\033[31;1m已成功加入购物车！\033[0m\n'
                    Break_flag = BreakFlag()
    elif 2 == choice:
        #显示购物车清单
        DicTra()
        Shopping_Car_Choose = 0
        while True:
            if shop_car:
                try:
                    Shopping_Car_Choose = int(raw_input('''\n\t请选择您要进行的操作：\n\t\t\t\t1.增加商品\n\t\t\t\t2.减少商品\n\t\t\t\t3.结账\n\t\t\t\t4.返回'''))
                    if Shopping_Car_Choose<= 0 or Shopping_Car_Choose > 4:
                        show_wrong_number_info()
                    else:
                        break
                except ValueError:
                    show_wrong_number_info()
            else:
                #购物车为空
                break
        #用户想增加商品数量         
        if 1 == Shopping_Car_Choose:
            while Break_flag != 'N':
                #显示购物车清单
                DicTra()
                if shop_car: 
                    Shopping_Car_Modify = raw_input('\n\t\t请输入您想增加的商品名称：')
                    #检查商品是否存在
                    if goods_existed(shop_car,Shopping_Car_Modify):
                        try:
                            Shopping_Car_Num = int(raw_input('\n\t\t请输入您增加的商品数量：'))
                            if Shopping_Car_Num >= 0: 
                                #判断余额是否足够
                                if balance >= Shopping_Car_Num * shop_list[Shopping_Car_Modify]:
                                    balance -= Shopping_Car_Num * shop_list[Shopping_Car_Modify]
                                    shop_car[Shopping_Car_Modify][0] += Shopping_Car_Num
                                    shop_car[Shopping_Car_Modify][1] = shop_car[Shopping_Car_Modify][0] * shop_list[Shopping_Car_Modify]
                                    Break_flag = BreakFlag()
                                else:
                                    print '\n\t\t\t\033[31;1m对不起，您的余额不足！\033[0m\n'
                                    Break_flag = BreakFlag()  
                            else:
                                show_wrong_number_info()  
                        except ValueError:
                            show_wrong_number_info()
        #用户想减少商品数量        
        elif 2 == Shopping_Car_Choose:
            while Break_flag != 'N':
                #显示购物车清单
                DicTra()
                if shop_car: 
                    Shopping_Car_Modify = raw_input('\n\t\t请输入您想减少的商品名称：')
                    #检查商品是否存在
                    if goods_existed(shop_car,Shopping_Car_Modify):
                        try:
                            Shopping_Car_Num = int(raw_input('\n\t\t请输入您想减少的商品数量：'))
                            #修改的数量必须小于等于当前的商品数量
                            if Shopping_Car_Num >= 0 and Shopping_Car_Num <= shop_car[Shopping_Car_Modify][0]:
                                balance += Shopping_Car_Num * shop_list[Shopping_Car_Modify]
                                shop_car[Shopping_Car_Modify][0] -= Shopping_Car_Num
                                shop_car[Shopping_Car_Modify][1] = shop_car[Shopping_Car_Modify][0]*shop_list[Shopping_Car_Modify]
                                #如果数量为0，需要从购物车中清除
                                if 0 == shop_car[Shopping_Car_Modify][0]:
                                    remove_shop_car(Shopping_Car_Modify)                                    
                                Break_flag = BreakFlag()
                            else:
                                show_wrong_number_info()
                        except ValueError:
                            show_wrong_number_info()
                else:
                    Break_flag = BreakFlag()           
         #用户想结账
        elif 3 == Shopping_Car_Choose:    
            #显示购物车清单
            DicTra()   
            #显示余额
            print '\n\t\t\t\033[31;1m您的余额为：%d，欢迎下次光临\033[0m\n'%(balance)
            exit_system()
        #用户想返回上一步：
        #不做处理，直接会就是返回上一步
        #
    else:
        #显示购物车清单
        DicTra()   
        #显示余额
        print '\n\t\t\t\033[31;1m您的余额为：%d，欢迎下次光临\033[0m\n'%(balance)
        exit_system()
                       
            
            
            