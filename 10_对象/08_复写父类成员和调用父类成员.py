"""
子类继承父类的成员属性和成员方法后，如果对其“不满意”，可以进行复写
即：在子类中重新定义同名的属性或方法即可。
"""

class Phone:
    IMEI = None
    producer = "apple"

    def call_by_5g(self):
        print("5G通话")

class MyPhone(Phone):
    producer = "HW"

    def call_by_5g(self):
        print("升级5G通话")
        # 调用父类成员
        print("父类的厂商：", Phone.producer)
        super().call_by_5g() # 用super()调用父类方法时，不需要在括号中写self
        print("新5G通话")

phone = MyPhone()
print(phone.producer)
phone.call_by_5g()


"""
调用父类同名成员
一旦复写父类成员，那么类对象调用成员的时候，就会调用复写后的新成员
如果需要使用被复写的父类的成员，需要特殊的调用方式：

方式1：调用父类成员
    使用成员变量：父类名.成员变量
    使用成员方法：父类名.成员方法(self)

方式2：使用super()调用父类成员
    使用成员变量：super().成员变量
    使用成员方法：super().成员方法()
    
注意：只可以在子类内部调用父类的同名成员，子类的实体类对象调用默认是调用子类复写的
"""
