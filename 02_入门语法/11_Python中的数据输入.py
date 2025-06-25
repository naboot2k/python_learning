
# input()语句，不管输入什么都视为字符串

# 可以直接在input()中设置提示语句
name = input("What is your name?\n")
print("Hello, %s" % name)

# 可以通过数据类型转换将input输入的数据转换成其他数据类型
age = int(input("How old are you?\n"))
final_age = age + 10
print("After 10 years, you will be %d years old" % final_age)