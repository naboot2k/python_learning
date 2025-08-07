"""
闭包是 Python 中一个重要的概念，指的是内部函数可以记住并访问其外部函数的变量，即使外部函数已经执行完毕。它通常用于数据封装和状态保持，能够让代码更加灵活和高效。
"""

# 简单闭包
def outer(logo):
    def inner(msg):
        print(f"<{logo}>{msg}<{logo}>")

    return inner    # 返回的是内部函数

fn1 = outer("nb")
fn1("hello world")
fn1("nihao")

fn2 = outer("python")
fn2("hello world")
fn2("nihao")


# 在闭包中修改外部函数变量的值：需要使用nonlocal 关键字修饰外部函数的变量才可以在内部函数中修改它
def outer(num1):

    def inner(num2):
        nonlocal num1
        num1 += num2
        print(num1)

    return inner

fn = outer(10)
fn(20)
fn(20)
fn(20)  # 外部程序无法修改num1的值


# 闭包的应用：ATM的实现
def account_create(initial_amount = 0):

    def atm(num, deposit = True):
        nonlocal initial_amount
        if deposit:
            initial_amount += num
            print(f"存款：+{num}，余额为：{initial_amount}")
        else:
            initial_amount -= num
            print(f"取款：-{num}，余额为：{initial_amount}")

    return atm

atm = account_create()
atm(100)
atm(200)
atm(300, False)














