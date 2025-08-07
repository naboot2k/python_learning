"""
工厂模式是一种创建型设计模式，主要用于简化对象的创建过程。其核心思想是通过一个工厂类来创建对象，
用户只需告诉工厂需要什么类型的对象，工厂就会返回相应的实例，而无需了解对象的具体实现细节。

优点：
    1、大批量创建对象的时候有统一的入口，易于代码维护
    2、当发生修改时，仅修改工厂类的创建方法即可
"""

class Person:
    pass

class Worker(Person):
    pass

class Student(Person):
    pass

class Teacher(Person):
    pass

class PersonFactory:
    def create_person(self, p_type):
        if p_type == "w":
            return Worker()
        elif p_type == "s":
            return Student()
        else:
            return Teacher()

pf = PersonFactory()
worker1 = pf.create_person('w')
student1 = pf.create_person('s')
teacher1 = pf.create_person('t')