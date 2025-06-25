"""
    type()语句用法：
    type(被查看类型的数据)
"""

# 使用print直接输出类型信息
print(type("学习Python"))
print(type(666))
print(type(13.14))

# 使用变量记录类型信息
string_type = type("学习Python")
int_type = type(666)
float_type = type(13.14)
print(string_type)
print(int_type)
print(float_type)

# 直接查看变量的类型
name = "我爱学习"
print(type(name))

# *Python中变量不用提前声明类型，也没有类型*