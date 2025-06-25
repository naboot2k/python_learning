"""
list的while循环：
    index = 0
    while index <= len(列表):
        元素 = 列表[index]
        对元素进行处理
        index += 1
"""
my_list = ["apple", "banana", "orange", "pear", "pear"]
index = 0
while index < len(my_list):
    element = my_list[index]
    print(element)
    index += 1


print("-------------------------")
"""
list的for循环：
    for 临时变量 in 数据容器：
        对临时变量进行处理
"""
my_list = ["apple", "banana", "orange", "pear", "pear"]
for element in my_list:
    print(element)
