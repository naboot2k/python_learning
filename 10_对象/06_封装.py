"""
定义私有成员的方式：
    1、私有成员变量：变量名以__开头
    2、私有成员方法：方法名以__开头

特点：
    1、私有方法无法直接被类对象使用
    2、私有变量无法赋值、也无法获取值
    3、私有成员无法被类对象使用，但是可以被其他的成员使用
"""

class Phone:
    __current_voltage = 0.5

    def __keep_single_core(self):
        print("保持单核运行")

    def call_by_5g(self):
        if self.__current_voltage >= 1:
            print("正在使用5G")
        else:
            self.__keep_single_core()
            print("电量不足，无法使用5G通话")


phone = Phone()
# phone.__keep_single_core()
# print(phone.__current_voltage)
phone.call_by_5g()
