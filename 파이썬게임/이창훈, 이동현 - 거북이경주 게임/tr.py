import turtle as t
import random as r
import time,os
global turtlecount
#그래픽환경 구현

abc=[1000] # 지갑

class turtlegame: #거북이 클래스
    def __init__(self):
        t.TurtleScreen._RUNNING = True # 터틀스크린 러닝
        self.batting() #배팅, 거북이선택
        self.fencing() #경기장
        self.tutlesetting() # 거북이 출발선
        self.turtle_move() #거북이 움직임
        self.account()

        self.bye() #경기 종료
        input('[press enter to go back to main menu]') #게임 끝난 후 메인메뉴로 돌아가기

    def batting(self): #배팅화면
        self.wallet=abc[0]
        self.money = 0 #배팅할 머니 초기 변수
        print("Your Wallet : %s\n"%self.wallet)
        print("Turtle list\n\n%s"%turtlelist[:(turtlecount)]) #거북이 선택 마리 수만큼 이름 리스트 출력
        print()
        global playerturtle
        feature= "Sam is smart Turtle     \nmatt is handsome Turtle \nsong is healthy Turtle  \nthunder is speedy Turtle"
        featureslice = feature[:turtlecount*25] # 거북이선택한 만큼 나오도록 설정
        print(featureslice)
        print()
        endd=0 #오류시 다시 와일문 처음으로 돌아가기 위한 변수
        while endd==0:
            playerturtle=input("Choise turtle to go batting. :")
            if playerturtle not in turtlelist:
                print(playerturtle,"\n")
                print("Please enter the turtle in the list\n")
            elif playerturtle in turtlelist:
                endd+=1
        self.money=int(input("betting money :")) # 배팅 머니 입력
        while self.money > self.wallet: #지갑보다 배팅금액이 적으면 출력
            print("have no money in your wallet")
            self.money=int(input("betting money"))

    def fencing(self): #경기장설정
        wn=t.Screen()
        wn.bgcolor("White") #터틀모듈 화면 설정
        fence=t.Turtle()
        goalline=t.Turtle()
        fence.penup()
        goalline.penup()
        fence.setposition(-300,-100)
        goalline.setposition(280,200)
        fence.pendown()
        goalline.pendown()
        fence.pensize(3)
        goalline.pensize(3)
        for i in range(2):
            fence.forward(600)
            fence.left(90)
            fence.forward(300)
            fence.left(90)
            goalline.rt(90)
            goalline.fd(300)
            fence.ht()
            goalline.ht()
    def tutlesetting(self): #거북이 처음 셋팅
            for i in range(turtlecount):
                turtlelist[i]=t.Turtle()
                turtlelist[i].shape("turtle")
                turtlelist[i].color(turtlecolor[i])
                turtlelist[i].penup()
                turtlelist[i].setposition(-280,140-(i*60))



    def turtle_move(self): #거북이 움직임 설정
        raceend=0

        while raceend!=1:
            for i in range(turtlecount): #골인 시 리스트 인덱스 리스트 2에서 받은 후 변환 후 값을 리턴
                if turtlelist[i].xcor()>270:
                    raceend+=1
                    turtlelist[i]=turtlelist2[i] #변환된 터틀 리스트의 값을 터틀 리스트 2에서 받아와 다시 변환
                    time.sleep(1)

                    return goal.append(turtlelist[i]) # 골 리스트에 추가

                #울타리 닿이면 돌아가도록 설정
                if turtlelist[i].xcor() < -295:
                    turtlelist[i].rt(180)
                    turtlelist[i].fd(15)
                if turtlelist[i].ycor()<-95:
                    turtlelist[i].rt(180)
                    turtlelist[i].fd(15)
                if turtlelist[i].ycor()>195:
                    turtlelist[i].rt(180)
                    turtlelist[i].fd(15)
                #거북이 움직임
                turtlelist[i].setheading(0)
                if r.randint(1,2) % 2==0:
                    turtlelist[r.randint(0,int(turtlecount)-1)].rt(r.randint(20,110))
                else:
                    turtlelist[r.randint(0,int(turtlecount)-1)].lt(r.randint(20,110))
                turtlelist[i].fd(r.randint(10,20))

    def bye(self): #승리 거북이 텍스트로 알린 뒤 터틀 모듈 나오기
        tt=t.Turtle()
        tt.ht()
        t.clearscreen()
        t.reset()
        t.write("★%s turtle win .★"%(goal[0]),False,"center",("",20))
        time.sleep(2)
        t.bye() #화면 아웃
        t.Turtle._screen = None #터틀모듈 초기화 종료
    def account(self): #정산 함수
        os.system("cls")
        print("Selected Turtle : %s\n"%playerturtle)
        print("Battingmoney : %s\n"%(self.money))
        if goal[0]==playerturtle:
            self.wallet+=(self.money*turtlecount)
            print("%s Turtle Win!! %s get money. ^o^ \n"%(goal[0],(self.money*turtlecount)))
            print("Money in Wallet : %s"%(self.wallet))
            abc[0]=self.wallet
        else:
            print("%s Turtle Win!! lose moeny ㅜ-ㅜ \n"%(goal[0]))
            self.wallet -= self.money
            print("Money in Wallet : %s\n"%(self.wallet))
            abc[0]=self.wallet
        if self.wallet<0:
            print("have no money in your wallet.")




while True:
    #들어온 거북이추가할 리스트
    turtlelist=["sam","matt","song","thunder"]          #변환 될 거북이 이름
    turtlelist2=["sam","matt","song","thunder"]         #거북이 이름
    turtlecolor=["red","blue","green","black"]    #거북이 색깔
    goal=[]
    resulttime=0
    print(" ")
    print("                  Turtlerace\n")
    print("""======================================================
                    1.Start


                    2.Exit
======================================================""")

    start=int(input("Button : "))
    os.system("cls")
    if start == 1 :
        print("""
If the turtle you choose wins,
 2 turtle = 2 X Battingmoney
 3 turtle = 3 X Battingmoney
 4 turtle = 4 X Battingmoney
        """)
        turtlecount=int(input("how many turtle?(2 ~ 4)")) #처음 거북이 수 결정

        if turtlecount <=1 or turtlecount> 4:
            print("Please input 2 ~ 4")
            time.sleep(1)
            os.system("cls")
            continue # 5
        os.system("cls")
        turtlegame() #class
        print("%s Winner"%goal[0])
        os.system("pause")
        os.system("cls")

        turtlelist=["sam","matt","song","thunder"]
        turtlelist2=["sam","matt","song","thunder"]
        money=0 # 배팅머니 초기화
        start=0 #
        goal=[] # 승리 거북이 리스트 초기화
        continue
    elif start==2: #2번 누르면 프로그램 종료
        exit()
