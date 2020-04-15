import random
A, B = 100, 100
print("시작) A점수 : %d, B점수 : %d"%(A,B))
#random.randint(A, B) : A에서 B사이 중 랜덤한 숫자 하나 반환
count = 0
round = int(input("주사위를 몇 번 던지시겠습니까? "))
while count < round:
    count += 1
    A_dice = random.randint(1, 6) #1 ~ 6사이의 정수를 반환
    B_dice = random.randint(1, 6)
    if A_dice > B_dice:
        B -= A_dice
    elif A_dice < B_dice:
        A -= B_dice
print("종료)A점수 : %d, B점수 : %d"%(A, B))
