import random as r
import os
minscore = 0 #최고점수
while True:
    print("☆☆☆☆☆UPDOWN게임☆☆☆☆☆")
    print("1.게임시작\n2.게임전적\n3.게임종료")
    select = int(input(">>> "))
    if select == 1:
        computer = r.randint(1, 100)
        count = 0 #시도한 횟수
        os.system("cls")
        while True:
            print(computer) #정답확인용
            player = int(input("정수 입력 : "))
            count += 1
            os.system("cls")
            if player > computer:
                print("=====DOWN=====")
            elif player < computer:
                print("=====U  P=====")
            else: #같을 경우
                print("%d회 만에 맞췄습니다."%count)
                if minscore == 0 or count < minscore:
                    print("☆☆최고기록갱신☆☆")
                    minscore = count
                os.system("pause")
                os.system("cls")
                break
    elif select == 2:
        if minscore == 0:
            print("===게임을 하고 와주세요===")
        else:
            print("최고점수는 %d점입니다."%minscore)
        os.system("pause")
        os.system("cls")
    elif select == 3:
        print("게임종료")
        exit(0)
    else:
        print("잘못된 입력입니다.")
