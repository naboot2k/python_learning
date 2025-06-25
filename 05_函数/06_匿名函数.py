"""
本节分为：
    1、函数作为参数传递
    2、lambda匿名函数
"""

# 函数作为参数传递
def test_func(compute):
    result = compute(10, 20)
    print(result)

def compute(x, y):
    return x + y

test_func(compute)




"""
lambda匿名函数
    匿名函数，也叫lambda函数
    语法：lambda 参数列表: 函数体（一行代码）
    注意：无名称的匿名函数，只可临时使用一次
"""
def test_func1(compute):
    result = compute(1, 2)
    print(result)

test_func1(lambda x, y: x - y)