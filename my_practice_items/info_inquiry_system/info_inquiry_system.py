#!/usr/bin/env python
#coding:utf-8
import time


#设置循环跳出标记位
def break_flag():
    while True:
        flag = raw_input("\n\t\t是否继续y/n:")
        if 'y' == flag or 'n' == flag:
            return flag
        else:
            print '\n\t\t\t\033[31;1m输入错误，请输入y/n\033[0m\n'
#显示查询信息
def shw_staff_info(staff_list,match_count):
    if match_count:
        print '\n\033[32;1m序列 \t\t名字\t\t电话\t\t邮箱\033[0m\n'         
        for i in staff_list:
            print i
        print '\n\t\t\t\033[31;1m共查询到%d条信息y/n\033[0m\n'%(match_count)
    else:
        print '\n\t\t\t\033[31;1m抱歉，没有查询到任何信息y/n\033[0m\n' 

def exit_system():
    for i in range(3):
        print '\n\t\t\t\033[31;1m剩余%d秒退出系统\033[0m\n'%(3-i) 
        time.sleep(1)
#以只读的方式读取员工信息库文件，生成信息列表
file1 = open('info_database.txt','r')
#生成员工信息列表
staff_info = file1.readlines()

file1.close()


print '\n\t\t\t\033[31;1m欢迎来到员工信息查询系统\033[0m\n'

#是否跳出循环的标志位
Break_flag = ''

while 'n' != Break_flag:    
    Break_flTrueag = ''
    while True: 
        search_info = raw_input('\n\t\t请输入您的查询信息:')
        #查询信息需要大于2个字符
        if len(search_info) > 2:
            break
        else:
            print '\n\t\t\t\033[31;1m您输入不合法，请输入2个以上的字符！\033[0m\n'
        
    #记录有多少信息匹配
    match_count = 0
    #记录匹配的信息
    match_list = []
    
    for i in staff_info:
        if i.count(search_info):
            #将满足条件的字符串替换成高亮的字符串
            match_list.append(i.replace(search_info,'\033[42;31;1m%s\033[0m'%(search_info)))
            #记录匹配的数据数目
            match_count += i.count(search_info)
                        
    shw_staff_info(match_list,match_count)
    Break_flag = break_flag()
    #用户输入n，表示不想继续则退出系统
    if 'n' == Break_flag:
        exit_system()      
