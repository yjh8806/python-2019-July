import os
import random as r
minname=""
minday = 0
day = 1

class User: #플레이어를 생성하는 클래스
    def __init__(self):
        self.fruit_list = []
        self.fruit_list_kor = []
        self.name = "" #닉네임
        self.money = 50000  #초기자금
        self.debt = 500000 #부채
    def new_name(self, name): #이름을 열글자까지만 저장하는 함수
        self.name = name[0:10]
    def in_out_money(self,money,sign): #초기자금 입력 함수
        if sign == "+":
            self.money += money
        else:
            self.money -= money
    def in_out_debt(self,debt,sign): #부채 입력 함수
        if sign == "+":
            self.debt += debt
        else:
            self.debt -= debt

class Fruit: #과일 가격, 수확시 가치, 수확성공할 확률
    def __init__(self, fruit, cost, value, percentage,count):
        self.fruit = fruit
        self.cost = cost
        self.value = value
        self.percentage = percentage #확률은 1~100
        self.count = count
    def store_print(self):
        print("%-10s %-10s   %-20s"%(self.fruit, self.cost, self.value))

def store(player): #과일종류들(Fruit 클래스 사용)
    peach = Fruit("복숭아", 3500, 11000, 60,100)
    watermelon = Fruit("수박", 5500, 25500, 30,100)
    grape = Fruit("포도", 3000, 13000, 50, 100)
    korean_melon = Fruit("참외", 5000, 20000, 40,100)
    plum = Fruit("자두", 4000, 12000, 55,100)
    cucumber = Fruit("오이", 3000, 8000, 75,100)
    greenpumpkin = Fruit("애호박", 4000, 12000, 60,100)
    potato = Fruit("감자", 3000, 10000, 65,100)
    pepper = Fruit("고추", 1000, 4000, 90,100)
    lettuce = Fruit("상추", 2000, 7000, 80,100)
    #객체가 들어간 리스트
    fruit_list = [peach, watermelon, grape, korean_melon, plum, cucumber, greenpumpkin, potato, pepper, lettuce]

    #메뉴판
    print("%-10s %-5s %-10s"%("종류","구입가격","수확성공후_가치"))
    peach.store_print()
    watermelon.store_print()
    grape.store_print()
    korean_melon.store_print()
    plum.store_print()
    cucumber.store_print()
    greenpumpkin.store_print()
    potato.store_print()
    pepper.store_print()
    lettuce.store_print()

    #구매할 과일종류, 개수 입력받기
    fruit_list2=[]
    for i in fruit_list: #과일객체의 이름을 저장
        fruit_list2.append(i.fruit)
    while True:
        choice = input("구매하실 과일 입력 : ")
        if choice in fruit_list2:
            break
        else:
            print("잘못입력! 재입력바람")
    while True:
        count = int(input("개수 : "))
        thing = fruit_list[fruit_list2.index(choice)]
        price = thing.cost * count
        if price <= player.money:
            print("지불하신 금액은 %s원입니다."%price)
            break
        else:
            print("돈이 모자람")
    if count > 0:
        if choice in player.fruit_list_kor:
            fIndex = player.fruit_list_kor.index(choice)
            player.fruit_list[fIndex].count = player.fruit_list[fIndex].count + count
        else:
            thing = Fruit(choice,thing.cost, thing.value, thing.percentage, count)
            player.fruit_list.append(thing)
            player.fruit_list_kor.append(choice)
    player.in_out_money(price,"-")
    print("구매하신 과일 : %s, 개수 : %s, 남은 현금 : %s"%(choice, count, player.money))

# def groud(using): #땅
#     row1 = using // 10
#     row2 = using % 10
#     for j in range(row1):
#         print("■"*10)
#     print("■"*row2,end="")
#     print("□"*(10 - row2))
#     for k in range(10 - row1 - 1):
#         print("□"*10)
#     print("사용하고있는 땅은 100칸 중 총 %d칸입니다."%using)

