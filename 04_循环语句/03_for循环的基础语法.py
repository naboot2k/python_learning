"""
for循环语句：
for 临时变量 in 待处理数据集（序列）:
    循环满足条件时执行的代码
"""

name = "itheima"
for x in name:
    # 将name里的内容挨个取出赋予临时变量
    print(x , end="")
print()

total = 0
name1 = "itheima is a brand of itcast"
for x in name1:
    if x=='a':
        total = total + 1
print(total)


"""
序列类型：（其内容可以一个个依次取出的一种类型）
1、字符串 2、列表 3、元组等
"""

"""
range语句：(获得一个简单的数字序列)

语法1：
range(num)
获取一个从0开始到num结束的数字序列（不含num本身）

语法2：
range(num1, num2)
获得一个从num1开始到num2结束的数字序列（不含num2本身）

语法3：
range(num1, num2, step)
获得一个从num1开始到num2结束的数字序列（不含num2本身）
step为数字之间的步长
"""

# 九九乘法表练习
for i in range(1,10):
    for j in range(1,i+1):
        print(i,"*",j,"=",i*j,end="\t")
    print()