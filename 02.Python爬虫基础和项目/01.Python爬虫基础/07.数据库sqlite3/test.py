#coding:utf-8
import sqlite3

conn = sqlite3.connect('test.db')
#建立一个commany表格,id作为主要key，int型，不为空，员工名字emp_name
create_sql = 'create table commany(id int primary key not null,emp_name text not null)'
conn.execute(create_sql)

#插入数据
insert_sql = 'insert into commany values(?,?)'
conn.execute(insert_sql,(100,'qiu'))
conn.execute(insert_sql,(200,'jia'))

#拿到数据
cursors = conn.execute('select id,emp_name from commany')
for row in cursors:
	print(row[0],row[1])
conn.close()