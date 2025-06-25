"""
函数多种传参方式
"""
def user_info(name, age, gender):
    print("用户名：%s, 年龄：%d, 性别：%s" % (name, age, gender))

"""
位置参数：调用函数时根据函数定义的参数位置来传递参数
    注意：传递的参数和定义的参数的顺序及个数必须一致
"""
user_info("张三", 18, "男")


"""
关键字参数：函数调用时通过“键=值”形式传递参数
    注意：函数调用时，如果有位置参数时，位置参数必须在关键字参数的前面，但关键字参数之间不存在先后顺序
"""
# 关键字传参
user_info(name="张三", age=18, gender="男")
# 可以不按照顺序传递参数
user_info(gender="女", age=18, name="张三")
# 可以和位置参数混合传递，位置参数必须在关键字参数的前面，且匹配参数顺序
user_info("张三", gender="女", age=18)


"""
缺省参数：缺省参数也叫做默认参数，用于定义函数，为参数提供默认值，调用函数时可不传该默认参数的值
    注意：所有位置参数必须出现在默认参数前，包括函数定义和调用
"""
def user_info1(name, age, gender="男"):
    print("用户名：%s, 年龄：%d, 性别：%s" % (name, age, gender))

user_info1("张三", 18)
user_info1("李四", 19, "女")


"""
可变参数：可变参数也叫做不定长参数，用于不确定调用的时候会传递多少个参数（不传参也可以）的场景
    作用：当调用函数时不确定参数个数时，可以使用不定长参数
    类型：1、位置传递
         2、关键字传递
"""

#位置传递
def user_info2(*args): # 传进去的参数会保存在args中，args是元组类型
    print(args)

user_info2("张三", 18, "男")
user_info2("张三", 18, "男", "上海")

# 关键字传递
def user_info3(**kwargs): # 传进去的参数会保存在kwargs中，kwargs是字典类型
    print(kwargs)

user_info3(name="张三", age=18, gender="男")
user_info3(name="张三", age=18, gender="男", city="上海")
