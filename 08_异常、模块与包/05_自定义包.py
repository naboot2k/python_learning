"""
Python包：
    从物理上看，包就是一个文件夹，在该文件夹下包含了一个__init__.py文件，该文件夹可用于包含多个模块文件
    从逻辑上看，包的本质依然是模块
包的作用：
    当模块文件越来越多时，包可以帮助我们管理这些模块，包的作用就是包含多个模块，但包的本质依然是模块
"""


"""
导入包：
    方式一：
        语法：import 包名.模块名
        使用方法：包名.模块名.目标
    方式二：
        语法：from 包名 import 模块名
        使用方法：模块名.目标
    方式三：
        注意：必须在'__init.py__'文件中添加'__all__ = []'，控制允许导入的模块列表
"""
# import my_package.my_module1
# my_package.my_module1.info_print1()
# my_package.my_module1.info_print2()

# from my_package import my_module1
# from my_package.my_module1 import *
# info_print1()
# info_print2()

# from my_package import *
# my_module1.info_print1()