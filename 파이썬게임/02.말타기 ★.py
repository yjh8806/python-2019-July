import random as r
import time as t
import os
acc = int(input("계정에 저금할 돈 액수 입력 : "))
print("===말타기 게임===")
print("1등 : 3배 " )
end = input("<Enter>를 누르면 시작 , 0을 누르면 종료 : ")
while end != 0 :
    a = 0
    b = 0
    c = 0
    d = 0
    e = 0
    money = int(input("돈을 거세요 : "))
    horses = [1 , 2 , 3 , 4 , 5]
    horsenum = input("말을 선택하세요 (1~5) : ")
    while a < 15 or b < 15 or c < 15 or d < 15 or e < 15:
        os.system("cls")
        taken = r.choice(horses)
        if taken == 1 :
            a += 2
            print("1번말",end = ' ')
            print(" "*a ,end = ' ')
            print(">")
            print("2번말",end = ' ')
            print(" "*b ,end = ' ')
            print(">")
            print("3번말",end = ' ')
            print(" "*c ,end = ' ')
            print(">")
            print("4번말",end = ' ')
            print(" "*d ,end = ' ')
            print(">")
            print("5번말",end = ' ')
            print(" "*e ,end = ' ')
            print(">")
        elif taken == 2 :
            b += 2
            print("1번말",end = ' ')
            print(" "*a ,end = ' ')
            print(">")
            print("2번말",end = ' ')
            print(" "*b ,end = ' ')
            print(">")
            print("3번말",end = ' ')
            print(" "*c ,end = ' ')
            print(">")
            print("4번말",end = ' ')
            print(" "*d ,end = ' ')
            print(">")
            print("5번말",end = ' ')
            print(" "*e ,end = ' ')
            print(">")
        elif taken == 3 :
            c += 2
            print("1번말",end = ' ')
            print(" "*a ,end = ' ')
            print(">")
            print("2번말",end = ' ')
            print(" "*b ,end = ' ')
            print(">")
            print("3번말",end = ' ')
            print(" "*c ,end = ' ')
            print(">")
            print("4번말",end = ' ')
            print(" "*d ,end = ' ')
            print(">")
            print("5번말",end = ' ')
            print(" "*e ,end = ' ')
            print(">")
        elif taken == 4 :
            d += 2
            print("1번말",end = ' ')
            print(" "*a ,end = ' ')
            print(">")
            print("2번말",end = ' ')
            print(" "*b ,end = ' ')
            print(">")
            print("3번말",end = ' ')
            print(" "*c ,end = ' ')
            print(">")
            print("4번말",end = ' ')
            print(" "*d ,end = ' ')
            print(">")
            print("5번말",end = ' ')
            print(" "*e ,end = ' ' )
            print(">")
        elif taken == 5 :
            e += 2
            print("1번말",end = ' ')
            print(" "*a ,end = ' ')
            print(">")
            print("2번말",end = ' ')
            print(" "*b ,end = ' ')
            print(">")
            print("3번말",end = ' ')
            print(" "*c ,end = ' ')
            print(">")
            print("4번말",end = ' ')
            print(" "*d ,end = ' ')
            print(">")
            print("5번말",end = ' ')
            print(" "*e ,end = ' ' )
            print(">")
        t.sleep(0.1)
    if a > b and a > c and a > d and a > e:
        first = 1
    elif b > a and b > c and b > d and b > e:
        first = 2
    elif c > a and c > b and c > d and c > e:
        first = 3
    elif d > a and d > b and d > c and d > e:
        first = 4
    elif e > a and e > b and e > c and e > d:
        first = 5
    if horsenum == first :
        print("☆☆☆☆☆1등☆☆☆☆☆")
        money *= 3
        acc += money
        print("현재 소지 금액 : ",acc)
    else :
        acc = acc - money
        print("%s번말이 이겼습니다."%(first))
        print("돈을 날렸습니다.")
        print("잔액은 %s입니다."%acc)


    os.system("pause")
    os.system("cls")
