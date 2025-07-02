"""
模块就是一个python文件，里面有类、函数、变量等，我们可以拿过来用（导入模块去使用）
模块的导入一般写在代码文件的开头位置
"""

"""
模块的导入方式：
    语法：[from 模块名] import [模块 | 类 | 变量 | 函数 | *] [as 别名]
常用组合形式：
    import 模块名
    from 模块名 import 类、变量、方法等
    from 模块名 import *     # *代表模块下所有的功能
    import 模块名 as 别名
    from 模块名 import 功能名 as 别名
"""

"""
import 模块名：
    语法：1、import 模块名
         2、import 模块名1, 模块名2
    模块功能使用方法：模块名.功能名()
"""
# import time
# print("hello")
# time.sleep(5)     # 通过. 就可以是使用模块内部的全部功能（类、 函数、 变量）
# print("5 seconds after")


"""
from 模块名 import 功能名：
    使用方法：功能名()
"""
from time import sleep
print("hello")
sleep(5)     # 让程序睡眠1秒（阻塞）
print("5 seconds after")


"""
as定义别名
    基本语法：
        # 模块定义别名
        import 模块名 as 别名
        #功能定义别名
        from 模块名 import 功能 as 别名
"""
