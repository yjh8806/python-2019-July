import os
import random as r
import time as t
class Playing:
    def __init__(self,deck):
        self.name = "player"
        self.deck = deck
    def show_deck(self):
        return self.deck
    def draw(self,enermy):
        if not self.deck or not enermy.deck:
            return
        print("상대 카드 매수 : %d"%(len(enermy.deck)))
        d=int(input("당신의 차례입니다. %s의 카드 중 하나를 골라주세요. (1 ~ %d 입력)"%(enermy.name,len(enermy.deck))))
        while True:
            if d < 1 or d > len(enermy.deck):
                os.system('cls')
                d = int(input("존재하지 않는 카드입니다 1 ~ %d 중에서 입력해주세요"%len(enermy.deck)))
            else:
                draw_card = enermy.deck[d-1]
                self.deck.append(draw_card)
                if draw_card == "JOKER":
                    print("ㄴㅇㄱ 상상도 못한 조커!")
                    t.sleep(3)
                    os.system("cls")
                else:
                    print("%s 를 뽑았습니다."%draw_card)
                    t.sleep(2)
                    for i in range(len(self.deck)-1):
                        if self.deck[i][1:] == draw_card[1:]:
                            print(self.deck[-1],self.deck[i])
                            self.deck.remove(self.deck[-1])
                            self.deck.remove(self.deck[i])
                            print("숫자가 같은 카드를 뽑았으므로 버립니다.")
                            print(self.deck)
                            t.sleep(2)
                            os.system("pause")
                            os.system("cls")
                            break
                enermy.deck.remove(draw_card)
                break
class Com_playing:
    def __init__(self,name,deck):
        self.name = name
        self.deck = deck
    def draw(self,enermy):
        if not self.deck or not enermy.deck:
            return
        if enermy.name == "player":
            print("%s이(가) 당신의 카드를 뽑는중입니다."%self.name)
            t.sleep(2)
            os.system("cls")
            com_select = r.randint(0,len(enermy.deck)-1)#컴퓨터가 뽑을 카드 고르기
            self.deck.append(enermy.deck[com_select])
            com_new_card = self.deck[-1]
            print("%s 이(가) %s를 뽑아갔습니다!"%(self.name,enermy.deck[com_select]))
            t.sleep(2)
            os.system("cls")
            enermy.deck.remove(enermy.deck[com_select])
        else:
            print("%s이(가) %s의 카드를 뽑는중입니다."%(self.name,enermy.name))
            com_select = r.randint(0,len(enermy.deck)-1)#컴퓨터가 뽑을 카드 고르기
            self.deck.append(enermy.deck[com_select])
            com_new_card = self.deck[-1]
            t.sleep(3)
            os.system("cls")
            enermy.deck.remove(enermy.deck[com_select])
        for i in range(len(self.deck)-1):
            if self.deck[i][1:] == com_new_card[1:]:
                self.deck.remove(self.deck[-1])
                self.deck.remove(self.deck[i])
                print("%s 이(가) 같은 숫자 카드를 냈습니다."%self.name)
                t.sleep(2)
                os.system("cls")
                break






def card_del(player):
    dellist = ["A ","2 ","3 ","4 ","5 ","6 ","7 ","8 ","9 ","10 ","K ","J ","Q "]
    while True: #같은 숫자 골라내기 player
        finish = 0
        i=0
        delcount = []
        double = input("""%s
        중에서 중복되는 숫자의 카드를 골라주세요."""%player)
        double = double + " " # 카드 이름 정규화
        while i<len(player):
            if double == player[i][1:]: ## 위 정규화를 double[1]로 개선 여지 있음
                delcount.append(player[i])
            i += 1
        if len(delcount) == 1 or len(delcount) == 0:
            print("같은 숫자 카드가 없습니다.")
            continue
        elif len(delcount) % 2 == 0:
            j=0
            while len(delcount)>0:
                if player[j] == delcount[0]:
                    delcount.remove(player[j])
                    player.remove(player[j])
                    j-=1
                j+=1
        elif len(delcount) % 2 == 1:
            j=0
            while len(delcount)-1 > 0:
                if delcount[0] == player[j]:# 여기 오류까지 고침
                    delcount.remove(player[j])
                    player.remove(player[j])
                    j-=1
                j+=1
        flag = False
        for i in range(len(dellist)):
            eqaul = 0
            for j in player:
                if j[1:]==dellist[i]:
                    eqaul +=1
                if eqaul >= 2:
                    flag = True
                    break
            if flag:
                break
            if i == len(dellist)-1:
                print("더 이상 같은 숫자가 없습니다.")
                return player #플레이어가 같은카드를 골라내는 함수
