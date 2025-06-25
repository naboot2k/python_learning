"""
列表的基本语法：
    1、字面量
    [元素1,元素2,元素3,元素4,...]
    2、定义变量
    变量名称 = [元素1,元素2,元素3,元素4,...]
    3、定义空列表
    变量名称 = []
    变量名称 = list()
"""

name_list = ['王征','王伟','王伟伟','王伟伟伟']
print(name_list)
print(type(name_list))

new_list = ['偶吼吼', 600, True]
print(new_list)
print(type(new_list))

my_list = [[1,2,3],[4,5,6]]
print(my_list)
print(type(my_list))


"""
列表的下标索引：
    列表[下标索引]

列表的下标索引（反向）：
    列表元素从后向前，从-1开始，依次递减（-1，-2，-3，-4...）d
    
嵌套列表的下标索引：
    列表[外层下标][内层下标]
"""
name2_list = ['Tom', 'Lily', 'Rose']
print(name2_list[0])
print(name2_list[1])
print(name2_list[2])
print(name2_list[-1])
my_list2 = [[1,2,3],[4,5,6]]
print(my_list2[0][0])