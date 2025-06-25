"""
在Python中，如果将函数定义为class（类）的成员，那么函数会称之为：方法
    方法的使用与函数稍有不同
例：
    class Student
        def add(self, x, y):
            return x + y

    student = Student()
    num = student.add(1, 2)
"""


"""
列表查询功能（方法）：
    查找指定元素在列表的下标，如果找不到，报错ValueError
    语法：列表.index(元素)
"""
my_list = ["apple", "banana", "orange", "pear", "pear"]
print(my_list.index("pear"))
# print(my_list.index("pear1"))


"""
列表修改功能（方法）：
    修改特定位置（索引）的元素值
    语法：列表[下标] = 值
"""
my_list[3] = "strawberry"
print(my_list)


"""
列表插入功能（方法）：
    插入元素
    语法：列表.insert(下标,元素)，在指定的下标位置，插入指定元素
"""
my_list.insert(1,"pear")
print(my_list)


"""
列表追加功能（方法）：
    1、追加一个元素
    在列表尾部追加指定元素
    语法：列表.append(元素)
    2、追加一批元素
    在列表尾部追加指定数据容器中的元素
    语法：列表.extend(其他数据容器)
"""
my_list.append("blueberry")
print(my_list)

my_list.extend(['a','b'])
print(my_list)


"""
列表删除功能（方法）：
    1、删除指定下标对应的元素
    语法：1、del 列表[下标]
         2、列表.pop(下标)
    2、删除某元素在列表中的第一个匹配项
    语法：列表.remove(元素)
    3、清空列表内容
    语法：列表.clear()
    eg: my_list.clear()
        print(my_list)
"""
del my_list[-1]
throw_num = my_list.pop(-1)
print(my_list)

my_list.remove('pear')
print(my_list)


"""
列表统计功能（方法）：
    1、统计某元素在列表中的数量
    语法：列表.count(元素)
    2、统计列表内共有多少元素（非方法）
    语法：len(列表)
"""
print(my_list.count('pear'))
print(len(my_list))


