# 字符串变量中加入占位符
name = "王征"
salary = 25000.1
message = "欢迎来到Python的世界，%s" % name

# 多个变量占位，变量要用括号括起来，并按照占位的顺序填入
message1 = "欢迎来到Python的世界，%s,你的薪资是%.1f" % (name,salary)

print(message)
print(message1)


"""
数字精度控制
使用辅助符号"m.n"来控制数据的宽度和精度
1、m控制宽度，要求是数字，设置的宽度小于数字自身，不生效；设置宽度大于数字自身，数字前空格填充
2、n控制小数点精度，要求是数字，会进行小数的四舍五入
"""


# 字符串格式化 - 快速写法（不限数据类型，不做精度控制）
name1 = "王征"
set_up_year = 1942
school = "南京邮电大学"
print(f"我是{name1}，我出生在{set_up_year}年，来自{school}")


# 字符串格式化 - 表达式的格式化
print("1 * 1的结果是：%3.d" % (1 * 1))
print(f"1 * 1的结果是：{1 * 1}")
print("字符串在Python中的类型是：%s" % type("字符串"))