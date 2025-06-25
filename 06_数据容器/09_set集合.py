"""
集合的定义：(无序、去重)
    基本语法：
        1、{元素, 元素, 元素 ..., 元素}
        2、变量名称 = {元素, 元素, 元素 ..., 元素}
        3、变量名称 = set()
    注意：集合是无序的，所以不支持下标索引访问，允许修改
"""
my_set = {1, 2, 3, 4, 5, 5, 5, 5}
print(my_set)

# 添加元素
my_set.add(6)
print(my_set)

my_set.add(5)
print(my_set)

# 移除元素
my_set.remove(5)
print(my_set)

# 随机取出一个元素，同时集合本身被修改，元素移除
print(my_set.pop())
print(my_set)

# 清空集合
my_set.clear()
print(my_set)

"""
取两个集合的差集:
    语法：集合1.difference(集合2)
    功能：取出集合1有而集合2没有的元素
    结果：得到一个新集合，集合1和集合2不变
"""
my_set1 = {1, 2, 3, 4, 5}
my_set2 = {4, 5, 6, 7, 8}
print(my_set1.difference(my_set2))


"""
消除两个集合的差集：
    语法：集合1.difference_update(集合2)
    功能：对比集合1和集合2，在集合1内，删除和集合2相同的元素
    结果：集合1被修改，集合2不变
"""
my_set1 = {1, 2, 3, 4, 5}
my_set2 = {4, 5, 6, 7, 8}
my_set1.difference_update(my_set2)
print(my_set1)


"""
取两个集合的并集:
    语法：集合1.union(集合2)
    功能：取出集合1和集合2都有的元素
    结果：得到一个新集合，集合1和集合2不变
"""
my_set1 = {1, 2, 3, 4, 5}
my_set2 = {4, 5, 6, 7, 8}
my_set3 = my_set1.union(my_set2)
print(my_set3)


"""
取两个集合的交集:
    语法：集合1.intersection(集合2)
    功能：取出集合1和集合2都有的元素
    结果：得到一个新集合，集合1和集合2不变
"""
my_set1 = {1, 2, 3, 4, 5}
my_set2 = {4, 5, 6, 7, 8}
my_set3 = my_set1.intersection(my_set2)
print(my_set3)


# 统计集合元素数量
my_set1 = {1, 2, 3, 4, 5}
print(len(my_set1))

# 集合的遍历
for element in my_set1:
    print(element)


