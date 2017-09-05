1.如何加载模块
	方法1:设置PYTHONPATH环境变量
	sudo vim /etc/profile
	export PYTHONPATH=/home/ubuntu1/share/temp/Python/Python基础学习/Day07_模块的安装与制作
	source /etc/profile

	方法2:设置sys.path,实时生效
	ubuntu1@ubuntu1:~/share/temp/Python/Python基础学习/Day07/01_模块的安装与制作/my_package$ python
	import sys
	sys.path.append("/home/ubuntu1/share/temp/Python/Python基础学习/Day07/01_模块的安装与制作/my_package")
	import my_package

	使用:
	from my_package import a
	a.aFunc()

	或者

	import my_package.a
	my_package.a.aFunc()

	或者

	在__init__.py中加入__all__=['a','b']
	from my_package import *
	a.aFunc()

2.如何制作包:
	1.新建setup.py
		from distutils.core import setup
		setup(name="package", version="1.0", description="package's module", author="qiujiahao", py_modules=['my_package.a', 'my_package.b', 'my_package2.c', 'my_package2.d'])
	2.构建模块
		ubuntu1@ubuntu1:~/share/temp/Python/Python基础学习/Day07_模块的安装与制作$ python setup.py build
	3.生成发布压缩包
		python setup.py sdist
		压缩包在dist/package-1.0.tar.gz下,发布出去即可

3.拿到压缩包之后如何使用:
	tar zxvf package-1.0.tar.gz 
	sudo python setup.py install(会复制到系统路径中)	或者sudo python setup.py install --prefix=你指定的路径
	代码使用:
	from my_package import *
		a.aFunc()

生成路径:
ubuntu1@ubuntu1:~/share/temp/Python/Python基础学习$ tree Day07_模块的安装与制作
Day07_模块的安装与制作
├── build
│   └── lib.linux-x86_64-2.7
│       ├── my_package
│       │   ├── a.py
│       │   ├── b.py
│       │   └── __init__.py
│       └── my_package2
│           ├── c.py
│           ├── d.py
│           └── __init__.py
├── dist
│   └── package-1.0.tar.gz
├── MANIFEST
├── my_package
│   ├── a.py
│   ├── a.pyc
│   ├── b.py
│   ├── b.pyc
│   ├── __init__.py
│   └── __init__.pyc
├── my_package2
│   ├── c.py
│   ├── d.py
│   └── __init__.py
├── readme.txt
└── setup.py

7 directories, 19 files
