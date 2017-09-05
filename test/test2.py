import test
 
test.show()

from test import show2 
show2()


#指定模块路径
#先找当前路径,在去终端中设置的PYTHONPATH下的路径
#然后去默认路径下找,一般是/usr/local/lib/python
#模块搜索路径包含在sys.path中,包含了python安装的路径