"""
public : 외부에서 제한없이 접근/수정 가능

protected : 외부에서는 접근 불가능, 상속 받은 클래스 에서는 접근 가능

private : 내부에서만 접근 / 수정 가능
            -> 외부 접근 가능하도록 property 사용

변수 혹은 메소드의 이름의 시작이 _ 한개 라면 관용적으로(실제로는 public) protected,
__ 두개 라면 private 이기 때문에 _로 함부로 시작해서는 안된다.
"""

class Shop:

    description = 'Python Shop Class'

    def __init__(self, name, shop_type, address):
        self.name = name
        self._shop_type = shop_type
        self.address = address


    def shop_info(self):
        print('[ 상점정보 ]\n 상호명 : {}\n 유형 : {}\n 주소 : {}'.format(self.name, self._shop_type, self.address))

    def change_type(self, shop_type):
        self._shop_type = shop_type

    @classmethod
    def change_description(cls, description):
        cls.description = description

    @staticmethod
    def print_hello():
        print('hello')


    @property
    def shop_type(self):
        return self._shop_type

    @shop_type.setter
    def shop_type(self, shop_type):
        self._shop_type = shop_type


class PCroom(Shop):

    def __init__(self, name, shop_type, address, price):
        super().__init__(name, shop_type, address)
        self.price

    def shop_info(self):
        print('[ 상점정보 ]\n 상호명 : {}\n 유형 : {} [ {} ]\n 주소 : {}'.format(self.name, self._shop_type, self.name, self.address))

# 다형성 및 덕타이핑
# 다형성 : 동일한 실행이지만 다른 동작을 수행할 수 있도록 허용하는 것


class User:
    def __init__(self, name):
        self.name = name

    def eat_something(self, something):
        something.eat()

    def eat_food(self, food):
        food.eat()

    def eat_drink(self, drink):
        drink.eat()

class Something:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print('{}는 무엇인지 몰라 먹을 수 없다!')

class Food:
    def eat(self):
        print('{}을 먹었다 배가부르다!')

class Drink:
    def eat(self):
        print('{}을 마셨다 갈증이 해소된다!')