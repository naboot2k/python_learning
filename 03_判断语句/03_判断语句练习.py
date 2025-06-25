import random

num = random.randint(1, 10)
print("这是一个猜数字游戏，你一共有三次机会。祝好运!")
num_guess = int(input("请输入数字："))

if num_guess != num:
    print("不好意思，猜错了")
    if num_guess > num:
        print("猜的数字太大了")
    else:
        print("猜的数字太小了")

    num_guess = int(input("请输入数字："))
    if  num_guess == num:
        print("恭喜你猜对了")
    else:
        print("猜错了")
        if num_guess > num:
            print("猜的数字太大了")
        else:
            print("猜的数字太小了")

        num_guess = int(input("请输入数字："))
        if num_guess == num:
            print("恭喜你猜对了")
        else:
            print("猜错了")
            if num_guess > num:
                print("猜的数字太大了")
            else:
                print("猜的数字太小了")
            print(f"数字为：{num}")
else:
    print("恭喜你猜对了")