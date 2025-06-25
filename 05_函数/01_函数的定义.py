"""
函数的定义：(当函数体遇到return就不执行了)
def 函数名(传入参数):
    函数体
    return 返回值
"""


def add(a, b):
     result = a + b
     return result

r = add(3, 4)
print(r)


"""
None类型:
1、用在函数无返回值
2、用在if判断上
    在if判断中，None等同于False（if not False为假执行）
    一般用于在函数中主动返回None，配合if判断做相关处理
3、用于声明无内容的变量上
    定义变量，但暂时不需要变量有具体值
"""

def say_hi():
    print("hello world")
def say_hi2():
    print("hello world")
    return None

result = say_hi()
print(result)
print(type(result)) 