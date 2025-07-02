"""
演示异常的传递
    异常是具有传递性的
"""
def func01():
    print("func01开始执行")
    num = 1 / 0
    print("func01执行完毕")

def func02():
    print("func02开始执行")
    func01()
    print("func02执行完毕")

def main():
    try:
        func02()
    except Exception as e:
        print(e)

main()