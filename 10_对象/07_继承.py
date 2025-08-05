"""
继承分为单继承和多继承
继承表示：将从父类那里继承(复制)来成员变量和成员方法(不含私有)
"""

"""
单继承的语法：
    class 类名(父类名):
        类内容体
"""
class Phone:
    IMEI = None
    producer = "apple"

    def call_by_4g(self):
        print("4g通话")


class Phone2025(Phone):
    face_id = "10001"

    def call_by_5g(self):
        print("2025年新功能：5g通话")


phone = Phone2025()
print(phone.producer)
phone.call_by_4g()
phone.call_by_5g()


"""
多继承的语法：
    class 类名(父类1, 父类2, ......, 父类N)
        类内容体
        
注意：多个父类中，如果有同名的成员，那么默认以继承顺序（从左到右）为优先级，即先继承的保留，后继承的被覆盖
"""
class NFC_reader:
    nfc_type = "第五代"
    producer = "HW"

    def read_card(self):
        print("NFC读卡")

    def write_card(self):
        print("NFC写卡")


class Remote_controller:
    rc_type = "红外遥控"

    def control(self):
        print("红外遥控")


class MyPhone(Phone, NFC_reader, Remote_controller):
    pass   # 当新类中没有成员变量和成员方法时，可以添加pass来补全语法


phone = MyPhone()
phone.call_by_4g()
phone.read_card()
phone.control()
phone.write_card()
print(phone.producer)













