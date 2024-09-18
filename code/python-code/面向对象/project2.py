#封装

class Phone:
    IMIE=None     #序列号
    __curr=None   #电压
    ID="xiaomi"

    def call_by_4G(self):
        print("4G通话")

    def __init__(self):
        self.__curr=2

    def __keep_core(self):
        print("单核运行")

    def call_by_5g(self):
        if self.__curr >=1:
            self.__keep_core()

#单继承
class Phone2023(Phone):
    ID = "huawei"
    def call_by_6G(self):
        self.call_by_5g()
        print(Phone.ID)
        print(self.ID)

        print("6G运行")

phone=Phone2023()
phone.call_by_6G()

#多继承
class NFC:
    def read_card(self):
        print("读卡成功")

class rad:
    def control(self):
        print("红外开启成功")

class Myphone(Phone2023,rad,NFC):
    pass           #站位语法，无实际作用



phone=Myphone()
phone.control()