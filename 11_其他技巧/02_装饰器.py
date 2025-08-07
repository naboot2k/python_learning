"""
装饰器其实也是一种闭包，其功能就是在不破坏目标函数原有代码和功能的前提下，为目标函数增加新功能
"""

# 装饰器的一般写法（闭包）
# def outer(func):
#     def inner():
#         print("我要睡觉了")
#         func()
#         print("我睡醒了")
#
#     return inner
#
#
# # 原函数
# def sleep():
#     import random
#     import time
#     print("睡眠中.....")
#     time.sleep(random.randint(1,5))
#
#
# fn = outer(sleep)
# fn()


# 装饰器的快捷写法（语法糖）
def outer(func):
    def inner():
        print("我要睡觉了")
        func()
        print("我睡醒了")

    return inner

@outer
def sleep():
    import random
    import time
    print("睡眠中.....")
    time.sleep(random.randint(1,5))

sleep()