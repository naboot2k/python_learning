"""
类中包含成员变量和成员方法
"""

"""
在类中定义成员方法和定义函数基本一致，但仍有细微区别：
    def 方法名(self, 形参1, ......, 形参N):
        方法体
        
self关键字是成员方法定义的时候，必须填写的
1、它用来表示类对象自身的意思
2、当我们使用类对象调用方法时，self会自动被python传入
3、* 在方法内部，想要访问类的成员变量，必须使用self *
"""
class Student:
    name = None
    age = None

    def say_hi(self):
        print(f"Hi,我是{self.name},我的年龄是{self.age}岁")

    def show_age(self, msg):
        print(f"Hello，{msg}")

# self关键字，尽管在参数列表中，但是传参的时候可以忽略它
stu = Student()
stu.name = "张三"
stu.age = 18
stu.say_hi()
stu.show_age("很高兴认识大家!")

stu2 = Student()
stu2.name = "李四"
stu2.age = 19
stu2.say_hi()
stu2.show_age("很高兴认识大家!")


