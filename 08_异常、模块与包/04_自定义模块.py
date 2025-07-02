"""
自定义模块：
    案例：新建一个Python文件，命名为my_module1.py,并定义test函数
    注意事项：当导入多个模块的时候，且模块内有同名功能，当调用这个同名功能的时候，调用到的是后面导入的模块的功能
"""

# import my_module1
# my_module1.test(1, 2

# from my_module1 import test
# test(1, 2)

from my_module1 import test    # 代码变灰，pycharm提示代码没有被使用
from my_module2 import test
test(1, 2)


"""
__name__变量：在my_module1中可以查看
"""


"""
__all__变量:如果一个模块文件中有'__all__'变量，当使用'from xxx import *'导入时，只能导入这个列表中的元素，在my_module1中可以查看 
"""