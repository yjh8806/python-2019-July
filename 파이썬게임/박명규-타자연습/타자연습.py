# 사용할 모듈 3 개
import random as r
import time as t
import os

# 타자 속도 재는 건데 게임? 일까요 이게?
class Speed():

    incorrect = 0 # 문장 몇 개가 틀린건지?
    count = 0 # 종합 시간을 출력해줄 때 사용할 count
    count2 = 0 # 평균 타자 속도를 출력해줄 때 사용할 count2
    Question = [] # 문장들을 넣을 리스트
    all_time_speed_tmp = 0 # 평균 타자 속도를 위해 각 타자 속도를 더해놓을 곳
    all_time_speed = 0 # 평균 타자 속도를 넣어 줄 곳
    num_speed = [] # 걸린 종합 시간을 넣어 줄 리스트
    num_all_speed = [] # 종합 타자 평균을 넣어 줄 리스트

    # 연습할 문장들을 리스트에 분리해서 만들어 놓기
    Star = []
    Star.append("별 하나에 추억과 별 하나에 사랑과")
    Star.append("별 하나에 쓸쓸함과 별 하나에 동경과")
    Star.append("별 하나에 시와 별 하나에 어머니, 어머니")
    Star.append("어머님, 나는 별 하나에 아름다운 말 한마디 씩 불러봅니다")

    Lucky = []
    Lucky.append("여름장이란 애시당초에 글러서 해는 아직 중천에 있건만")
    Lucky.append("장판은 벌써 쓸쓸하고 더운 햇발이 벌려 놓은 전시장")
    Lucky.append("밑으로 등줄기를 훅훅 볶는다")

    # Question 에 만들어 놓은 문장들을 넣어준다
    Question.append(Star)
    Question.append(Lucky)

    def pickNote(self): # Question 에 든 것을 랜덤으로 뽑을 것
        Question = []
        return r.choice(self.Question)

    def Print_Input(self, note): # 랜덤으로 뽑은 문장을 보여주고 사용자에게 다시 입력 받음
        print(note) # 랜덤으로 뽑은 것 출력
        a_time = t.time() # 시작 시간
        answer = input("") # 출력된 모양대로 입력할 변수
        b_time = t.time() # 끝 시간
        if answer != note: # 문장이 똑같지 않으면 +1
            self.incorrect += 1
        one_time_speed = len(answer) / (b_time - a_time) * 60 # 입력한 한 문장에 대해서 타자 속도 재는 것
        self.All_time_speed(one_time_speed) # 문장의 타자 속도를 넣어 더해서 저장
        print("타자 속도 : %.2f 타\n"%one_time_speed) # 입력이 끝나면 타자 속도 출력

    def All_time_speed(self, ots): # Print_Input 에서 타자 속도를 받아 다 더해서 보관
        self.all_time_speed_tmp += ots

    # 받은 종합 시간을 저장할 곳
    def Num_speed(self, setime):
        self.num_speed.append(setime) # 리스트에 종합 시간을 저장
        self.num_speed.sort()
        self.count += 1

    # 종합 시간을 순위 매겨서 출력
    def Print_Num_speed(self):
        for i in range(self.count):
            print("%d 위 : %.2f"%(i+1, self.num_speed[i]))

    # 받은 평균 타자 속도들을 저장할 곳
    def Num_all_speed(self, getime):
        self.num_all_speed.append(getime) # 리스트에 평균 타자 속도를 추가
        self.num_all_speed.sort()
        self.num_all_speed.reverse()
        self.count2 += 1

    # 평균 타자 속도들을 순위 매겨서 출력
    def Print_Num_all_speed(self):
        for i in range(self.count2):
            print("%d 위 : %.2f"%(i+1, self.num_all_speed[i]))

    # 평균 타자 속도 저장한 것을 초기화
    def all_time_zero(self):
        self.all_time_speed_tmp = 0

    # 잠깐 멈췄다가 누르면 화면 깔끔하게 비워줌
    def pause_cls(self):
        os.system("pause")
        os.system("cls")

    def start(self): # 시작
        while True: # 게임이 반복될 수 있게 해줌
            Que = self.pickNote() # Que 에 저장된 문장을 랜덤으로 넣어줌
            print("타자 게임?")
            print("===1. 게임시작===\n===2. 시간 순위 출력===\n===3. 평균 타자 순위 출력===")
            print("===4. 종료하고 나가기===")
            select_type = int(input("선택하세요 :"))
            if select_type == 1: # 1을 넣으면 게임 시작
                input("\n===Enter로 시작===\n")
                os.system("cls") # window 명령어로 cls 넣어주기
                S_time = t.time() # 종합 시간 확인용 시작 시간
                for i in range(len(Que)): # Que 에 들어있는 문장 수 만큼 반복
                    self.Print_Input(Que[i]) # Que 리스트 인덱스 Print_Input 에 넣어줌
                all_time_speed = self.all_time_speed_tmp / len(Que) # 보관한 전체 시간을 문장 수 만큼 나눗셈
                E_time = t.time() # 종합 시간 확인용 끝나는 시간
                SE_time = E_time - S_time # 걸린 종합 시간을 완성
                self.Num_speed(SE_time) # 종합 시간을 저장할 수 있게 넣어줌
                self.Num_all_speed(all_time_speed) # 평균 타자 속도를 저장할 수 있게 넣어줌
                self.pause_cls() # 멈췄다가 화면 정리
                print("\n끝났습니다!\n걸린 시간 : %.2f\n틀린 문장 : %d"%(SE_time, self.incorrect))
                print("평균 타자 속도 : %.2f 타"%all_time_speed)
                self.all_time_zero()
                self.pause_cls() # 멈췄다가 화면 정리
            elif select_type == 2: # select_type 이 2 이면 종합 시간 순위 출력
                self.Print_Num_speed()
                self.pause_cls() # 멈췄다가 화면 정리
            elif select_type == 3: # select_type 이 3 이면 평균 타자 속도 순위 출력
                self.Print_Num_all_speed()
                self.pause_cls() # 멈췄다가 화면 정리
            elif select_type == 4: # select_type 이 4 이면 나가기
                break
            else: # 1 ~ 4 가 아닐 경우(space bar 만 넣으면 종료 됨... 왜?)
                print("잘못 입력하셨습니다")
                self.pause_cls() # 멈췄다가 화면 정리

game = Speed().start() # Speed class 구동