def myfarm(player):
    os.system("cls")
    global day #day는 외부변수와 연동하기 위해 global로 선언
    using = 0 #사용중인 땅
    revenue = 0 #현금 임시보관용(수익) : 메뉴 나갈땐 항상 0이어여함
    while(True):
        print("===%s일차 내 농장===\n"%day)
        a =(30-using)
        print("사용가능한 땅 : %d / 30"%a)
        print("보유 작물 : ")
        for i in player.fruit_list:
            print("%s(%s개)"%(i.fruit,i.count),end=" ")
        print()
        print("1. 농사짓기")
        print("2. 오늘 일과 끝내기")
        run_menuF = input(">>") #엔터를 치면 int로 못바꾸니까... => 문자열로 받고 문자열로 비교
        if run_menuF == '1':
            farming = input("심을 작물을 골라주세요 : ")
            if farming in player.fruit_list_kor:
                while True:
                    fmn = int(input("몇개를 심을까요? : "))
                    if fmn > player.fruit_list[player.fruit_list_kor.index(farming)].count or a-fmn<0 :
                        print("개수가 초과되었습니다.")
                    else:
                        using += fmn
                        a= player.fruit_list[player.fruit_list_kor.index(farming)].percentage
                        success_count = 0 #성공한 과일 갯수
                        for i in range(fmn):
                            b = r.randint(1,100)
                            if b < a:
                                success_count +=1
                        print("%s개 수확"%success_count)
                        revenue += success_count * player.fruit_list[player.fruit_list_kor.index(farming)].value
                        #사용한 개수만큼 차감
                        player.fruit_list[player.fruit_list_kor.index(farming)].count -= fmn
                        #개수가 0개라면 plyaer(User클래스)에 저장했던 fruit 삭제
                        if player.fruit_list[player.fruit_list_kor.index(farming)].count == 0:
                            player.fruit_list.remove(player.fruit_list[player.fruit_list_kor.index(farming)])
                            player.fruit_list_kor.remove(farming)
                        break
            else:
                print("작물이 없습니다.")

        elif run_menuF == '2':
            print("%d일차 종료입니다."%day)
            print("오늘 수익은 %d원입니다."%revenue)
            if revenue >0:
                while True:
                    pdebt = int(input("돈을 얼마나 갚을까요?"))
                    if pdebt<=revenue:
                        player.in_out_debt(pdebt,"-")
                        player.in_out_money(revenue - pdebt, "+")
                        break
                    else:
                        print("다시 입력")
            if player.debt <= 0:
                print("빚이 0원입니다.")
                global minday
                global minname
                if minday > day or minday == 0:
                    print("최고기록갱신")
                    minname = player.name
                    minday = day
                print("%d일만에 빚을 다 갚았습니다."%day)
            else:
                day += 1
            break
        else:
            print("잘못 입력")
        os.system("pause")
        os.system("cls")

def Run_game(): #게임함수
    player = User()
    you = str(input("이름입력(10자리 이내) : "))
    player.new_name(you)
    os.system("cls")
    while(True):
        if player.debt == 0:
            break
        print("%s님의 농장"%player.name)
        print("현재 현금 : %s"%player.money)
        print("현재 부채 : %s"%player.debt)
        print("1. 상점가기")
        print("2. 농장가기")
        run_menu = int(input(">>"))
        if run_menu == 1:
            store(player)
            os.system("pause")
            os.system("cls")
        elif run_menu ==2:
            myfarm(player)
            os.system("pause")
            os.system("cls")
        else:
            os.system("cls")



while True: #메인함수
    print("농장게임")
    print("1.게임시작")
    print("2.게임방법")
    print("3.랭킹")
    print("4.종료")
    menu = int(input(">>"))
    if menu == 1:
        print("게임시작")
        Run_game()
        os.system("pause")
        os.system("cls")
    elif menu == 2:
        print("게임방법")
        print("""
        작물을 키워서 빚을 갚아라!
        초기자금으로 작물종자를 구매해서 빚을 갚는 게임입니다.
        1. 상점에서 작물을 구입한다.
        2. 농장에 가서 심는다.
        3. 작물을 팔아서 돈을 번다.
        * 각 작물마다 종자가격, 판매금액, 그리고 농사 실패확률이 다릅니다.
        * 운이 좋다면 비싼 작물만 재배해서 큰 돈을 만질수도 있지만...
        """)
        os.system("pause")
        os.system("cls")
    elif menu == 3:
        print("랭킹")
        if minday == 0:
            print("아직 기록이 없습니다.")
        else:
            print("최고기록은 %s님의 %d일입니다."%(minname,minday))
        os.system("pause")
        os.system("cls")
    elif menu == 4:
        print("종료")
        exit(0)
    else:
        print("잘못입력")
        os.system("pause")
        os.system("cls")
