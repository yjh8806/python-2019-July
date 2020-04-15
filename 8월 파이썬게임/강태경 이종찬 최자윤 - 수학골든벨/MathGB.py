import os
import random as r
import time as t

class Mathgb:
    def __init__(self):
        pass

    def calc(self):     #나머지 메소드를 모두 사용하는 메소드
        num = 0     #만약 정답이라면 num에 1이 더해짐 => 진행횟수가 올라감
        while num < 3:
            self.a = r.randint(2, 99)
            self.b = r.randint(2, 99)
            c = r.randint(1, 4)     # c는 랜덤변수로 사칙연산 하나를 지정함
            if c == 1:
                num += self.sum()
            elif c == 2:
                num += self.sub()
            elif c == 3:
                num += self.div()
            else:
                num += self.mul()
            print("현재 진행상황 : ({} / 3)".format(num))

    def sum(self):
        num = 1
        result = int(input("{} + {} = ".format(self.a, self.b)))
        if result == self.a + self.b:
            print("정답입니다.")
        else:
            print("오답입니다.")
            num -= 1
        return num

    def sub(self):
        num = 1
        if self.a < self.b:
            result = int(input("{} - {} = ".format(self.b, self.a)))
        else: # 정답이 양의 정수가 되기 위한 조건식
            result = int(input("{} - {} = ".format(self.a, self.b)))

        if result == abs(self.a - self.b):
            print("정답입니다.")
        else:
            print("오답입니다.")
            num -= 1
        return num

    def div(self):
        while True:
            num = 1
            self.a = r.randint(2, 99)
            self.b = r.randint(3, 10)
            if self.a % self.b == 0 and self.a != self.b :  # 정수로 떨어지는 정답을 위해 조건을 지정
                result = int(input("{} / {} = ".format(self.a, self.b)))
                if result == self.a / self.b:
                    print("정답입니다.")
                else:
                    print("오답입니다.")
                    num -= 1
                break
        return num

    def mul(self): # 난이도 조정을 위해 b의 숫자를 줄임
        num = 1
        self.a = r.randint(2, 99)
        self.b = r.randint(2, 10)
        result = int(input("{} x {} = ".format(self.a, self.b)))
        if result == self.a * self.b:
            print("정답입니다.")
        else:
            print("오답입니다.")
            num -= 1
        return num

def ranker(result): #최단시간 기록이면 메시지 띄움
    print("소요시간은 %.2f초 입니다"%result)
    if best_score[0] == result :
        print("☆☆최고기록갱신☆☆")
    else:
        pass

def filemaker():
    if best_score[0] == 10 ** 5:
        print("게임을 하고 돌아오세요!")
    elif best_score[1] == 10 ** 5:
        print("1. %s : %.2f"%(name[game_score.index(best_score[0])], best_score[0]))
    elif best_score[2] == 10 ** 5:
        for i in range(2):
            print("%d. %s : %.2f"%(i+1, name[game_score.index(best_score[i])], best_score[i]))
    else:
        for i in range(3):
#  best_score[0]은 최고기록 // game_score.index(best_score[0])은 최고기록의 game_score 인덱스번호 // 인덱스번호에 맞는 name(사용자 닉네임)
            print("%d. %s : %.2f"%(i+1, name[game_score.index(best_score[i])], best_score[i]))

p = Mathgb()
min_time = 0
name = [] # 사용자의 닉네임 저장
game_score = [] # 사용자의 기록 저장
best_score = [10 ** 5] # 사용자의 최고기록을 정리하는 리스트. (10 ** 5 는 인덱스 번호를 일정하게 유지하기 위해 사용)
f = open("Rank.txt", "r")
while True:
    line = f.readline()
    if line:
        name.append(line.split()[1])
        game_score.append(float(line.split()[3]))
        best_score.append(float(line.split()[3]))
    else:
        break
f.close()
while True: #초기화면
    print("====수☆학☆골☆든☆벨====")
    print("""개요: 이 게임의 취지는 수학연산 능력 평가입니다.
    1. 게임시작
    2. 최고점수
    3. 개발자
    4. 게임 종료""")
    select = int(input(">>> "))

    if select == 1: #게임 시작
        while True:
            nickname = input("닉네임을 적으세요 : ")
            print("1!")
            t.sleep(1)
            print("2!")
            t.sleep(1)
            print("3!")
            t.sleep(1)
            print("시작!")
            start = t.time()
            p.calc() # calc() 메소드가 끝나는 시간을 측정 => 기록으로 활용됨
            end = t.time()
            result = end - start

            ranker(result)
            name.append(nickname) # 사용자의 닉네임 추가
            game_score.append(result) # 사용자의 기록을 추가  ////  name과 game_score의 인덱스번호의 일치로 3개의 점수를 표시하기 위함
            best_score.append(result) # 정렬하여 최고기록부터 3개의 기록을 골라내기 위해
            best_score.sort()

            re = int(input("다시 하시겠습니까? (다시한다 : 1, 그만한다 : 0)"))
            if re == 0:
                break
            else:
                os.system("pause")
                os.system("cls")
            os.system("pause")
            os.system("cls")

    elif select == 2: #최고 점수
        filemaker()
        f = open("Rank.txt", "w")
        if best_score[0] == 10 ** 5:
            f.write("게임을 하고 돌아오세요!")
        elif best_score[1] == 10 ** 5:
            f.write("1 %s : %.2f\n"%(name[game_score.index(best_score[0])], best_score[0]))
        elif best_score[2] == 10 ** 5:
            for i in range(2):
                f.write("%d %s : %.2f\n"%(i+1, name[game_score.index(best_score[i])], best_score[i]))
        else:
            best_score.remove(10 ** 5)
            for i in range(len(best_score)):
            #  best_score[0]은 최고기록 // game_score.index(best_score[0])은 최고기록의 game_score 인덱스번호 // 인덱스번호에 맞는 name(사용자 닉네임)
                f.write("%d %s : %.2f\n"%(i+1, name[game_score.index(best_score[i])], best_score[i]))
        f.close()
        os.system("pause")
        os.system("cls")

    elif select == 3: #개발자
        print("조명 : 최강종찬")
        print("조원 : 강태경 이종찬 최자윤")
        os.system("pause")
        os.system("cls")

    elif select == 4:
        print("프로그램을 종료합니다.")
        exit(0)
        break
    else:
        print("잘못된 입력입니다.")
