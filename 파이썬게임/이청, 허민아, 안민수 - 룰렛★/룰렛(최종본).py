from time import sleep
from os import *
from random import *

total_gold = 0
logo="""
     ================================
     ★☆★☆★☆★☆★☆★☆★☆★☆
       Welcome to
             ┌──┐  ┌──┐  ┌──┐
                │     │     │
                │     │     │  ♥

     ★☆★☆★☆★☆★☆★☆★☆★★
     ================================
"""

first_menu="""
1. 게임장 입장

2. 계좌 확인

3. 대출하기

4. 종료
"""

gold=500000 # 초기 골드값
loan=0      # 대출금 (사용자가 대출할 때 입력한 값 저장)
total_loan=0    # 총 대출금
loan_p=total_loan*0.2   # 대출이자 ( 20% )
max_loan=1000000000     # 최대 대출 가능한 금액 10억
total_gold=gold+total_loan



while True:
    system("cls")
    print(logo) # welcome to 777
    print(first_menu)   # 1.게임시작 ~ 4.종료
    first_select = int(input(" >>> "))  # 1.게임시작 ~ 4.종료 중에서 선택
    system("cls")
    if first_select == 1:  # 게임시작을 고를 경우
        pass

    elif first_select == 2:  # 계좌확인
        print("""
        ===============================
        ★ Gold    : {:>15,.0f}원
        ★ 대출잔액 : {:>14,.0f}원
        ★ 대출이자 : {:>14,.0f}원
        ===============================
        """.format(total_gold,total_loan,round(total_loan*0.2)))
        system("pause")
        system("cls")
        if total_loan > 0 and gold > total_loan+(total_loan*0.2) :   # 총 대출금이 0원 이상이고 ( 대출이 있고 )
            pay = input("\n 대출금을 갚으시겠습니까?[y/n] : ")           # 현재 소지 골드가 대출금+대출이자보다 많으면
            if pay == 'y':                                           # 대출금을 갚겠냐는 선택지 출력
                # total_gold-=total_loan+loan_p

                total_gold -= total_loan*1.2
                # total_gold -= (total_loan*0.2)
                print(" 대출원금 {:,.0f}원과 대출이자 {:,.0f}원을 갚아 {:,.0f}원이 남았습니다.\n".format(total_loan,round(total_loan*0.2),total_gold))
                total_loan=0
                loan=0
                system("pause")
            elif pay == 'n':
                print(" 대출금을 갚지 않았습니다... \n")
                system("pause")
        continue
    elif first_select == 3:     # 대출
        loan=int(input("\n 얼마를 대출 하시겠습니까? (최대 1,000,000,000원 / 이율 : 20% ) : "))
        if total_loan < 1000000000 and loan <= 1000000000 :  # 총 대출금 10억이하, 1회 대출금 10억 이하일 경우
            print(" {:,d}원을 대출하였습니다. \n".format(loan))
            total_loan += loan
            total_gold += loan
        elif total_loan >= 1000000000 or loan > 1000000000:
            print(" 한도금액을 초과하였습니다.")

        else:   # 총 대출금 10억이하, 1회 대출금 10억 이하 기준치에 부합되지 않을 경우
            print(" 정확히 입력해주세요. \n")

        system("pause")
        system("cls")
        continue
    elif first_select == 4 :    # 종료
        print("\n\n\n\n\n\n\n\n\n\t\t\t\t♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥\n\n\t\t\t\t\t다음번에 또 이용해주세요\n\n\t\t\t\t♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥\n\n\n\n\n\n\n")
        break


    else :      # 1.게임시작 ~ 4.종료 외에 다른 키를 입력했을 경우
        print("정확히 입력해주세요! \n")
        system("pause")
        continue
    system("cls")

    list = ["★","77","♠","♥"]

    print("\n\n\n\n\n\n\t\t\t현재잔액 : %.0f원"%total_gold)
    bet = int(input("\t\t\t배팅할 금액을 입력해주세요 : "))
    if bet > total_gold:
        print("배팅하신 금액이 현재 금액보다 큽니다")
        print("처음 화면으로 돌아갑니다. 다시입력해주세요")
        system("pause")
        continue
    else:
        system("cls")
        print("\n\n\n\n\n\n\n\n\n\n\t\t\t%s원을 배팅하셨습니다. 잠시후 게임이 시작됩니다."%bet)
        total_gold -= bet
    sleep(1)
    system("cls")
    print("\n\n\n\n\n\n\n\n\n\n\n\t\t\t\t\t\t 3")
    sleep(1)
    system("cls")
    print("\n\n\n\n\n\n\n\n\n\n\n\t\t\t\t\t\t 2")
    sleep(1)
    system("cls")
    print("\n\n\n\n\n\n\n\n\n\n\n\t\t\t\t\t\t 1")
    sleep(1)
    system("cls")
    for k in range(20):
        luck = choice(list)
        print("\n\n\n\n\n\n\n\n\n\t\t\t\t★☆★☆★☆★☆★☆★☆★☆★")
        print("\t\t\t\t☆┌────────────────────┐   ☆")
        print("\t\t\t\t★│  %s  │      │      │ ●★"%luck)
        print("\t\t\t\t☆│────────────────────│ | ☆")
        print("\t\t\t\t★│  %s  │      │      │ | ★"%luck)
        print("\t\t\t\t☆│────────────────────│ | ☆")
        print("\t\t\t\t★│  %s  │      │      │┘  ★"%luck)
        print("\t\t\t\t☆└────────────────────┘   ☆")
        print("\t\t\t\t★☆★☆★☆★☆★☆★☆★☆★")
        sleep(0.1)
        system("cls")
    a,b,c,d,e = choice(list),choice(list),choice(list),choice(list),choice(list)
    f,g,h,i = choice(list),choice(list),choice(list),choice(list)
    print("\n\n\n\n\n\n\n\n\n\t\t\t\t★☆★☆★☆★☆★☆★☆★☆★")
    print("\t\t\t\t☆┌────────────────────┐   ☆")
    print("\t\t\t\t★│  %s  │      │      │ ●★"%a)
    print("\t\t\t\t☆│────────────────────│ | ☆")
    print("\t\t\t\t★│  %s  │      │      │ | ★"%d)
    print("\t\t\t\t☆│────────────────────│ | ☆")
    print("\t\t\t\t★│  %s  │      │      │┘  ★"%g)
    print("\t\t\t\t☆└────────────────────┘   ☆")
    print("\t\t\t\t★☆★☆★☆★☆★☆★☆★☆★")
    print("\n\n\t\t\t 자~ 첫번째 룰렛의 결과가 나왔습니다~!! \n\n\n\n")
    system("pause")
    system("cls")
    for k in range(20):
        luck = choice(list)
        print("\n\n\n\n\n\n\n\n\n\t\t\t\t★☆★☆★☆★☆★☆★☆★☆★")
        print("\t\t\t\t☆┌────────────────────┐   ☆")
        print("\t\t\t\t★│  %s  │  %s  │      │   ★"%(a,luck))
        print("\t\t\t\t☆│────────────────────│   ☆")
        print("\t\t\t\t★│  %s  │  %s  │      │ ●★"%(d,luck))
        print("\t\t\t\t☆│────────────────────│ | ☆")
        print("\t\t\t\t★│  %s  │  %s  │      │┘  ★"%(g,luck))
        print("\t\t\t\t☆└────────────────────┘   ☆")
        print("\t\t\t\t★☆★☆★☆★☆★☆★☆★☆★")
        sleep(0.1)
        system("cls")
    print("\n\n\n\n\n\n\n\n\n\t\t\t\t★☆★☆★☆★☆★☆★☆★☆★")
    print("\t\t\t\t☆┌────────────────────┐   ☆")
    print("\t\t\t\t★│  %s  │  %s  │      │   ★"%(a,b))
    print("\t\t\t\t☆│────────────────────│   ☆")
    print("\t\t\t\t★│  %s  │  %s  │      │ ●★"%(d,e))
    print("\t\t\t\t☆│────────────────────│ | ☆")
    print("\t\t\t\t★│  %s  │  %s  │      │┘  ★"%(g,h))
    print("\t\t\t\t☆└────────────────────┘   ☆")
    print("\t\t\t\t★☆★☆★☆★☆★☆★☆★☆★")
    print("\n\n\t\t\t 자~ 두번째 룰렛의 결과도 나왔습니다~!!!")
    print("\t\t\t\t 마지막까지 화이팅!! \n")
    system("pause")
    system("cls")

    for k in range(20):
        luck = choice(list)
        print("\n\n\n\n\n\n\n\n\n\t\t\t\t★☆★☆★☆★☆★☆★☆★☆★")
        print("\t\t\t\t☆┌────────────────────┐   ☆")
        print("\t\t\t\t★│  %s  │  %s  │  %s  │   ★"%(a,b,luck))
        print("\t\t\t\t☆│────────────────────│   ☆")
        print("\t\t\t\t★│  %s  │  %s  │  %s  │   ★"%(d,e,luck))
        print("\t\t\t\t☆│────────────────────│ ●☆")
        print("\t\t\t\t★│  %s  │  %s  │  %s  │┘  ★"%(g,h,luck))
        print("\t\t\t\t☆└────────────────────┘   ☆")
        print("\t\t\t\t★☆★☆★☆★☆★☆★☆★☆★")
        sleep(0.1)
        system("cls")

    while True:
        system("cls")
        print("\n\n\n\n\n\n\n\n\n\t\t\t\t결과를 보여드리겠습니다.")
        print("\t\t\t\t잠시만 기다려주세요!!")
        my = []
        list2 = [[a,b,c],[d,e,f],[g,h,i]]
        count = 0
        sleep(2)
        system("cls")
        print("\n\n\n\n\n\n\n\n\n\t\t\t\t★☆★☆★☆★☆★☆★☆★☆★")
        print("\t\t\t\t☆┌────────────────────┐   ☆")
        print("\t\t\t\t★│  %s  │  %s  │  %s  │   ★"%(a,b,c))
        print("\t\t\t\t☆│────────────────────│   ☆")
        print("\t\t\t\t★│  %s  │  %s  │  %s  │   ★"%(d,e,f))
        print("\t\t\t\t☆│────────────────────│ ●☆")
        print("\t\t\t\t★│  %s  │  %s  │  %s  │┘  ★"%(g,h,i))
        print("\t\t\t\t☆└────────────────────┘   ☆")
        print("\t\t\t\t★☆★☆★☆★☆★☆★☆★☆★")
        for k in range(3):     #행의 일치
            for j in list2[k]:
                my.append(j)
            for k in list:
                if my.count(k) == 3:
                    count += 2
            my = []
        for k in range(1):   #열의 일치
            for j in range(3):
                if list2[k][j] == list2[k+1][j] == list2[k+2][j]:
                    count += 2
        if (list2[0][0] == list2[1][1] == list2[2][2]):   #대각선 두줄
            count += 4
        if (list2[0][2] == list2[1][1] == list2[2][0]):
            count += 4
        print("\n\n\n현재 배율은 %s배 입니다."%count)
        print("원하시는 행과 열의 문자들을 바꿀 기회를 드리겠습니다(배팅금액의 20%)")
        print("그만하시려면 1번을, 행을 바꾸시려면 2번을, 열을 바꾸시려면 3번을 눌러주세요")
        reply = int(input(": "))
        system("cls")
        if reply == 1:
            break
        elif reply == 2 and total_gold >= bet*0.2:
            total_gold -= bet*0.2
            print("\n\n\n\n\n\n\n\n\n\t\t\t\t잔액에서 %.0f원 차감됩니다."%(bet*0.2))
            print("\t\t\t\t현재금액 : %.0f"%total_gold)
            print("\t\t\t\t┌────────────────────┐")
            print("\t\t\t\t│         1          │")
            print("\t\t\t\t│────────────────────│")
            print("\t\t\t\t│         2          │")
            print("\t\t\t\t│────────────────────│")
            print("\t\t\t\t│         3          │")
            print("\t\t\t\t└────────────────────┘")
            print("\t\t\t\t4: 돌아가기")
            reply2 = int(input("\t\t\t\t어느것을 바꾸시길 원하십니까? (1~4) :  "))
            if reply2 == 1:
                a,b,c = choice(list), choice(list), choice(list)
            elif reply2 == 2:
                d,e,f = choice(list), choice(list), choice(list)
            elif reply2 == 3:
                g,h,i = choice(list), choice(list), choice(list)
            elif reply2 == 4:
                total_gold += bet*0.2
                print("\t\t\t\t%.0f원을 반환해 드리겠습니다"%(bet*0.2))
                system("pause")
                continue
            else:
                print("1~4까지 숫자를 입력해주세요!!")
                reply2 = int(input("어느것을 바꾸시길 원하십니까? (1~4) :  "))
            continue

        elif reply == 2 and total_gold < bet*0.2:
            print("잔액이 부족합니다.")
            system("pause")
            continue
        elif reply == 3 and total_gold >= bet*0.2:
            total_gold -= bet*0.2
            print("\n\n\n\n\n\n\n\n\n\t\t\t\t잔액에서 %.0f원 차감됩니다."%(bet*0.2))
            print("\t\t\t\t현재금액 : %.0f"%total_gold)
            print("\t\t\t\t┌────────────────────┐")
            print("\t\t\t\t│      │      │      │")
            print("\t\t\t\t│      │      │      │")
            print("\t\t\t\t│  1   │  2   │   3  │")
            print("\t\t\t\t│      │      │      │")
            print("\t\t\t\t│      │      │      │")
            print("\t\t\t\t└────────────────────┘")
            print("\t\t\t\t4: 돌아가기")
            reply2 = int(input("\t\t\t\t어느것을 바꾸시길 원하십니까? (1~3) :  "))
            if reply2 == 1:
                a,d,g = choice(list),choice(list),choice(list)
            elif reply2 == 2:
                b,e,h = choice(list),choice(list),choice(list)
            elif reply2 == 3:
                c,f,i = choice(list),choice(list),choice(list)
            elif reply2 == 4:
                total_gold += bet*0.2
                print("\t\t\t\t%.0f원을 반환해 드리겠습니다"%(bet*0.2))
                system("pause")
                continue
            else:
                print("1~4까지 숫자를 입력해주세요!!")
                reply2 = int(input("어느것을 바꾸시길 원하십니까? (1~3) :  "))
            continue

        elif reply == 3 and total_gold < bet*0.2:
            print("잔액이 부족합니다.")
            system("pause")
            continue
        else:
            print("다시 입력해주세요")
            reply = int(input(" : "))


    print("\n\n\n\n\n\n\n\n\n\t\t\t\t최종 배율은 %s배이고, %.0f원을 획득하셨습니다."%(count,bet*count))
    print("\t\t\t\t\t★☆★☆★축하합니다★☆★☆★")
    total_gold += (bet*count)
    system("pause")
    system("cls")
    continue


    #list3 = [["a","b","c"],["d","e","f"],["g","h","i"]]
    # print("┌────────────────────┐")
    # print("│  a   │  b   │  c   │")
    # print("│────────────────────│")
    # print("│  d   │  e   │  f   │")
    # print("│────────────────────│")
    # print("│  g   │  h   │  i   │")
    # print("└────────────────────┘")
    # print(list2)
    # reply2 = input("어느것을 바꾸시길 원하십니까? (a~i) :  ")
    # if reply2 in list3[0] or reply2 in list3[1] or reply2 in list3[2]:
    #     for k in range(3):
    #         for j in range(3):
    #             if reply2 == list3[k][j]:
    #                 list2[k][j] = choice(list)
    # print(list2)
