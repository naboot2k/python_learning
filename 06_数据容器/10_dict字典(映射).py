"""
字典的定义，同样使用{}，不过存储的元素是一个个键值对
    语法：1、{key: value, key: value, ...... , key: value}
         2、my_dict = {key: value, key: value, ...... , key: value}
         3、my_dict = {}
            my_dict =dict()
    注意：1、字典的key值不可以重复
         2、不可以使用下标索引
         3、字典的Key和value可以是任意数据类型（Key不可以是字典）
"""
my_dict = {"name": "张三", "age": 18, "sex": "男"}
my_dict2 = {}
print(my_dict)
print(my_dict2)

# 字典的key值不可以重复
my_dict = {"name": "张三", "name": "张三", "age": 18, "sex": "男"}
print(my_dict)
print(my_dict["name"])

# 字典的嵌套
my_dict3 = {"name": "张三",
            "age": 18,
            "sex": "男",
            "addr": {
                "province": "江苏",
                "city": "南京"}
            }
print(my_dict3["addr"]["city"])