from chap09 import Restaurant

class IceCreamStand(Restaurant):

    def __init__(self, rname, rtype, *flavors):
        super().__init__(rname, rtype)
        self.flavors = list(flavors)

    def showFlavors(self):
        print(f"맛을 출력합니다 : {self.flavors}")
        print("맛을 출력합니다 : {}".format(self.flavors))        
        print(type(self.flavors))

ics = IceCreamStand("무인", "아이스크림점","사과","딸기","메론","수박")
ics.showFlavors()