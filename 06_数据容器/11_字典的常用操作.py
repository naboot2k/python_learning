"""
新增元素：
    语法：字典[Key] = Value
    结果：若字典没该Key值，新增一个元素
"""

"""
更新元素：
    语法：字典[Key] = Value
    结果：对已存在的Key执行上述操作，更新Value值 
"""

"""
删除元素：
    语法：字典.pop(Key)
    结果：获得指定Key的Value，同时字典被修改，指定Key的数据被删除
"""

"""
清空字典：
    语法：字典.clear()
    结果：字典被清空
"""

"""
获取全部的Key：
    语法：字典.Keys()
    结果：得到字典中全部的Key
"""
my_dict = {"name": "张三", "age": 18, "sex": "男"}
keys = my_dict.keys()
print(keys)

# 遍历字典
# 方式一
for key in keys:
    print(key, my_dict[key])

# 方式二
for key in my_dict:
    print(key, my_dict[key])


# 统计字典内的元素数量
print(len(my_dict)) 