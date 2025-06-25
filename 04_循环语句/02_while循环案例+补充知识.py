import random
from functools import total_ordering

num = random.randint(1, 10)

print("数字猜猜我是多少？")
total = 0
while True:
    guess = int(input("请输入数字："))
    total += 1
    if guess > num:
        print("数字太大了")
    elif guess < num:
        print("数字太小了")
    else:
        print(f"恭喜你猜对了,你一共猜了{total}次")
        break


"""
print输出不换行：
print("hello"， end='')
print("world"， end='')
"""
print("hello", end='')
print("world")


""


"""
制表符 \t 
相当于按一个Tab键，一个\t占4位，如果前面的字符位数不够4位就补到4位
制表位一般为8位
"""
print("hello\tworld")
print("heyo\tworld")