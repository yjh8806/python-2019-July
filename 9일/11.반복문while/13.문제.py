import random
Round = 1
LotteSum, SamsungSum = 0, 0 #점수 합계
while Round <= 12: #12회까지 반복하겠네
    Lotte, Samsung = random.randint(0,1), random.randint(0,1) #한 회당 0 ~ 1점 사이의 득점
    print("%d Round) L : %d, S : %d"%(Round, Lotte, Samsung))
    LotteSum += Lotte
    SamsungSum += Samsung
    if Round >= 9 and LotteSum != SamsungSum: #9회 이상이고 롯데와 삼성의 점수가 다를때 나갑니다.
        break
    Round += 1
if LotteSum > SamsungSum:
    print("[%d : %d]롯데가 승리"%(LotteSum, SamsungSum))
elif LotteSum < SamsungSum:
    print("[%d : %d]삼성이 승리"%(LotteSum, SamsungSum))
else:
    print("[%d : %d]비겼습니다."%(LotteSum, SamsungSum))
