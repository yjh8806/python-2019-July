import random
import os
#플레이어 레벨
class ArrplayerLevel1:
    def __init__(self):
        self.money = 10000
    def Money(self):
        return self.money
    def sub(self,n1):
        self.money -= n1
        return self.money
    def sum(self,n2):
        self.money += n2
class ArrplayerLevel2(ArrplayerLevel1):
    def __init__(self):
        self.money = 50000
class ArrplayerLevel3(ArrplayerLevel1):
    def __init__(self):
        self.money = 100000
class ArrplayerLevel4(ArrplayerLevel1):
    def __init__(self):
        self.money = 1000000
class ArrplayerLevel5(ArrplayerLevel1):
    def __init__(self):
        self.money = 10000000

#카드 클래스
#플레이어용
class plKd:
    def __init__(self,de):
        self.cards = [ de[k] for k in range(0, 2)]
    def car(self,n3):
        self.cards.append(n3)
    def ret(self):
        return self.cards
#컴터카드
class cmKd(plKd):
    def __init__(self,de):
        self.cards = [ de[k] for k in range(2, 4)]

#플러쉬확인용 클래스
class Sp():
    def __init__(self,de):
        self.de = de
    def fmo(self):
        if self.de.count("♠") == 5:
            return 5
class Lo(Sp):
    def fmo(self):
        if self.de.count("♥") == 5:
            return 5
class Di(Sp):
    def fmo(self):
        if self.de.count("♦") == 5:
            return 5
class Ch(Sp):
    def fmo(self):
        if self.de.count("♣") == 5:
            return 5
# 카드 순위 따지는 코드
def CardRank(cards):
    paircount = 0
    for n1 in range(0,len(cards)):
        for n2 in range(n1+1,len(cards)):
            if cards[n1][1] == cards[n2][1] :
                paircount += 1
    num = [cards[k][1] for k in range(len(cards))]
    num.sort()
    straightox = False
    if paircount == 0 and len(cards) >= 5:
        if (num[4]-num[0]) == 4:
            straightox = True
        if num[0] == 1 and num[1] == 10:
            straightox = True
    suit = [cards[k][0] for k in range(len(cards))]
    suit.sort()
    flushox = False
    sp = Sp(suit)
    lo = Lo(suit)
    di = Di(suit)
    ch = Ch(suit)

    if sp.fmo() == 5:
        flushox = True
    elif lo.fmo() == 5:
        flushox = True
    elif di.fmo() == 5:
        flushox = True
    elif ch.fmo() == 5:
        flushox = True
    if straightox and flushox:
        rank = 1
    elif paircount == 6:
        rank = 2
    elif paircount == 4:
        rank = 3
    elif flushox:
        rank = 4
    elif straightox:
        rank = 5
    elif paircount == 3:
        rank = 6
    elif paircount == 2:
        rank = 7
    elif paircount == 1:
        rank = 8
    else:
        rank = 9
    return rank
def ageMoney(n1,n2,n3,n4):
    print("computer Money : %s\n"%n1)
    print("computer: %s\n"%n2)
    print("player  : %s\n"%n3)
    print("player Money : %s\n"%n4)
def Rank(n1):
    if n1 == 1:
        return "★★★스트레이스 플러쉬★★★"
    elif n1 == 2:
        return "★★포카드★★"
    elif n1 == 3:
        return "★풀하우스★"
    elif n1 == 4:
        return "플러쉬"
    elif n1 == 5:
        return "스트레이트"
    elif n1 == 6:
        return "트리플"
    elif n1 == 7:
        return "투페어"
    elif n1 == 8:
        return  "원페어"
    elif n1 == 9:
        return "노페어"
