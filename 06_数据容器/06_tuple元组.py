"""
元组特点：
    1、可以封装多个、不同类型的元素在内
    2、元组一旦定义完成，就不可修改

元组定义：
    1、定义元组字面量
    (元素, 元素, ......,元素)
    2、定义元组变量
    变量名称 = (元素, 元素, ......,元素)
    3、定义空元组
    变量名称 = ()
    变量名称 = tuple()

元组注意事项：
    元组只有一个数据时，这个数据后面要添加逗号
    my_tuple = ('Hello',)
"""

my_tuple = (1, "hello", True)
print(type(my_tuple))

my_tuple1 = ('Hello')
my_tuple2 = ('Hello',)
print(type(my_tuple1))
print(type(my_tuple2))


"""
元组也可以通过下标索引取出内容
index、count、len方法与list相同
"""
t5 = ((1, 2, 3), (4, 5, 6))
print(t5[0][1])


"""
元组中的list可以修改
"""
t6 = ("Hello", [1, 2, 3], [4, 5, 6])
t6[1][1] = 10
t6[2].append(7)
print(t6)