import sys
from functions.game import play_game, title as game_title
from functions.shop import buy_item, title as shop_title
from friends.chat import send_message
#import game
#import shop

title = 'Main Module'

def turn_on():
    print('= Turn on game =')

    while True:
        choice = input('What would tou like to do?\\n  1: Go to Shop, 2: Play Game, 3: Send to Message, 0: Exit\\n   Input : ')
        if choice == '0':
            break
        elif choice == '1':
            buy_item()
        elif choice == '2':
            play_game()
        elif choice == '3':
            send_message()
        else:
            print('Choice not exist')
        print('------------------------------------')

    print('= Turn off game =')



if __name__ == '__main__':
    #print(sys.argv)
    #print('= Start game =')
    #print(title)
    #print(game_title)
    #print(shop_title)
    #play_game()
    #buy_item()
    turn_on()


