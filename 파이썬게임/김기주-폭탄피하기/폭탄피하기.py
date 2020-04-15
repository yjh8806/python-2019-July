import random as r
import time as t
import os #system함수를 사용하기 위한 객체

bomb_list1 = ["휴, 살았다!","폭탄 당첨!"] #게임 진행에 사용될 리스트
bomb_list2 = ["휴, 살았다!","폭탄 당첨!","살았어!"]
bomb_list3 = ["휴, 살았다!","폭탄 당첨!","살았어!","나만 아니면 돼!"]

class Bomb:
    def game_start(self):
        while True: #조건식이 거짓말이 안되는 반복문 => 무한반복문
            print("""
            =====폭탄 피하기 게임=====
            <1.게임 시작 2.게임 종료>
            """)
            select = int(input(">> "))
            if select == 1:
                pick = int(input("인원입력(2 ~ 4인) : "))
                if pick == 2:
                    select = r.choice(bomb_list1) #bomb_list1 중 랜덤하게 선택
                    print("\n3!")
                    t.sleep(1) #시간을 지연 시켜줍니다.
                    print("2!")
                    t.sleep(1)
                    print("1!")
                    t.sleep(1)
                    print("\n%s"%select) #결과물을 출력
                    t.sleep(1)
                    bomb_list1.remove(select) #나왔던 결과는 지워줍니다.
                elif pick == 3:
                    select = r.choice(bomb_list2)
                    print("\n3!")
                    t.sleep(1)
                    print("2!")
                    t.sleep(1)
                    print("1!")
                    t.sleep(1)
                    print("\n%s"%select)
                    t.sleep(1)
                    bomb_list2.remove(select)
                elif pick == 4:
                    select = r.choice(bomb_list3)
                    print("\n3!")
                    t.sleep(1)
                    print("2!")
                    t.sleep(1)
                    print("1!")
                    t.sleep(1)
                    print("\n%s"%select)
                    t.sleep(1)
                    bomb_list3.remove(select)
                else: #지정해둔 숫자외에 다른것을 입력했을 경우
                    print("잘못된 입력입니다.")
            elif select == 2:
                break #중지
            else:
                print("잘못된 입력입니다.")

            os.system("pause") #코드 일시정지
            os.system("cls") #콘솔창을 지워줍니다.

a = Bomb() #객체 생성
a.game_start()
