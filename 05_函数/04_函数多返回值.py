"""
函数多返回值
"""

"""
1、按照返回值顺序，写对应顺序的多个变量接收即可
2、变量之间用逗号隔开
3、支持不同类型的数据return
"""
def test_return():
    return 1, "hello", True

x, y, z = test_return()
print(x, y, z)

