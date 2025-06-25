"""
字符串大小比较
"""


"""
根据ASCII码表，对应的数值进行比较
"""


"""
字符串是按位比较，也就是一位位进行比较，只要有一位大，那么整体就大
    1、一位一位比较，直到某位大小不同
    2、长度不等且前缀相等，则长度长的大
"""
# 若想忽略大小写，则使用lower()方法
name1 = "Zheng Wang"
name2 = "zheng wang"
print(name1 == name2)
print(name1.lower() == name2.lower())

