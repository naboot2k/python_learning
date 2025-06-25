"""
局部变量：
    定义在函数体内部的变量，即只在函数体内部生效

全局变量：
    在函数体内、外都能生效的变量，可在函数外定义
"""


"""
global关键字：
    使用global关键字可以在函数内部声明变量为全局变量
"""
num = 100

def testA():
    print(num)

def testB():
    global num
    num = 200
    print(num)

testA()
testB()
print(num)