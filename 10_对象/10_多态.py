"""
多态，指的是：多种状态，即完成某个行为时，使用不同的对象会得到不同的状态
"""
from abc import ABC, abstractmethod
"""
这种设计的含义是：
    1、父类用来确定有哪些方法
    2、具体的方法实现，由子类自行决定
    
下面Animal类的写法，就叫做抽象类（也可以称之为接口）
Python 提供了 abc 模块来支持抽象类和抽象方法。通过继承 abc.ABC 类并使用 @abstractmethod 装饰器，可以定义抽象方法

抽象类：是一种特殊的类，不能直接实例化，只能被继承，用于定义接口或行为规范，包含抽象方法
抽象方法：指在基类中声明但未实现的方法，必须由子类实现

注意：子类继承抽象类后，必须实现所有抽象方法，才能被实例化
"""
class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        print("汪汪汪")

class Cat(Animal):
    def speak(self):
        print("喵喵喵")

def make_speak(animal: Animal):
    animal.speak()

dog = Dog()
cat = Cat()
make_speak(dog)
make_speak(cat)
