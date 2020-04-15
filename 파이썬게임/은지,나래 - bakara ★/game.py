'''
합 첫자리수 9에가까우면 이김 banker vs player
2~10, a, k, q, j (13)x4 = 52
52 x 12deck = 624 장
```

```3rd card rule
player - 0~5 must draw/ 6,7 must stand/ 8,9 natural (both hands stand)
banker - 0~2 must draw/ 3~6 depends on player's 3rd card/ 7 must stand/ 8,9 natural(both hands stand) 95% / 6으로이기면 50%



2. 뱅커

   a)카드 두장의 합이 1또는 2면 플레이어 가 8,9가 나오지 않는한 무조건 한장을 더 받습니다
 b)카드 두장의 합이 3이면 플레이어가 받는 3번째 장이 8이면 뱅커는 추가로 받지 않습니다. 현재까지 받은 숫자로 상황 종료

c)카드 두장의 합이 4면 플레이어가 1-5까지 인 경우, 플레이어가 한장을 더 받게 되며, 플레이어가 6 이상인 경우 뱅커가 한장을 더 받게 됩니다. 플레이어 세번째 장이 1또는 8,9,10(J,Q,K 포함)이면 뱅커는 추가로 카드를 받지 않습니다
 d)카드 두장의 합이 5면 플레이어가 1-5인 경우, 플레이어가 한장을 더 받게되며 플레이어가 6 이상인 경우 뱅커가 한장을 더 받게 됩니다. 플레이어가 4번째 장이 1,2,3 또는 8,9,10(JQK포함) 인 경우 이대로 상황 종료


'''

def change(x): #카드가 kqja일떄 숫자로 변환
    if (x == "K") or (x == "Q") or (x == "J") :
        print("%s의 점수가 10으로 계산됩니다." %x)
        x = 10
    if x == "A":
        print("A의 점수가 1로 계산됩니다.")
        x = 1
    return x





one_deck = [ 2,3,4,5,6,7,8,9,10,'A', 'K', 'Q', 'J'] * 4  # 52장
card_decks = one_deck * 12  # 624장


import random as r
import time as t
import os
# 룰 설명

p1 = r.choice(card_decks)
b1 = r.choice(card_decks)
p2 = r.choice(card_decks)
b2 = r.choice(card_decks)

start = input("시작 [y/n]")

if start == "y" :
    team = input("베팅 : [p]layer / [b]anker / [t]ie : ")
    bet = int(input("베팅할 금액을 입력하시오 : ")) #거는 돈
    t.sleep(1)
    print("player의 첫번째 카드는", p1, "입니다.")
    t.sleep(0.5)
    print("banker의 첫번쨰 카드는", b1, "입니다.")
    t.sleep(0.5)
    print("player의 두번째 카드는", p2, "입니다.")
    t.sleep(0.5)
    print("banker의 두번째 카드는", b2, "입니다.")
    t.sleep(1)


    ls = [p1,p2,b1,b2]
    ls_num = []

    for i in range(4):
        if (ls[i] == "K") or (ls[i] == "Q") or (ls[i] == "J") :
            ls[i] = 10
        if ls[i] == "A":
            ls[i] = 1
        ls_num.append(ls[i])


    p_sum = (ls_num[0] + ls_num[1]) % 10
    b_sum = (ls_num[2] + ls_num[3]) % 10

    print("player의 점수 :", p_sum )
    print("banker의 점수 :", b_sum )
    t.sleep(1)

    p3 = 0
    b3 = 0

# 3
    print("3번째 카드를 뽑습니다 <Enter>")

    if (p_sum > 7) or (b_sum > 7):
        if p_sum == b_sum:
            print("비겼습니다. [tie]")
        elif p_sum > b_sum:
            print("player 가 이겼습니다.")
        else:
            print("banker 가 이겼습니다.")

    elif p_sum == 7:
        if b_sum < 7:
            b3 = r.choice(card_decks)
        if b_sum == 7:
            print("비겼습니다. [tie]")

# player 가 6 일떄
    elif p_sum == 6:
        if b_sum == 6:
            print("비겼습니다. [tie]")
        if b_sum == 7:
            print("banker가 이겼습니다.")
        else: # banker가 0~5 일때 하나 더뽑음
            b3 = r.choice(card_decks)
            b3 = change(b3)
# player가 0~5일떄 무조건 p3뽑음
    elif p_sum < 6:
        p3 = r.choice(card_decks)
        p3 = change(p3)
        if b_sum == 7:
            pass
        elif (b_sum == 6) and p3 == (6 or 7):
            b3 = r.choice(card_decks)
            b3 = change(b3)
        elif b_sum == (4 or 5) and p3 > 5:
            b3 = r.choice(card_decks)
            b3 = change(b3)
        elif b_sum == 3:
            if p3 != 8:
                b3 = r.choice(card_decks)
                b3 = change(b3)
        else:
            if p3 < 8:
                b3 = r.choice(card_decks)
                b3 = change(b3)
            pass

    os.system("pause")
    print("p3",p3)
    print("b3",b3)
    t.sleep(1)
    p_sum += p3
    b_sum += b3
    p_sum %= 10
    b_sum %= 10

    print("player의 점수 :", p_sum )
    print("banker의 점수 :", b_sum )
    t.sleep(1)
    if p_sum == b_sum:
        print("비겼습니다. [tie]")
    elif p_sum > b_sum:
        print("player 가 이겼습니다.")
    else:
        print("banker가 이겼습니다.")






#
# else:
#     exit(0)
