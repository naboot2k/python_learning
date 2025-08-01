"""
常见的几个魔术方法：
    1、__init__
    2、__str__
    3、__lt__
    4、__le__
    5、__eq__
"""
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # 输出对象时，会自动调用此方法，将对象转换成字符串
    def __str__(self):
        return "Student类对象(name={}, age={})".format(self.name, self.age)

    # 比较两个对象中的属性值，返回布尔值（不支持等于）
    def __lt__(self, other):
        return self.age < other.age

    def __le__(self, other):
        return self.age <= other.age
    def __eq__(self, other):
        return self.age == other.age




stu = Student("张三", 18)
print(stu)
print(stu.__str__())
print(str(stu))

stu1 = Student("王五", 18)
print(stu < stu1)
print(stu <= stu1)
print(stu == stu1)
