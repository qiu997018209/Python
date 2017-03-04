1.函数入口为main.py

2.功能介绍：
  (1)网上商城:
	购物，结算，修改或增加购物车，可实时扣除信用卡余额，生成消费明细
        文件：shopping.py

  (2)网上银行:
	还款，转账，查询余额，查询消费明细
        文件：Internet_bank.py

  (3)数据库：采用python自带的pickle处理格式存储，具有一定的加密功能
	文件：consume_list.txt消费明细
	文件：Bank_lock.txt多次密码错误被锁定的用户名录
	文件：Bank_infobase.txt银行账户，保存账户，密码，余额

  (4)库文件：将一些重复利用的函数封装到库文件中，提供代码可读性
	文件：function_base.py
  