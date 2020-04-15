import random as r
import time as t
import os

class Game():
    incorrect = 0
    count = 0
    score_list = []
    #타자연습에 들어갈 문장
    Flower = []
    Flower.append("여름장이란 애시당초에 글러서, 해는 아직 중천에 있건만")
    Flower.append("장판은 벌써 쓸쓸하고 더운 햇발이 벌여 놓은 전 휘장 밑으로 등줄기 훅훅 볶는다.")
    Flower.append("마을 사람들은 거지반 돌아간 뒤요, 팔리지 못한 나뭇군패가 길거리에 궁싯거리고들")

    Rain = []
    Rain.append("소년은 개울가에서 소녀를 보자 곧 윤초시네 증손녀 딸이라는 걸 알 수 있었다.")
    Rain.append("소녀는 개울에다 손을 잠그고 물장난을 하고 있는 것이다. 서울서는 이런 개울물을 보지 못기나하니한듯이.")
    Rain.append("벌써 며칠 째 소녀는, 학교에서 돌아오는 길에 물장난이었다. 소년은 개울둑에 앉아버렸다.")

    Ball = []

    Ball.append("사람들은 아버지를 난쟁이라고 불렀다. 사람들은 옳게 보았다. 아버지는 난쟁이다.")
    Ball.append("불행하게도 사람들은 아버지를 보는 것 하나만 옳았다. 그 밖의 것들은 하나도 옳지 않았다.")
    Ball.append("나는 아버지, 어머니, 영호, 영희, 그리고 나를 포함한 다섯 식구의 모든 것을 걸고 그들이")


    def pause_cls(self):
        os.system("pause")
        os.system("cls")

player = Game()
while True:
    print("타자게임")
    print("""
    ================
    1. 게임 시작
    2. 평균 타자 순위 출력
    """)
    select1 = int(input("선택하시오. "))
    if select1 == 1:
        os.system("cls")
        input("\n=== Enter로 시작 ===")
        os.system("cls")
        print("""
        === 쳐보고 싶은 단어 선택하세요. ===
        1. 메밀꽃 필 무렵
        2. 소나기
        3. 난쟁이가 쏘아 올린 작은 공
        """)

        select2 = int(input("선택하시오. "))
        if select2 == 1:
            os.system("cls")
            print()
            print(player.Flower[0])
            start = t.time()
            answer = input("")
            print(player.Flower[1])
            answer = input("")
            print(player.Flower[2])
            answer = input("")
            end = t.time()
            print("걸린 시간은 %.2f초입니다."%(end - start))


        elif select2 == 2:
            os.system("cls")
            print(player.Rain[0])
            answer = input("")
            start = t.time()
            print(player.Rain[1])
            answer = input("")
            print(player.Rain[2])
            answer = input("")
            end = t.time()
            print("걸린 시간은 %.2f초입니다."%(end - start))

        elif select2 == 3:
            os.system("cls")
            print(player.Ball[0])
            answer = input("")
            start = t.time()
            print(player.Ball[1])
            answer = input("")
            print(player.Ball[2])
            answer = input("")
            end = t.time()
            print("걸린 시간은 %.2f초입니다."%(end - start))
        else:
            print("잘 못 입력하셨습니다.")
        player.score_list.append(end-start)
    if select1 == 2:
        player.score_list.sort()
        count = 1
        for i in player.score_list:
            print("%d등 : %.2f"%(count,i))
            count += 1
