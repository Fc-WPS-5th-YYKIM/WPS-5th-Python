class Monster():
    description = 'pokemon'
    hp = 100
    dash_dmage = 10
    def __init__(self, name):
        self.name = name

    def attack(self, enemy):
        enemy.hp -= self.dash_dmage
        print('{}는 {}에게 {}의 피해를 줬다!!!'.format(self.name, enemy.name, enemy.dash_dmage))

    @staticmethod
    def run():
        print('도망치기')

    @classmethod
    def change_type(cls, description):
        cls.description = description

ggobugi = Monster('ggobugi')
pikachu = Monster('pikachu')

ggobugi.attack(pikachu)
print(pikachu.hp)

pikachu.run()

agumon = Monster('agumon')
print(agumon.description)
agumon.change_type('digimon')
print(agumon.description)

print(ggobugi.description)