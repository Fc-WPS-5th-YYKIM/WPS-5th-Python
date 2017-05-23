'''
상위 폴더에 우클릭 -> Mark Directory as... -> Sources Root
'''

from class_sample import Shop, PCroom
from class_sample import User, Something, Food, Drink

lotteria = Shop('Lotteria', '패스트푸드', '신사역')
xeno = PCroom('제노','PC방','신사역')

xeno.shop_info()

user = User('김용연')
s = Something('알수없는 무언가')
f = Food('햄버거')
d = Drink('콜라')

user.eat_something(s)
user.eat_food(f)
user.eat_drink(d)