def com_card_del(com):
    dellist = ["A ","2 ","3 ","4 ","5 ","6 ","7 ","8 ","9 ","10 ","K ","J ","Q "]

    for i in range(len(dellist)):
        index = -1
        index2= -1
        count = 0
        for j in com:
            if j[1:]==dellist[i]:
                count +=1
                if index == -1:
                    index = com.index(j)
                elif index2 == -1:
                    index2 = com.index(j)
                    com.remove(com[index2])
                    com.remove(com[index])
            if count == 2:
                count = 0
                index = -1
                index2 = -1
        if i == len(dellist)-1:
            return com


     # 컴퓨터가 같은카드를 골라내는 함수
def gamestart():
    card = ["♠A ","♠2 ","♠3 ","♠4 ","♠5 ","♠6 ","♠7 ","♠8 ","♠9 ","♠10 ","♠J ","♠Q ","♠K ",
            "◆A ","◆2 ","◆3 ","◆4 ","◆5 ","◆6 ","◆7 ","◆8 ","◆9 ","◆10 ","◆J ","◆Q ","◆K ",
            "♣A ","♣2 ","♣3 ","♣4 ","♣5 ","♣6 ","♣7 ","♣8 ","♣9 ","♣10 ","♣J ","♣Q ","♣K ",
            "♥A ","♥2 ","♥3 ","♥4 ","♥5 ","♥6 ","♥7 ","♥8 ","♥9 ","♥10 " ,"♥J ","♥Q ","♥K ","JOKER"]
    os.system("cls")

    while True:
        os.system("cls")
        player = []

        computer1 = [] # 컴퓨터1 의 손패
        computer2 = [] # 컴퓨터2 의 손패
        while card: #카드배분
            randomcard = r.choice(card)
            player.append(randomcard)
            card.remove(randomcard)
            if len(card) < 1:
                break
            randomcard = r.choice(card)
            computer1.append(randomcard)
            card.remove(randomcard)
            if len(card) < 1:
                break
            randomcard = r.choice(card)
            computer2.append(randomcard)
            card.remove(randomcard)
            if len(card) < 1:
                break
        player=card_del(player)
        os.system("pause")
        os.system("cls")
        print("컴퓨터1이 같은카드를 골라내는 중입니다",end="")
        t.sleep(1)
        print(".",end="")
        t.sleep(1)
        print(".",end="")
        computer1=com_card_del(computer1)

        os.system("cls")
        print("컴퓨터2가 같은카드를 골라내는 중입니다",end="")
        t.sleep(1)
        print(".",end="")
        t.sleep(1)
        print(".",end="")
        computer2=com_card_del(computer2)




        os.system("cls")
        print("게임 시작!")
        t.sleep(3)
        player = Playing(player[0:])
        computer1 = Com_playing("컴퓨터1",computer1[0:])
        computer2 = Com_playing("컴퓨터2",computer2[0:])
        gameplayers = [player,computer1,computer2]
        rank = 1
        p = 0
        c1 = 0
        c2 = 0
        j=0
        players_rank = [0,0,0]# 0번째 인덱스 = 플레이어 ,1번째 = 컴퓨터1, 2번째 = 컴퓨터2
        while rank<3:
            print("""나의 패
            %s"""%player.show_deck())


            print("                                                            \t  상대 카드수:컴퓨터1=%d,컴퓨터2=%d"%(len(computer1.deck),len(computer2.deck)))
            print(computer1.deck)

            if j == len(gameplayers)-1:
                if len(gameplayers)-2 == 2:
                    gameplayers[j].draw(gameplayers[-1])
                else:
                    gameplayers[j].draw(gameplayers[0])

                if not gameplayers[j].deck:
                    if gameplayers[j].name == "player" and rank == 1 and p == 0:
                        print("축하합니다! 1등하셨습니다.")
                        t.sleep(2)
                        os.system("cls")
                        players_rank[0]=1
                        p=1
                        rank+=1
                        j=-1
                    elif gameplayers[j].name == "player" and p == 0:
                        print("당신은 %d등 하셨습니다."%rank)
                        t.sleep(2)
                        os.system("cls")
                        players_rank[0]=rank
                        p=1
                        rank+=1
                        j=-1
                    elif gameplayers[j].name == "컴퓨터1" and c1 == 0:
                        print("컴퓨터1이 %d등 하였습니다."%rank)
                        t.sleep(2)
                        os.system("cls")
                        players_rank[1] = rank
                        c1 = 1
                        rank+=1
                        j=0
                    elif gameplayers[j].name == "컴퓨터2" and c2 == 0:
                        print("컴퓨터2가 %d등 하였습니다."%rank)
                        t.sleep(2)
                        os.system("cls")
                        players_rank[2]=rank
                        c2 = 1
                        rank+=1
                        j=-1
                    gameplayers.remove(gameplayers[j])
                j=0
                continue



            else:
                gameplayers[j].draw(gameplayers[j+1])
                if not gameplayers[j].deck:
                    if gameplayers[j].name == "player" and rank == 1 and p == 0:
                        print("축하합니다! 1등하셨습니다.")
                        t.sleep(2)
                        os.system("cls")
                        players_rank[0]=1
                        p = 1
                        rank+=1
                        j=-1

                    elif gameplayers[j].name == "player" and p == 0:
                        print("당신은 %d등 하셨습니다."%rank)
                        t.sleep(2)
                        os.system("cls")
                        players_rank[0]=rank
                        p = 1
                        rank+=1
                        j=-1

                    elif gameplayers[j].name == "컴퓨터1" and c1 == 0:
                        print("컴퓨터1이 %d등 하였습니다."%rank)
                        t.sleep(2)
                        os.system("cls")
                        players_rank[1] = rank
                        c1 = 1
                        rank+=1
                        j=0

                    elif gameplayers[j].name == "컴퓨터2" and c2 == 0:
                        print("컴퓨터2가 %d등 하였습니다."%rank)
                        t.sleep(2)
                        os.system("cls")
                        players_rank[2]=rank
                        c2 = 1
                        rank+=1
                        j=0
                        gameplayers.remove(gameplayers[j])
                        continue
                    gameplayers.remove(gameplayers[j])

            j+=1
            if j > len(gameplayers):
                j=len(gameplayers)-1


        a=players_rank.index(0)
        players_rank[a] = 3
        os.system("cls")
        print(computer1.deck)
        print(computer2.deck)
        print('''최종점수
        플레이어:%d
        컴퓨터1:%d
        컴퓨터2:%d'''%(players_rank[0],players_rank[1],players_rank[2]))
        os.system("pause")
        os.system("cls")
        return players_rank



while True:
    sw = int(input("""★★★★★★도둑잡기 게임★★★★★★
                1.게임 시작
                2.전적
                3.종료
             """))
    if sw == 1:
        score = gamestart()
    elif sw == 2:
        if not score:
            print("진행된 게임이 없습니다.")
        elif score:
            os.system("cls")
            print("플레이어 : %d, 컴퓨터1 : %d, 컴퓨터2 : %d"%(score[0],score[1],score[2]))
            os.system("pause")
            os.system("cls")
    elif sw==3:
        os.system("cls")
        print("게임종료")
        exit()
