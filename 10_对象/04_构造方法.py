"""
python类可以使用：__init__()方法，称之为构造方法。
可以实现：
    1、在创建类对象（构造类）的时候，会自动执行
    2、在创建类对象（构造类）的时候，将传入参数自动传递给__init__方法使用
"""

class Student:
    # 下面成员变量定义不写也行
    name = None
    age = None
    tel =  None

    def __init__(self, name, age,  tel):  # 构造方法也是成员方法，不要忘记在参数列表中提供self
        self.name = name    # 在构造方法内定义成员变量，需要使用self关键字
        self.age = age
        self.tel = tel
        print("Student类创建了一个对象")

stu = Student("张三", 18, "123456")
print(stu.name)
print(stu.age)
print(stu.tel)