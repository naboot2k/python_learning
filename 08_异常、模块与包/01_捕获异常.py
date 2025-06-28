"""
不捕获异常时，当程序出现一个异常的时候，程序将停止
"""
"""
捕获异常基本语法：
    try:
        可能发生错误的代码
    except:
        如果出现异常执行的代码
"""
# try:
#     f = open("error.txt", "r", encoding="utf-8")
# except:
#     print("文件不存在，使用w模式创建新文件")
#     f = open("error.txt", "w", encoding="utf-8")


"""
捕获指定异常：
    一般try下方只放一行尝试执行的代码
"""
# try:
#     print(name)
# except NameError as e: # e记录着异常的具体信息
#     print('name变量名称未定义错误')
#     print(e)


"""
捕获多个异常：
    当捕获多个异常时，可以把要捕获的异常类型的名字放到except后，并使用元组的方式进行书写
"""
# try:
#     print(name)
# except (NameError, ZeroDivisionError) as e:
#     print('出现变量未定义 或者 除以0的异常错误')
#     print(e)


"""
捕获所有异常：
"""
try:
    print(1/0)
except Exception as e:
    print('出现异常错误')
    print(e)


"""
异常else：
    else表示的是如果没有异常要执行的代码
"""