# 字符串定义方式
# 1、单引号定义：name = '王征'
# 2、双引号定义：name = "王征"
# 3、三引号定义：name = """王征"""

name = '黑马程序员'
print(type(name))

name1 = "黑马程序员"
print(type(name1))

name2 = """黑马
           程序
           员"""
print(type(name2))



"""
字符串的引号嵌套
1、单引号定义法，可以内含双引号
2、双引号定义法，可以内含单引号
3、可以使用转义字符（\）来将引号解除效用，变成普通字符串
"""

name3 ='"王征"'
name4 ="'王征'"
name5 ="\"王征\""
name6 ='\'王征\''
print(name3,name4,name5,name6)