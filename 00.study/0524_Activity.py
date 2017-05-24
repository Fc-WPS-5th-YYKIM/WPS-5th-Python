class Hamburger():
    def __init__(self, name, price, calorie):
        self.name = name
        self.__price = price
        self.calorie = calorie

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price):
        self.__price = price


class Mcdonald(Hamburger):

    def __init__(self, name, price, calorie, setType):
        super().__init__(name, price, calorie)
        self.setType = setType

        if setType == True:
            self.price += 1500
            self.calorie += 150




hamburger = Hamburger('bulgogibuger', 5500, 450)
print(hamburger.price)
hamburger.price = 5000

print('{}의 가격이 {} 변경 되었습니다.'.format(hamburger.name, hamburger.price))
'''
bigmac = Mcdonald('bicmac', 5500, 450, True)
bigmac.price = 5000

print(bigmac.price)
'''