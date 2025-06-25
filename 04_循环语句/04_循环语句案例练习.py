import random


total = 10000
for x in range(1, 21):
    num = random.randint(1, 10)
    if num < 5:
        print(f"员工{x}，绩效分{num}，低于5，不发工资，下一位")
        continue
    total = total - 1000
    print(f"向员工{x}发放工资1000元，账户余额还剩{total}元")
    if total == 0:
        print("账户余额不足，结束发放")
        break
if total > 0:
    print("账户余额还剩", total)