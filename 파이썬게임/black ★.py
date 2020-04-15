import random
import os
#0은 인덱스를 맞추기 위함
card = {0:"null", 1: "ace", 2:"two", 3:"three", 4:"four", 5:"five", 6:"six", 7:"seven", 8:"eight", 9:"nine", 10:"ten", 11:"jack", 12:"queen", 13:"king"}
dealer_cards = []
player_cards = []
dealer_cards_display = []
player_cards_display = []
class Game:
    def __init__(self):
        self.initalDraw()
        self.initalDisplay()
        self.points()
        self.draw()
        self.evaluation()

    def initalDraw(self):
        while len(dealer_cards) != 2:
            d_card = random.randint(1, len(card)-1)
            dealer_cards.append(d_card)
            dealer_cards_display.append(d_card)
        while len(player_cards) != 2:
            p_card = random.randint(1, len(card)-1)
            player_cards.append(p_card)
            player_cards_display.append(p_card)

    def initalDisplay(self):
        print("The dealer has {0}".format(card[dealer_cards_display[1]]))
        print("You have {0} and {1}".format(card[player_cards_display[0]], card[player_cards_display[1]]))

    def points(self):
        for i in range(0, len(dealer_cards)):
            if dealer_cards[i] > 10:
                dealer_cards[i] = 10
        for i in range(0, len(player_cards)):
            if player_cards[i] > 10:
                player_cards[i] = 10

    def draw(self):
        global a
        global b
        while sum(dealer_cards) < sum(player_cards) and sum(player_cards) <= 21:
            d_card = random.randint(1, len(card)-1)
            dealer_cards.append(d_card)
            dealer_cards_display.append(d_card)
            self.points()
            b = []
            for i in dealer_cards_display:
                b.append(card[i])
        while sum(player_cards) < 21:
            action = input("press [h]it or [s]tand : ")
            if action.upper() == "H":
                p_card = random.randint(1, len(card)-1)
                player_cards.append(p_card)
                player_cards_display.append(p_card)
                self.points()
                a = []
                for i in player_cards_display:
                    a.append(card[i])
                print(a)
            elif action.upper() == "S":
                a = []
                for i in player_cards_display:
                    a.append(card[i])
                b = []
                for i in dealer_cards_display:
                    b.append(card[i])
                break
            else:
                print("잘못입력하셨습니다.")
                exit(0)

    def evaluation(self):
        global a
        global b
        if sum(dealer_cards) == 21 and sum(player_cards) == 21:
            print("딜러 : ", b, "합 :", sum(dealer_cards), "\n플레이어 : ", a, "합 :", sum(player_cards))
            print("딜러와 플레이어는 둘다 블랙잭입니다.")
        elif sum(dealer_cards) == 21:
            print("딜러 : ", b, "합 :", sum(dealer_cards), "\n플레이어 : ", a, "합 :", sum(player_cards))
            print("딜러가 블랙잭으로 이겼습니다")
            winner = "player"
        elif sum(player_cards) == 21:
            print("딜러 : ", b, "합 :", sum(dealer_cards), "\n플레이어 : ", a, "합 :", sum(player_cards))
            print("플레이어가 블랙잭으로 이겼습니다")
        elif sum(dealer_cards) > 21:
            print("딜러 : ", b, "합 :", sum(dealer_cards), "\n플레이어 : ", a, "합 :", sum(player_cards))
            print("플레이어가 이겼습니다")
        elif sum(player_cards) > 21:
            print("딜러 : ", b, "합 :", sum(dealer_cards), "\n플레이어 : ", a, "합 :", sum(player_cards))
            print("딜러가 이겼습니다")
        else:
            if sum(dealer_cards) > sum(player_cards):
                print("딜러 : ", b, "합 :", sum(dealer_cards), "\n플레이어 : ", a, "합 :", sum(player_cards))
                print("딜러가 이겼습니다")
            elif sum(player_cards) > sum(dealer_cards):
                print("딜러 : ", b, "합 :", sum(dealer_cards), "\n플레이어 : ", a, "합 :", sum(player_cards))
                print("플레이어가 이겼습니다")

Game()

qq = input("\n다시하시겠습니까? [y/n] : ")
while qq == 'y':
    os.system("pause")
    os.system("cls")
    card = {0:"null", 1: "ace", 2:"two", 3:"three", 4:"four", 5:"five", 6:"six", 7:"seven", 8:"eight", 9:"nine", 10:"ten", 11:"jack", 12:"queen", 13:"king"}
    dealer_cards = []
    player_cards = []
    dealer_cards_display = []
    player_cards_display = []
    Game()
    qq = input("\n다시하시겠습니까? [y/n] : ")
exit(0)