while True:
    # 카드 한 팩을 만든다.
    deck = [(suit, k) for  suit in ["♠", "♥", "♦", "♣"] for k in range(1,14)]
    os.system("cls")
    level = int(input("""Level 1 = 10,000원 \t배팅금액 100 ~ 500원
Level 2 = 50,000원 \t배팅금액 500 ~ 3,000원
Level 3 = 500,000원 \t배팅금액 3,000 ~ 10,000원
Level 4 = 5,000,000원 \t배팅금액 10,000 ~ 100,000원
Level 5 = 10,000,000원 \t배팅금액 100,000 ~ 500,000원

Level을 숫자만 입력하시오 :"""))
    if level == 1:
        money = ArrplayerLevel1()
        comMoney = ArrplayerLevel1()
    elif level == 2:
        money = ArrplayerLevel2()
        comMoney = ArrplayerLevel2()
    elif level == 3:
        money = ArrplayerLevel3()
        comMoney = ArrplayerLevel3()
    elif level == 4:
        money = ArrplayerLevel4()
        comMoney = ArrplayerLevel4()
    elif level == 5:
        money = ArrplayerLevel5()
        comMoney = ArrplayerLevel5()
    else:
        print("잘못누르셧습니다 다시 돌아갑니다")
        os.system("pause")
        os.system("cls")
        continue
    # 게임을 반복한다
    while True:
        os.system("pause")
        os.system("cls")
        # 카드를 섞는다.
        random.shuffle(deck)
        arr = 0
        # 배팅 1,2,3,4,5
        for i in range(1,8):
            print("""족보
            1.스트레이트 플러쉬 = 5장의 그림이 같고 숫자의 순서가 일정할시?
            예 ) ♠1 ♠2 ♠3 ♠4 ♠5 ♣5 ♦1

            2.포카드 = 같은숫자가 4장일때
            예 ) ♠1 ♥1 ♦1 ♣1 ♣5 ♦3 ♣4

            3.풀하우스 = 3장의 카드가 같은 숫자이면서 2장의 숫자가 같은숫자일때
            예 ) ♠1 ♥1 ♦1 ♣5 ♣5 ♦3 ♣4

            4.플러쉬 = 5장의 그림이 같을때
            예 ) ♠1 ♠7 ♠8 ♠4 ♠5 ♦3 ♣4

            5.스트레이트 = 숫자의순서가 일정할시?
            예 ) ♠1 ♥2 ♦3 ♣4 ♣5 ♠8 ♣10

            6.트리플 = 같은숫자가 3장일때
            예 ) ♠1 ♥1 ♦1 ♣4 ♣5 ♣3 ♣7

            7.투페어 = 같은숫자가 2장인 세트가 2세트일때
            예 ) ♠1 ♥1 ♦3 ♣3 ♣5 ♣7 ♣10

            8.원페어 = 같은숫자가 2장인 세트가 1세트일때
            예 ) ♠1 ♥1 ♦3 ♣4 ♣5 ♣7 ♣10

            9.노페어 = 같은숫자가 없을시\n
            컴터는 3장까지 오픈함\n""")
            rand = 0
            if i < 7:
                print("===%d턴==="%i)
            if i == 1:
                cards_A = cmKd(deck) # 컴퓨터
                cards_B = plKd(deck)  # 선수
                rank_A = CardRank(cards_A.ret())
                rank_B = CardRank(cards_B.ret())
            elif i < 3:
                cards_A.car(deck[i*2])
                cards_B.car(deck[i*2+1])
                rank_A = CardRank(cards_A.ret())
                rank_B = CardRank(cards_B.ret())
            #컴퓨터는 3장까지 오픈함
            elif i == 3:
                hidd = deck[i*2]
                cards_B.car(deck[i*2+1])
                rank_B = CardRank(cards_B.ret())
            elif i == 4:
                hiddencard = deck[i*2]
                cards_B.car(deck[i*2+1])
                rank_B = CardRank(cards_B.ret())
            elif i == 5:
                hidde = deck[i*2]
                cards_B.car(deck[i*2+1])
                rank_B = CardRank(cards_B.ret())
            elif i == 6:
                hidden = deck[i*2]
                cards_B.car(deck[i*2+1])
                rank_B = CardRank(cards_B.ret())
            else:
                cards_A.car(hiddencard)
                cards_A.car(hidd)
                cards_A.car(hidde)
                cards_A.car(hidden)
                rank_A = CardRank(cards_A.ret())
                rank_B = CardRank(cards_B.ret())
                if rank_B < rank_A:
                    money.sum(arr)
                    print("컴퓨터 : %s"%(Rank(rank_A)))
                    ageMoney(comMoney.Money(),cards_A.ret(),cards_B.ret(),money.Money())
                    print("플레이어 : %s"%(Rank(rank_B)))
                    print('당신이 이겼습니다.')
                    print("player Money + %d\n"%arr)
                    break
                elif rank_B == rank_A:
                    print('비겼습니다')
                    print("컴퓨터 : %s"%(Rank(rank_A)))
                    ageMoney(comMoney.Money(),cards_A.ret(),cards_B.ret(),money.Money())
                    print("플레이어 : %s\n"%(Rank(rank_B)))
                    break
                else:
                    comMoney.sum(arr)
                    print('컴퓨터가 이겼습니다.')
                    print("computer Money + %d"%arr)
                    print("컴퓨터 : %s\n"%(Rank(rank_A)))
                    ageMoney(comMoney.Money(),cards_A.ret(),cards_B.ret(),money.Money())
                    print("플레이어 : %s\n"%(Rank(rank_B)))
                    break
            print("컴퓨터 : %s"%(Rank(rank_A)))
            ageMoney(comMoney.Money(),cards_A.ret(),cards_B.ret(),money.Money())
            print("플레이어 : %s"%(Rank(rank_B)))
            answer = input("배팅하시겠습니까? (y/n) :")
            if answer == 'n' or answer == 'N':
                break
            elif answer == 'y' or answer == 'Y':
                pass
            else:
                print("너님 잘못누름 팅")
                exit(0)
            #배팅금액
            if level == 1:
                rand = random.randint(100,500)
                age = random.randint(100,500)
            elif level == 2:
                rand = random.randint(500,3000)
                age = random.randint(500,3000)
            elif level == 3:
                rand = random.randint(3000,10000)
                age = random.randint(3000,10000)
            elif level == 4:
                rand = random.randint(10000,100000)
                age = random.randint(10000,100000)
            elif level == 5:
                rand = random.randint(100000,500000)
                age = random.randint(100000,500000)
            if age > money.Money():
                os.system("pause")
                os.system("cls")
                print("너님 졋음 집에가셈 대출안됨")
                break
            elif rand > comMoney.Money():
                os.system("pause")
                os.system("cls")
                print("너님 이김 더 꼴기전에 본전뽑았으면 집에 가셈")
                break
            arr += age + rand
            money.sub(age)
            comMoney.sub(rand)
            os.system("pause")
            os.system("cls")
        answer = input("게임을 더 하시겠습니까? (y/n) :")
        if answer == 'n' or answer == 'N':
            exit(0)
        elif answer == 'y' or answer == 'Y':
            if age > money.Money():
                os.system("pause")
                os.system("cls")
                print("너님 돈없음 처음부터")
                break
            elif rand > comMoney.Money():
                os.system("pause")
                os.system("cls")
                print("컴터 돈없음 처음부터")
                break
            else:
                continue
        else:
            print("너님 잘못누름 팅")
            exit(0)
