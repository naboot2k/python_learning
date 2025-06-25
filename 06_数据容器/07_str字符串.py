"""
字符串是一个无法修改的数据容器
字符串通过下标进行存取
"""
my_str = "Hello"
print(my_str[0])


"""
查找特定字符串的下标索引值：
    语法：字符串.index(字符串)
"""
print(my_str.index("l"))


"""
字符串替换：
    语法：字符串.replace(字符串1, 字符串2)
    功能：将原字符串内的全部内容：字符串1，替换为字符串2
    注意：该方法并不是修改了原字符串，而是得到了一个新的字符串
"""
new_str = my_str.replace("l", "L")
print(new_str)


"""
字符串的分割：
    语法：字符串.split(分隔符字符串)
    功能：按照指定的分隔符字符串。将字符串划分为多个字符串，并存入列表对象中
    注意：字符串本身不变，而是得到了一个列表对象
"""
my_str = "Hello World How are you"
new_list = my_str.split(" ")# 按照空格进行分割
print(new_list)


"""
字符串的规整操作：
    1、去前后空格
    语法：字符串.strip()
    2、去前后指定字符串
    语法字符串.strip(字符串)
"""
my_str = "   Hello World   "
print(my_str.strip())

my_str = "   12Hello World   "
my_str2 = "12   Hello World   21"
print(my_str.strip("12"))
print(my_str2.strip("12"))


"""
统计字符串中子字符串出现的次数：
    语法：字符串.count(子字符串)
"""
my_str = "Hello World Hello Python"
print(my_str.count("Hello"))


"""
统计字符串长度：
    语法：len(字符串)
    注意：统计出的长度就是字符串可见长度
"""


"""
字符串遍历（略）
"""

















