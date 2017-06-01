import time
import random


class Iamhungry:
    def __init__(self, name, money):
        self.__name = name
        self.__money = money

    def check_money(self):
        print('현재 {}의 지갑에 {}원이 남아있다.'.format(self.__name, self.__money))

    def move(self, target):
        print('{}는 {}으(로) 이동한다.'.format(self.__name, target))

    def alarm_msg(self):
        print('입점 대기중 입니다.')

    def money_msg(self):
        print("잔액이 부족합니다.")

    def play(self):
        print('========= 시작 =========')
        while True:
            print('1: 잔액 확인\n2. 편의점\n3. PC방\n4. 패스트 푸드\n5. 집으로')
            turn_num = input('다음 행동을 입력하세요 : ')
            if turn_num == '1':
                self.check_money()
            elif turn_num == '2':
                print("구매할 물품을 선택하세요")
                product_num = input('1: 햄버거\n2. 삼각김밥\n3. 컵라면\n4. 콜라\n5. 나가기')
                if product_num == '1':
                    print("햄버거를 구매하셨습니다. 금액은 1500원 입니다.")
                    if self.__money < 1500:
                        self.money_msg()
                    else:
                        self.__money = self.__money - 1500
                elif product_num == '2':
                    print("삼각김밥를 구매하셨습니다. 금액은 900원 입니다.")
                    if self.__money < 900:
                        self.money_msg()
                    else:
                        self.__money = self.__money - 900
                elif product_num == '3':
                    print("컵라면를 구매하셨습니다. 금액은 1200원 입니다.")
                    if self.__money < 1200:
                        self.money_msg()
                    else:
                        self.__money = self.__money - 1500
                elif product_num == '4':
                    print("콜라를 구매하셨습니다. 금액은 950원 입니다.")
                    if self.__money < 950:
                        self.money_msg()
                    else:
                        self.__money = self.__money - 950
                elif product_num == '5':
                    print("편의점을 나왔습니다")
                    break

            elif turn_num == '3':
                self.alarm_msg()

            elif turn_num == '4':
                self.alarm_msg()

            elif turn_num == '5':
                break

hungry = Iamhungry("용연",10000)
hungry.play()