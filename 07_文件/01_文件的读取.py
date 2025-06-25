"""
open()打开函数：
    语法：open(name, mode, encoding) 注意：open函数实际形参中，encoding并不是第三位参数，因此需要关键字传参
        name:是要打开的目标文件名的字符串（可以包含文件所在的具体路径）
        mode：设置打开文件的模式（访问模式）：只读、写入、追加等
        encoding：编码格式（推荐使用UTF-8）
"""

"""
mode常用的三种基础访问模式：
    1、r：以只读方式打开文件，文件的指针将会放在文件的开头。这是默认模式。
    2、w：打开一个文件只用于写入。如果该文件已存在则打开文件，并从头开始编辑，原有内容会被删除；如果该文件不存在，创建新文件。
    3、a：打开一个文件用于追加。如果该文件已存在，新的内容将会被写入到已有内容之后。如果该文件不存在，创建新文件并写入。
"""
f = open("E:/test.txt", "r", encoding="utf-8")
print(type(f))


"""
对文件对象操作的方法：
    1、read()方法
        语法：文件对象.read(num)
        注意：num表示要从文件中读取的数据的长度（单位是字节），如果没有传入num，那么就表示读取文件中所有的数据
    2、readlines()方法
        语法：文件对象.readlines()
        注意：该方法可以按照行的方式把整个文件中的内容进行一次性读取，并且返回的是一个列表，其中每一行的数据为一个元素。
    3、readline()方法
        语法：文件对象.readline()
"""

# content = f.read(10)
# 连续调用两次read()或readlines()，第二次会从第一次结尾的地方开始
# content1 = f.read()
# print(content)
# print(content1)
# print("-------------------------------------------")
# lines = f.readlines()
# print(lines)
line1 = f.readline()
line2 = f.readline()
print(line1)
print(line2)

print("-------------------------------------------")

"""
for循环读取文件行
    语法：for line in open(name, mode):
            print(line)
"""
f1 = open("E:/test.txt", "r", encoding="utf-8")
for line in f1:
            print(line)


"""
关闭文件对象：
    语法：f.close()
"""
f.close()
f1.close()


"""
with open方法：
    语法：with open(name, mode)（空格）as f:
            对文件的操作
    注意：通过在with open的语句块中对文件进行操作，可以在操作完成后自动close文件，避免遗忘掉close方法
    
"""
with open("E:/test.txt", "r", encoding="utf-8") as f:
    print(f.readlines())