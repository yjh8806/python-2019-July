import random as r
import time as t
import os
list = ["★", "1 " , "2 " , "3 " ]
acc = int(input("돈을 뽑으세요 : "))
while True :
    print('''★★★JACKPOT★★★
    ┌────────────────────┐ |
    │  ★  │  ★  │  ★  │┘
    └────────────────────┘ ''')
    money = int(input("베팅할 돈을 넣으세요 : "))
    start = input("<Enter> 를 누르면 게임시작")
    os.system("cls")
    for i in range(50) :
        rand1 = r.choice(list)
        print("★☆★☆★☆JACKPOT★☆★☆★")
        print("☆┌────────────────────┐ | ☆")
        print("★│  %s  │      │      │┘  ★"%(rand1))
        print("☆└────────────────────┘   ☆")
        print("★☆★☆★☆★☆★☆★☆★☆")
        os.system("cls")
    first = r.choice(list)
    print("★☆★☆★☆JACKPOT★☆★☆★")
    print("☆┌────────────────────┐ | ☆")
    print("★│  %s  │      │      │┘  ★"%(first))
    print("☆└────────────────────┘   ☆")
    print("★☆★☆★☆★☆★☆★☆★☆")
    t.sleep(1)
    os.system("cls")
    for i in range(50) :
        rand2 = r.choice(list)
        print("★☆★☆★☆JACKPOT★☆★☆★")
        print("☆┌────────────────────┐ | ☆")
        print("★│  %s  │  %s  │      │┘  ★"%(first,rand2))
        print("☆└────────────────────┘   ☆")
        print("★☆★☆★☆★☆★☆★☆★☆")
        os.system("cls")
    second = r.choice(list)
    print("☆★☆★☆★JACKPOT☆★☆★☆")
    print("★┌────────────────────┐ | ★")
    print("☆│  %s  │  %s  │      │┘  ☆"%(first,second))
    print("★└────────────────────┘   ★")
    print("☆★☆★☆★☆★☆★☆★☆★")
    t.sleep(1)
    os.system("cls")
    for i in range(50) :
        rand3 = r.choice(list)
        print("★☆★☆★☆JACKPOT★☆★☆★")
        print("☆┌────────────────────┐ | ☆")
        print("★│  %s  │  %s  │  %s  │┘  ★"%(first,second,rand3))
        print("☆└────────────────────┘   ☆")
        print("★☆★☆★☆★☆★☆★☆★☆")
        os.system("cls")
    third = r.choice(list)
    print("★☆★☆★☆JACKPOT★☆★☆★")
    print("☆┌────────────────────┐ | ☆")
    print("★│  %s  │  %s  │  %s  │┘  ★"%(first,second,third))
    print("☆└────────────────────┘   ☆")
    print("★☆★☆★☆★☆★☆★☆★☆")

    if first == second == third != "★":
        acc = money * 2 + acc
        print("축하합니다!! 원금 2배!")
        print("잔액",acc)
    elif first == second == third == "★" :
        acc = money * 5 + acc
        print("★☆★☆★☆★☆★☆★☆★☆★☆")
        print("축하합니다!! JACKPOT!!!!")
        print("★☆★☆★☆★☆★☆★☆★☆★☆")
        print("잔액",acc)
    else :
        acc -= money
        print("아쉽네요 다시 도전하세요 ")
        print("잔액",acc)
    os.system("pause")
    os.system("cls")
