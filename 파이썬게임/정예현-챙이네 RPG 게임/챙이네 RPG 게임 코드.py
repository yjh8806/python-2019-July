import os
import time
import random

# 3번째 게임을 위한 클래스

class horse():
    def __init__(self):
        self.locate = 0 # 시작점 & 두 번째 판부터 할 경우 위치 초기화(할수록 덮어쒸워진다.)
        self.go = 0
    def Show(self):
        if self.locate == 0:
            print(" ● ㅣ ○ ○ ○ ○ ○ ○ ○ ○ ㅣ ○") # 막대기 : 한글 ㅣ
        elif self.locate > 8:
            print(" ○ ㅣ ○ ○ ○ ○ ○ ○ ○ ○ ㅣ ●", end = "")
            print(" <탈락>")
        else:
            print(" ○ ㅣ", end = "")
            print(" ○" * (self.locate - 1), end = "")
            print(" ●", end = "")
            print(" ○" * (8 - self.locate), end = "")
            print(" ㅣ ○")
    def my_separate(self, my_select): # 내 변수도 클래스에 넣기 위해 따로 만든 함수. 이게 없으면 내 말은 고려대상이 안 된다.
        if my_select == "1":
            self.go = 1
        elif my_select == "2":
            self.go = 2
        elif my_select == "3":
            self.go = 3
        print(self.go, end = "  ")
    def horse_pro_number(self, pro_number):
        global move_total_1_count
        global move_total_2_count
        global move_total_3_count
        if pro_number in [1, 2, 3, 4]:
            move_total_1_count += 1
            self.go = 1
        elif pro_number in [5, 6, 7]:
            move_total_2_count += 1
            self.go = 2
        elif pro_number in [8, 9]:
            move_total_3_count += 1
            self.go = 3
        print(self.go, end = "  ")
    def horse_go(self): # 여기서 말을 움직임과 동시에 등수가 정해짐
        if move_total_1_count >= move_total_2_count and move_total_1_count >= move_total_3_count and self.go == 1:
            self.locate += self.go
        elif move_total_2_count > move_total_1_count and move_total_2_count >= move_total_3_count and self.go == 2:
            self.locate += self.go
        elif move_total_3_count > move_total_1_count and move_total_3_count > move_total_2_count and self.go == 3:
            self.locate += self.go
    def rank_up(self):
        global my_rank
        if self.locate > 8:
            my_rank -= 1 # 나의 등수가 8등에서 한 등수 씩 올라감



################################## 1. 게임 설명

def game_explain():
    print("여러분은 여기에 있는 네 가지 게임을 통해 한스(화폐단위)를 벌 수 있으며")
    print("한스를 번 다음 여러 장비들을 강화시켜 공격력을 높여 네 가지 보스를 모두 쓰러뜨리면 승리하는 게임입니다.")
    print("그러나 처음부터 모든 게임을 할 수 있는 것은 아닙니다. 보스를 쓰러뜨릴 때마다 봉인되어 있는 게임이 하나씩 개방됩니다.")
    print("장비 강화도 보스를 쓰러뜨리지 않는 한 일정 레벨 까지만 강화할 수 있습니다.")
    print()
    print("보스를 쓰러뜨리는 방법은 간단합니다. 보스의 공격력보다 여러분의 공격력이 높으면 됩니다.")
    print("단, 보스와 대결을 하기 위해서는 게임에서 요구하는 필요 조건을 만족해야 합니다.")
    print("각 보스마다 공격력이 다르고, 보스마다 단계가 있으며 첫 번째 보스부터 순서대로 쓰러뜨려 나갈 수 있습니다.")
    print("만약 보스보다 공격력이 낮은데 공격을 할 경우 목숨이 하나씩 소멸됩니다.")
    print("그럼 즐거운 게임 되시기 바랍니다!")
    print()

################################## 2. 게임 시작

game2 = 1 # 두 번째 게임이 개방되면 1로 변경
game3 = 1 # 세 번째 게임이 개방되면 1로 변경
game4 = 1 # 네 번째 게임이 개방되면 1로 변경



def game_in():
    while True:
        os.system("cls")
        print(" 어느 게임을 하시겠습니까?")
        print()
        print(" 1. 베팅 묵찌빠 [게임 비용 : 0 한스]")
        if game2 == 0:
            print(" 2. ●●●●●● [잠겨 있습니다. 첫 번째 보스 클리어시 봉인 해제]")
        else:
            print(" 2. 컴퓨터 위치 추적하기 [게임 비용 : 1000 한스]")
        if game3 == 0:
            print(" 3. ●●●●●● [잠겨 있습니다. 두 번째 보스 클리어시 봉인 해제]")
        else:
            print(" 3. 위험한 전진 [게임 비용 : 10000 한스]")
        if game4 == 0:
            print(" 4. ●●●●●● [잠겨 있습니다. 세 번째 보스 클리어시 봉인 해제]")
        else:
            print(" 4. 랜덤 숫자 폭탄 던지기 [게임 비용 : 100000 한스]")
        print("\n 5. 게임 방법을 본다.")
        print(" 6. 메뉴로 돌아간다.")
        print()
        while True:
            select = input()
            if select in ["1", "2", "3", "4"]:
                os.system("cls")
                game_condition_check(select)
                break
            elif select == "5":
                game_method()
                break
            elif select == "6":
                print("메뉴로 돌아갑니다.")
                return
            else:
                print(" 잘못 입력하셨습니다.")



def game_method():
    while True:
        os.system("cls")
        print(" 어느 게임의 방법을 보시겠습니까?")
        print()
        print(" 1. 베팅 묵찌빠")
        if game2 == 0:
            print(" 2. ●●●●●● [잠겨 있습니다. 첫 번째 보스 클리어시 봉인 해제]")
        else:
            print(" 2. 컴퓨터 위치 추적하기")
        if game3 == 0:
            print(" 3. ●●●●●● [잠겨 있습니다. 두 번째 보스 클리어시 봉인 해제]")
        else:
            print(" 3. 위험한 전진")
        if game4 == 0:
            print(" 4. ●●●●●● [잠겨 있습니다. 세 번째 보스 클리어시 봉인 해제]")
        else:
            print(" 4. 랜덤 숫자 폭탄 던지기")
        print("\n 5. 게임 메뉴로 돌아간다.")
        print()
        while True:
            select = input()
            if select == "2" and game2 == 0:
                os.system("cls")
                print("첫 번째 보스를 클리어하지 않아 게임방법을 볼 수 없습니다. 게임방법 메뉴로 돌아갑니다.\n")
                os.system("pause")
                break
            elif select == "3" and game3 == 0:
                os.system("cls")
                print("두 번째 보스를 클리어하지 않아 게임방법을 볼 수 없습니다. 게임방법 메뉴로 돌아갑니다.\n")
                os.system("pause")
                break
            elif select == "4" and game4 == 0:
                os.system("cls")
                print("세 번째 보스를 클리어하지 않아 게임방법을 볼 수 없습니다. 게임방법 메뉴로 돌아갑니다.\n")
                os.system("pause")
                break
            if select == "1":
                os.system("cls")
                game1_method()
                os.system("pause")
                break
            elif select == "2":
                os.system("cls")
                game2_method()
                os.system("pause")
                break
            elif select == "3":
                os.system("cls")
                game3_method()
                os.system("pause")
                break
            elif select == "4":
                os.system("cls")
                game4_method()
                os.system("pause")
                break
            elif select == "5":
                print("게임 메뉴로 돌아갑니다.")
                os.system("pause")
                return
            else:
                print(" 잘못 입력하셨습니다.")



def game1_method():
    print("베팅 묵찌빠는 컴퓨터와 묵찌빠 게임을 하기 전에 자신이 이길 것 같은 횟수를 설정하고 게임을 시작합니다.")
    print("컴퓨터와 세 번 게임을 해서 자신이 설정한 승리 횟수와 맞으면 보너스로 한스를 받습니다.")
    print("자신이 설정한 승리 횟수가 빗나가도 게임에서 승리한 횟수에 따라 별도로 한스를 얻을 수 있습니다.")
    print()



def game2_method():
    print("컴퓨터 위치 추적하기 게임은 자신의 위치와 컴퓨터의 위치가 다섯 번 안에 자신이 설정한 거리의 차 안에 들면")
    print("한스를 벌 수 있는 게임입니다. 한 번 한스를 지불하면 게임할 수 있는 횟수는 3회이며")
    print("각 회마다 거리의 차를 설정할 수 있습니다.")
    print()



def game3_method():
    print("위험한 전진 게임은 자신과 일곱 대의 컴퓨터가 함께 대결을 합니다.")
    print("이 게임은 가능한 한 전진해서는 안 되며 도착점에 다다를 시 탈락하게 되는 게임입니다.")
    print("전진하지 않는 방법은 다음과 같습니다. 자신과 일곱 대의 컴퓨터에는 1, 2, 3의 숫자 중 하나를 선택하게 되는데,")
    print("가장 많이 겹치는 숫자를 든 플레이어는 그 숫자만큼 앞으로 전진하게 됩니다. 즉 자신이 든 숫자가")
    print("컴퓨터들과 많이 안 겹치면 됩니다.")
    print("예를 들어 1을 6명이 들고, 2를 1명이 들고, 3을 1명이 들면, 1을 든 플레이어가 가장 많으므로")
    print("6명은 앞으로 한 칸씩 전진하게 됩니다.")
    print("자신이 들어온 등수에 따라 한스를 얻게 됩니다.")
    print()
    print("※ 참고로 각 컴퓨터가 1, 2, 3을 낼 확률은 각각 4/9, 1/3, 2/9 이며")
    print("※ 가장 많이 겹치는 숫자의 개수가 같으면 적은 숫자를 든 플레이어가 앞으로 그 숫자만큼 전진하게 됩니다.")
    print("※ 또한 컴퓨터와 도착점에 동시에 들어올 시 자신이 도착점에 들어오기 전의 등수가 자신의 등수가 됩니다.")
    print()



def game4_method():
    print("랜덤 숫자 폭탄 던지기 게임은 처음에 입장하면 자신의 말 4개와 컴퓨터의 말 4개가 목숨을 하나씩 가진 채")
    print("정팔각형으로 놓여 있습니다. 총 8개의 말 중에는 임시폭탄 4개가 랜덤으로 놓여지며 게임을 하면서 점수를 얻어")
    print("자신의 말이 가진 임시폭탄을 상대방에게 넘겨야 합니다. 점수를 얻는 방법은 다음과 같습니다.")
    print("총 다섯 라운드를 진행하며 각 라운드에는 세 개의 스테이지가 있는데, 각 스테이지에서 자신과 컴퓨터는")
    print("1이상 10 이하의 숫자 중 하나를 랜덤으로 받습니다. 이때, 자신은 자신의 숫자는 보이지 않고 컴퓨터의 숫자만 보입니다.")
    print("(컴퓨터 또한 자신(컴퓨터)의 숫자가 무엇인지 알 수 없습니다.) 이 상태에서 상대방의 숫자를 보고 대결을 할지 ")
    print("말지를 결정합니다. 대결을 포기한 경우 상대방이 무조건 이기며 대결을 신청한 경우 서로의 숫자를 비교한 뒤 점수가 낮은")
    print("플레이어는 일정량의 점수가 깎이며 높은 숫자를 가진 플레이어가 이깁니다. 이긴 플레이어는 1부터 30까지의 뽑기가 있는")
    print("별도의 맵으로 이동을 합니다. 30개 중에는 10부터 50까지의 점수가 골고루 섞여 있으며 4개의 꽝도 있습니다. 각 스테이지마다")
    print("5번의 기회가 있으며 그 전에 꽝이 걸릴 시 이전에 얻은 점수는 모두 소멸됩니다. 세 개의 스테이지가 끝이 나면")
    print("폭탄 던지기 시스템으로 이동합니다. 여기서 점수가 높은 사람이 찬스권을 가지며 점수를 사용해 임시폭탄의 위치를")
    print("옮길 수 있습니다. 폭탄 던지기 시스템이 끝나면 네 개의 임시폭탄 중 하나가 진짜 폭탄으로 밝혀지며 진짜 폭탄이 있는")
    print("말은 목숨이 없어집니다. 마지막 라운드를 마치고 말의 개수가 많은 플레이어가 이기며 말의 개수의 현황에 따라")
    print("한스가 지급됩니다.")
    print()



def game_condition_check(select):
    if select == "2" and game2 == 0:
        print("첫 번째 보스를 클리어하지 않아 게임을 할 수 없습니다.\n")
        os.system("pause")
        return
    elif select == "3" and game3 == 0:
        print("두 번째 보스를 클리어하지 않아 게임을 할 수 없습니다.\n")
        os.system("pause")
        return
    elif select == "4" and game4 == 0:
        print("세 번째 보스를 클리어하지 않아 게임을 할 수 없습니다.\n")
        os.system("pause")
        return
    else:
        game_pay_and_stand_by(select)



def game_pay_and_stand_by(select):
    global money
    if select == "1":
        print("베팅 묵찌빠 게임을 하시겠습니까? (y/n)")
        while True:
            select_Y_or_N = input()
            if select_Y_or_N == "y" or select_Y_or_N == "Y":
                os.system("cls")
                break
            elif select_Y_or_N == "n" or select_Y_or_N == "N":
                print("게임 메뉴로 돌아갑니다.")
                os.system("pause")
                return
            else:
                print("잘못 입력하셨습니다.")
    elif select in ["2", "3", "4"]:
        if select == "2":
            print("1000", end = "")
        elif select == "3":
            print("10000", end = "")
        elif select == "4":
            print("100000", end = "")
        print(" 한스를 지불하고 게임을 시작하시겠습니까? (y/n)")
        while True:
            select_Y_or_N = input()
            if select_Y_or_N == "y" or select_Y_or_N == "Y":
                os.system("cls")
                if (select == "2" and money < 1000) or (select == "3" and money < 10000) or (select == "4" and money < 100000):
                    print("한스가 부족하여 게임을 할 수 없습니다. 게임 메뉴로 돌아갑니다.")
                    os.system("pause")
                    return
                if select == "2":
                    print("1000", end = "")
                    money -= 1000
                elif select == "3":
                    print("10000", end = "")
                    money -= 10000
                elif select == "4":
                    print("100000", end = "")
                    money -= 100000
                print(" 한스를 지불하고 게임을 시작합니다.")
                break
            elif select_Y_or_N == "n" or select_Y_or_N == "N":
                print("게임 메뉴로 돌아갑니다.")
                os.system("pause")
                return
            else:
                print("잘못 입력하셨습니다.")
    if select == "1":
        print("잠시 후 게임이 시작됩니다.")
    print("3")
    time.sleep(0.85)
    print("2")
    time.sleep(0.85)
    print("1")
    time.sleep(0.85)
    os.system("cls")
    if select == "1":
        game1_in()
    elif select == "2":
        game2_in()
    elif select == "3":
        game3_in()
    elif select == "4":
        game4_in()

################################## 첫 번째 게임

r_c_p = ["가위", "바위", "보"]
R_C_P_count = 0 # 아직 1번 게임을 안 한 상태. 한 경우 1로 바뀐다. 게임이 끝날 경우 다시 0으로 바뀐다.
player_first_win = 0
computer_first_win = 0
player_predict_count = 0
R_C_P_reward = [600, 1200, 2000] # 묵찌빠를 각각 한 판, 두 판, 세 판 이겼을 경우 상금



def game1_in():
    global money
    global player_predict_count
    print("세 판 중 자신이 이길 것 같은 게임 횟수는? : ")
    while True:
        victory_count = input()
        if victory_count not in ["0", "1", "2", "3"]:
            print(" 잘못 입력하셨습니다.")
            continue
        break
    os.system("cls")
    print("\n\t자신이 이길 것 같은 게임 횟수로 %s 회를 말씀하셨습니다." % victory_count)
    print()
    for i in range(3):
        print("%d번째 게임을 시작합니다." % (i + 1))
        R_C_P(i + 1)
    print("최종 결과 : %d / 3\n" % player_predict_count)
    time.sleep(0.85)
    if int(victory_count) == player_predict_count:
        print("축하합니다~~ 예측하신 대로 %d 회만큼 이기셨네요! 상금으로 1500 한스를 드리겠습니다!" % player_predict_count)
        money += 1500
    else:
        print("아쉽게도 예측하신 횟수에는 빗나갔습니다...")
    if player_predict_count >= 1:
        print("그리고, %d 회만큼 이기셨으므로 %d 한스를 상금으로 드리겠습니다!" % (player_predict_count, R_C_P_reward[player_predict_count - 1]))
        money += R_C_P_reward[player_predict_count - 1]
    else:
        print("그리고, 묵찌빠는 한 판도 못 이기셨네요... 다음에는 더 잘하기를 바라겠습니다!")
    print(" 보유 금액 : %d 한스" % money)
    player_predict_count = 0
    os.system("pause")



def R_C_P(j): # j는 현재 몇 회인지 알려주는 알림이 역할
    global R_C_P_count
    global player_first_win
    global computer_first_win
    global player_predict_count
    while True:
        print("1. 가위\t2. 바위\t3. 보")
        print()
        print("무엇을 내시겠습니까?")
        player = input()
        computer = str(random.randint(1, 3))
        if player not in ["1", "2", "3"]:
            print(" 잘못 입력하셨습니다.\n")
            continue
        if R_C_P_count == 0:
            print("가위 바위 보!")
        elif R_C_P_count == 1:
            print("묵찌빠!")
        print("플레이어 : %s, 컴퓨터 : %s\n" % (r_c_p[int(player) - 1], r_c_p[int(computer) - 1]))
        time.sleep(1)
        if R_C_P_count == 0 and player == computer: # R_C_P_count = 0이란 말은 아직 이긴 적이 없다는 말
            print("비겼으므로 재경기를 합니다.")
            os.system("pause")
            os.system("cls")
            print("%d번째 게임" % j)
            continue
        elif (player == "1" and computer == "3") or (player == "2" and computer == "1") or (player == "3" and computer == "2"): # 플레이어가 이겼을 때
            print("플레이어가 이겼으므로 플레이어가 공격을 합니다.")
            R_C_P_count = 1
            player_first_win = 1 # 공격권은 플레이어에게로
            computer_first_win = 0 # 만약 공격권이 컴퓨터에게 있었다면 0으로 초기화
            R_C_P(j)
        elif (player == "1" and computer == "2") or (player == "2" and computer == "3") or (player == "3" and computer == "1"): # 컴퓨터가 이겼을 때
            print("컴퓨터가 이겼으므로 컴퓨터가 공격을 합니다.")
            R_C_P_count = 1
            player_first_win = 0 # 만약 공격권이 플레이어에게 있었다면 0으로 초기화
            computer_first_win = 1 # 공격권은 컴퓨터에게로
            R_C_P(j)
        elif R_C_P_count == 1 and player == computer and player_first_win == 1: # 이때 승부가 남! 플레이어가 이겼을 때
            print("플레이어가 이겼습니다!")
            player_predict_count += 1
            os.system("pause")
            R_C_P_count = 0
            player_first_win = 0
            computer_first_win = 0
        elif R_C_P_count == 1 and player == computer and computer_first_win == 1: # 이때 승부가 남! 컴퓨터가 이겼을 때
            print("컴퓨터가 이겼습니다.")
            os.system("pause")
            R_C_P_count = 0
            player_first_win = 0
            computer_first_win = 0
        os.system("cls")
        if R_C_P_count == 0: # 한 판이 끝나면 while문 나온다.
            break

################################## 두 번째 게임

game2_count = 0 # 아직 2번 게임을 안 한 상태. 한 경우 1로 바뀐다. 게임이 끝날 경우 다시 0으로 바뀐다.
game2_remain_count = 3
move_count = 0 # 몇 번 이동했는가
opportunity_count = 5 # 게임 2 한 판 도중 남은 기회 횟수
trace_success_reward = [3000, 7000, 12000, 18000] # 각 단계를 성공했을 경우 상금



def game2_in():
    global game2_remain_count
    if game2_remain_count != 0:
        print("몇 단계를 하시겠습니까? (남은 전체 횟수 : %d 번)\n" % game2_remain_count)
        print("1단계 : 거리의 차가 3 이하")
        print("2단계 : 거리의 차가 2 이하")
        print("3단계 : 거리의 차가 1 이하")
        print("4단계 : 거리의 차가 0")
    while True:
        select = input()
        if select in ["1", "2", "3", "4"]:
            os.system("cls")
            move_game(4 - int(select))
            os.system("cls")
            game2_remain_count -= 1 # 전체 남은 횟수 1 다운
            if game2_remain_count != 0:
                game2_in()
            else:
                game2_remain_count = 3 # 게임이 끝난 후 전체 남은 횟수 원상복귀
            break
        else:
            print(" 잘못 입력하셨습니다.")



def move_game(select): # 이 함수의 매개변수 select는 정수다.
    global money
    global game2_count
    global move_count
    global opportunity_count
    global computer_locate
    global player_locate
    while True:
        while True:
            if game2_count == 0:
                computer_locate = random.randint(1, 30)
                player_locate = random.randint(1, 30)
                if abs(computer_locate - player_locate) <= select:
                    continue
                else:
                    break
            elif game2_count == 1:
                a = random.randint(-5, 5)
                if computer_locate + a < 1:
                    computer_locate = 30 + (computer_locate + a)
                elif computer_locate + a > 30:
                    computer_locate = (computer_locate + a) - 30
                else:
                    computer_locate += a
                break
        print("남은 기회 : %d 회\n" % opportunity_count)
        print("computer", "  " * computer_locate, "▼")
        print("\t    0         5        10        15        20        25        30")
        print("\t   │         │         │         │         │         │         │")
        print("\t   ┌─┬─┬─┬─┬─┬─┬─┬─┬─┬─┬─┬─┬─┬─┬─┬─┬─┬─┬─┬─┬─┬─┬─┬─┬─┬─┬─┬─┬─┬─┐")
        print("\t   └┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┘")
        print("\t   │         │         │         │         │         │         │")
        print("\t    0         5        10        15        20        25        30")
        print("   me   ", "  " * player_locate, "▲")
        if opportunity_count != 0 and abs(computer_locate - player_locate) > select: # 아직 추적을 못 했을 때
            print("\n자신의 위치를 몇 만큼 움직이시겠습니까? (-5 이상 5 이하 입력)")
        if abs(computer_locate - player_locate) <= select: # 추적에 성공했을 때
            print("\n축하합니다! %d 번만에 컴퓨터 위치 추적에 성공하셨습니다!" % (5 - opportunity_count)) # 몇 번만에 맞췄는지 출력
            print("%d 단계를 성공하셨으므로 %d 한스를 드리겠습니다." % (4 - select, trace_success_reward[3 - select]))
            money += trace_success_reward[3 - select]
            print(" 보유 금액 : %d 한스" % money)
            opportunity_count = 5 # 기회 횟수 다시 되돌리기
            game2_count = 0
            os.system("pause")
            return
        elif opportunity_count == 0: # 추적에 실패했을 때
            print("\n컴퓨터 위치 추적에 실패하셨습니다....")
            print(" 보유 금액 : %d 한스" % money)
            opportunity_count = 5 # 기회 횟수 다시 되돌리기
            game2_count = 0
            os.system("pause")
            return
        while True:
            my_move = input()
            if my_move in ["-5", "-4", "-3", "-2", "-1", "0", "1", "2", "3", "4", "5"]:
                game2_count = 1
                opportunity_count -= 1
                if player_locate + int(my_move) < 1:
                    player_locate = 30 + (player_locate + int(my_move))
                elif player_locate + int(my_move) > 30:
                    player_locate = (player_locate + int(my_move)) - 30
                else:
                    player_locate += int(my_move)
                os.system("cls")
                move_game(select)
                break
            else:
                print(" 잘못 입력하셨습니다.")
        if game2_count == 0: # 한 판이 끝나면 while문 나온다.
            break

################################## 세 번째 게임

move_total_1_count = 0 # 한 칸 움직이는 말의 개수
move_total_2_count = 0 # 두 칸 움직이는 말의 개수
move_total_3_count = 0 # 세 칸 움직이는 말의 개수
game3_reward = [80000, 60000, 45000, 30000, 15000, 6000, 0, 0] # 각 등수에 따른 상금



def game3_in():
    global money
    global move_total_1_count # 함수 내에서 선언하면 다른 함수를 호출했을 때 그 함수에서는 사용할 수 없다.(값을 변경할 수 없다.) 그러므로 밖에서 선언! (공부 차원)
    global move_total_2_count # 물론 이 함수 내에서는 사용 가능!
    global move_total_3_count
    global my_rank

    my = horse()
    computer1 = horse()
    computer2 = horse()
    computer3 = horse()
    computer4 = horse()
    computer5 = horse()
    computer6 = horse()
    computer7 = horse()
    print()
    print("나 : ", end = "")
    my.Show()
    print("C1 : ", end = "")
    computer1.Show()
    print("C2 : ", end = "")
    computer2.Show()
    print("C3 : ", end = "")
    computer3.Show()
    print("C4 : ", end = "")
    computer4.Show()
    print("C5 : ", end = "")
    computer5.Show()
    print("C6 : ", end = "")
    computer6.Show()
    print("C7 : ", end = "")
    computer7.Show()
    while True:
        my_rank = 8
        computer1.rank_up() # 내가 순위에 들어가지 않기 위해 따로 함수를 생성
        computer2.rank_up()
        computer3.rank_up()
        computer4.rank_up()
        computer5.rank_up()
        computer6.rank_up()
        computer7.rank_up()
        print("\n현재 나의 등수 : %d / 8" % my_rank)

        if my_rank == 1:
            print()
            print("축하합니다!! %d 등을 하셨으므로 %d 한스를 드리겠습니다!!" % (my_rank, game3_reward[my_rank - 1]))
            money += game3_reward[my_rank - 1]
            print(" 보유 금액 : %d 한스" % money)
            move_total_1_count = 0 # 초기화
            move_total_2_count = 0
            move_total_3_count = 0
            os.system("pause")
            return
        print("\n1, 2, 3 중 어느 숫자를 부르시겠습니까?")
        while True:
            select = input()
            if select in ["1", "2", "3"]:
                os.system("cls")
                if select == "1":
                    move_total_1_count += 1
                elif select == "2":
                    move_total_2_count += 1
                elif select == "3":
                    move_total_3_count += 1
                break
            else:
                print("잘못 입력하셨습니다.")
        print("player : 나 C1 C2 C3 C4 C5 C6 C7")
        print(" 숫자  : ", end = "")
        my.my_separate(select)
        computer1.horse_pro_number(random.randint(1, 9)) # 1부터 9 사이의 숫자를 줘서
        computer2.horse_pro_number(random.randint(1, 9)) # 1 ~ 4가 나오면 한 칸,
        computer3.horse_pro_number(random.randint(1, 9)) # 5 ~ 7이 나오면 두 칸,
        computer4.horse_pro_number(random.randint(1, 9)) # 8 ~ 9가 나오면 세 칸
        computer5.horse_pro_number(random.randint(1, 9)) #즉 각 칸이 나올 확률은 4/9, 1/3, 2/9
        computer6.horse_pro_number(random.randint(1, 9))
        computer7.horse_pro_number(random.randint(1, 9))
        print()
        print()
        print("총 1의 개수 : %d 개" % move_total_1_count)
        print("총 2의 개수 : %d 개" % move_total_2_count)
        print("총 3의 개수 : %d 개" % move_total_3_count)
        if move_total_1_count >= move_total_2_count and move_total_1_count >= move_total_3_count:
            print("1의 개수가 2 또는 3의 개수와 같거나 1의 개수가 가장 많으므로 1을 든 선수는 앞으로 한 칸씩 전진합니다.")
        elif move_total_2_count > move_total_1_count and move_total_2_count >= move_total_3_count:
            print("2의 개수가 3의 개수와 같거나 2의 개수가 가장 많으므로 2를 든 선수는 앞으로 두 칸씩 전진합니다.")
        elif move_total_3_count > move_total_1_count and move_total_3_count > move_total_2_count:
            print("3의 개수가 가장 많으므로 3을 든 선수는 앞으로 세 칸씩 전진합니다.")

        my.horse_go()
        computer1.horse_go()
        computer2.horse_go()
        computer3.horse_go()
        computer4.horse_go()
        computer5.horse_go()
        computer6.horse_go()
        computer7.horse_go()

        print()
        print("나 : ", end = "")
        my.Show()
        print("C1 : ", end = "")
        computer1.Show()
        print("C2 : ", end = "")
        computer2.Show()
        print("C3 : ", end = "")
        computer3.Show()
        print("C4 : ", end = "")
        computer4.Show()
        print("C5 : ", end = "")
        computer5.Show()
        print("C6 : ", end = "")
        computer6.Show()
        print("C7 : ", end = "")
        computer7.Show()

        if my.locate > 8:
            print("\n현재 나의 등수 : %d / 8" % my_rank)
            if my_rank >= 7:
                print("아쉽군요.. 다음에는 더 잘하기를 바라겠습니다!")
            else:
                print("%d 등을 하셨으므로 %d 한스를 드리겠습니다." % (my_rank, game3_reward[my_rank - 1]))
                money += game3_reward[my_rank - 1]
            print(" 보유 금액 : %d 한스" % money)
            move_total_1_count = 0 # 초기화
            move_total_2_count = 0
            move_total_3_count = 0
            os.system("pause")
            return
        move_total_1_count = 0 # 초기화
        move_total_2_count = 0
        move_total_3_count = 0

################################## 네 번째 게임

me_life = [1, 1, 1, 1] # 현재 '나'의 각 위치의 목숨
computer_life = [1, 1, 1, 1] # 현재 컴퓨터의 각 위치의 목숨

me_maybe_bomb = []
C_maybe_bomb = []


game4_ROUND = 1 # 제일 처음 네 번째 게임을 시작할 때 라운드 : 1
game4_STAGE = 1 # 제일 처음 네 번째 게임을 시작할 때 스테이지 : 1

me_score = 0
computer_score = 0

game4_win_reward = [400000, 800000, 1300000, 2500000] # 순서 : 개수가 같을 때, 1개 많을 때, 2개 많을 때, 3개 많을 때
game4_lose_reward = [80000, 60000, 40000, 0] # 순서 : 1개 적을 때, 2개 적을 때, 3개 적을 때

def game4_in():
    global money
    global game4_ROUND
    global game4_STAGE
    global me_life
    global computer_life
    global me_score
    global computer_score
    global me_maybe_bomb
    global C_maybe_bomb

    # 숫자 뽑기에서 숫자 1부터 30까지 각각 10, 20, 30, 40, 50점의 점수를 부여하는 코드
    number_dic = {}
    for i in range(1, 31):
        number_dic.update({i : random.randint(1, 5) * 10})

    # 숫자 뽑기에서 꽝 4개를 설치하는 코드
    number_repetition_check1 = []
    count = 0
    while True:
        bomb_number = random.randint(1, 30)
        if count == 4:
            break
        elif bomb_number not in number_repetition_check1:
            count += 1
            number_repetition_check1.append(bomb_number)
            number_dic[bomb_number] = "●"

    # 숫자 뽑기에서 물음표를 생성하는 코드
    question_mark_dic = {}
    for i in range(1, 31):
        question_mark_dic.update({i : "??"})

    # 숫자 뽑기에서 선택한 숫자를 담아주는 코드(현재는 빈 리스트)
    choice_list = []


    # '나'와 컴퓨터에게 임시폭탄 4개를 자동 분배하는 코드
    A = random.randint(0, 4)
    B = 4 - A
    for i in range(A):
        me_maybe_bomb.append(1)
    for j in range(B):
        C_maybe_bomb.append(1)

    for i in range(4 - A):
        me_maybe_bomb.append(0)
    for j in range(4 - B):
        C_maybe_bomb.append(0)

    random.shuffle(me_maybe_bomb)
    random.shuffle(C_maybe_bomb)

    while True:
        if game4_STAGE != 4 and game4_ROUND == 5: # 마지막 라운드일 때 출력하는 코드
            print("마지막 ROUND의 %d STAGE를 시작합니다.\n" % game4_STAGE)
            print("나의 점수 : %03d, 컴퓨터의 점수 : %03d\n" % (me_score, computer_score))
        elif game4_STAGE != 4: # 세 번의 스테이지를 하고 나서는 출력하지 않는 코드
            print("%d ROUND의 %d STAGE를 시작합니다.\n" % (game4_ROUND, game4_STAGE))
            print("나의 점수 : %03d, 컴퓨터의 점수 : %03d\n" % (me_score, computer_score))

        game4_Show_field()

        # 마지막 라운드 되기 전에 '나' 또는 컴퓨터의 목숨이 전부 소멸됐을 때
        if me_life.count(1) == 0:
            print("마지막 라운드를 진행하려 하는데.. '나'의 목숨이 전부 소멸되었군요....")
            os.system("pause")
            print("안타깝지만 패배하셨습니다. 메뉴로 돌아갑니다.")
            os.system("pause")
            return
        elif computer_life.count(1) == 0:
            print("마지막 라운드를 진행하려 하는데.. 컴퓨터의 목숨이 전부 소멸되었군요!!")
            os.system("pause")
            print("마지막 라운드를 하기 전에 컴퓨터의 목숨 전부를 소멸시키다니 대단하십니다!! 상금으로 %d 한스를 드리겠습니다!!" % 3000000)
            money += 3000000
            print(" 보유 금액 : %d 한스" % money)
            os.system("pause")
            return
        if game4_STAGE <= 3:
            me_card = random.randint(1, 10)
            computer_card = random.randint(1, 10)

            print("카드가 뽑혔습니다.")
            print("    나    : ??")
            print(" computer : %02d" % computer_card)
            print()
            print("승부를 거시겠습니까? (y/n)")
            computer_choice_Y_N = "n" # 일단 컴퓨터의 대답을 no로 설정한다.
            for k in range(1, 11):
                if me_card == k and random.randint(1, 10) >= k: # 내 카드가 k이면 컴퓨터가 yes라고 할 확률은 ((11 - k) / 10) * 100
                    computer_choice_Y_N = "y"
            while True:
                select_Y_or_N = input()
                if select_Y_or_N == "y" or select_Y_or_N == "Y":
                    break
                elif select_Y_or_N == "n" or select_Y_or_N == "N":
                    break
                else:
                    print("잘못 입력하셨습니다.")
            print("    나    : %02d" % me_card)
            print(" computer : %02d\n" % computer_card)
            if select_Y_or_N == "y" or select_Y_or_N == "Y": # 내가 yes를 했을 때
                if computer_choice_Y_N == "y": # '나'와 컴퓨터 둘 다 yes를 했을 때 카드 숫자 비교
                    if me_card > computer_card:
                        print("컴퓨터의 숫자보다 높으므로 '나'가 뽑기 기회를 가졌습니다!")
                        print("컴퓨터는 점수 50 을 잃고 '나'는 뽑기 화면으로 이동합니다.")
                        computer_score -= 50
                        if computer_score < 0:
                            computer_score = 0
                        game4_STAGE += 1 # 한 스테이지 완료
                        os.system("pause")
                        me_score = me_pick_number(me_score, number_dic, question_mark_dic, choice_list)
                    elif me_card == computer_card:
                        print("컴퓨터의 숫자와 같으므로 비겼습니다. 재경기를 합니다.")
                        os.system("pause")
                    elif me_card < computer_card:
                        print("컴퓨터의 숫자가 높으므로 컴퓨터가 뽑기 기회를 가집니다. 뽑기 화면으로 이동합니다.")
                        print("'나'는 점수 50 을 잃고 컴퓨터는 뽑기 화면으로 이동합니다.")
                        me_score -= 50
                        if me_score < 0:
                            me_score = 0
                        game4_STAGE += 1 # 한 스테이지 완료
                        os.system("pause")
                        computer_score = computer_pick_number(computer_score, number_dic, question_mark_dic, choice_list)
                elif computer_choice_Y_N == "n":
                    print("컴퓨터가 승부를 포기하여 '나'가 이겼습니다! 뽑기 화면으로 이동합니다.")
                    game4_STAGE += 1 # 한 스테이지 완료
                    os.system("pause")
                    me_score = me_pick_number(me_score, number_dic, question_mark_dic, choice_list)
            elif select_Y_or_N == "n" or select_Y_or_N == "N": # 내가 no를 했을 때
                if computer_choice_Y_N == "y":
                    print("'나'가 승부를 포기하여 컴퓨터가 이겼습니다. 뽑기 화면으로 이동합니다.")
                    game4_STAGE += 1 # 한 스테이지 완료
                    os.system("pause")
                    computer_score = computer_pick_number(computer_score, number_dic, question_mark_dic, choice_list)
                elif computer_choice_Y_N == "n":
                    print("'나'와 컴퓨터가 승부를 포기하였습니다. 스테이지 %d를 종료합니다." % game4_STAGE)
                    game4_STAGE += 1 # 한 스테이지 완료
                    os.system("pause")
        elif game4_STAGE == 4: # 세 번의 STAGE가 끝나면 game4_STAGE가 4가 된다.
            game4_STAGE = 1
            if game4_ROUND == 5:
                print("마지막 라운드가 끝났습니다. 폭탄 던지기 시스템으로 이동합니다.")
            else:
                print("%d 라운드가 끝났습니다. 폭탄 던지기 시스템으로 이동합니다." % game4_ROUND)
            os.system("pause")
            os.system("cls")
            bomb_throw_system()
            me_maybe_bomb = [] # 임시 폭탄 초기화
            C_maybe_bomb = []
            os.system("cls")
            if game4_ROUND == 5:
                game4_ROUND = 1 # 전부 처음으로 초기화
                game4_STAGE = 1
                me_score = 0
                computer_score = 0
                print("네 번째 게임이 모두 끝났습니다!! 최종 결과를 발표합니다.")
                os.system("pause")
                me_maybe_bomb = [0, 0, 0, 0] # 마지막 라운드 끝나고 나서, 임시 폭탄을 출력하지 않는 코드.
                C_maybe_bomb = [0, 0, 0, 0]
                os.system("cls")
                print(3)
                time.sleep(0.85)
                print(2)
                time.sleep(0.85)
                print(1)
                time.sleep(0.85)
                os.system("cls")
                game4_Show_field()
                print("'나'의 목숨 개수 : %d 개, 컴퓨터의 목숨 개수 : %d 개\n" % (me_life.count(1), computer_life.count(1)))
                if me_life.count(1) > computer_life.count(1):
                    print("축하합니다~ 컴퓨터보다 목숨이 많으므로 게임에서 승리하셨습니다!!")
                    os.system("pause")
                    print("\n컴퓨터보다 목숨이 %d 개 많으므로 상금으로 %d 한스를 드리겠습니다!!" % (me_life.count(1) - computer_life.count(1), game4_win_reward[me_life.count(1) - computer_life.count(1)]))
                    money += game4_win_reward[me_life.count(1) - computer_life.count(1)]
                    print(" 보유 금액 : %d 한스" % money)
                elif me_life.count(1) == computer_life.count(1):
                    print("'나'와 컴퓨터의 목숨의 개수가 같으므로 비겼습니다.")
                    os.system("pause")
                    print("\n비겼으므로 상금으로 %d 한스를 드리겠습니다." % game4_win_reward[me_life.count(1) - computer_life.count(1)])
                    money += game4_win_reward[me_life.count(1) - computer_life.count(1)]
                    print(" 보유 금액 : %d 한스" % money)
                elif me_life.count(1) < computer_life.count(1):
                    print("컴퓨터보다 목숨이 적으므로 패배하셨습니다.")
                    os.system("pause")
                    print("\n그렇지만 컴퓨터보다 목숨이 %d 개 적으므로 %d 한스를 드리겠습니다." % (computer_life.count(1) - me_life.count(1), game4_lose_reward[computer_life.count(1) - me_life.count(1) - 1]))
                    money += game4_lose_reward[computer_life.count(1) - me_life.count(1) - 1]
                    print(" 보유 금액 : %d 한스" % money)
                me_maybe_bomb = [] # 임시 폭탄도 완전 초기화
                C_maybe_bomb = []
                me_life = [1, 1, 1, 1] # 목숨도 완전 되돌리기
                computer_life = [1, 1, 1, 1]
                os.system("pause")
                return
            game4_ROUND += 1
            game4_in()
            break
        os.system("cls")



def game4_Show_field():
    print("         나1 C4")
    print("         ", end = "")
    if me_life[0] == 1:
        print("○", end = "")
    elif me_life[0] == 0:
        print("×", end = "")
    print("  ", end = "")
    if computer_life[3] == 1:
        print("○")
    elif computer_life[3] == 0:
        print("×")
    print("         ", end = "")
    if me_maybe_bomb[0] == 0:
        print("  ", end = "")
    elif me_maybe_bomb[0] == 1:
        print("●", end = "")
    print("  ", end = "")
    if C_maybe_bomb[3] == 0:
        print("  ")
    elif C_maybe_bomb[3] == 1:
        print("●")

    print(" C1  ", end = "")
    if computer_life[0] == 1:
        print("○", end = "")
    elif computer_life[0] == 0:
        print("×", end = "")
    if C_maybe_bomb[0] == 0:
        print("  ", end = "")
    elif C_maybe_bomb[0] == 1:
        print("●", end = "")
    print("      ", end = "")
    if me_maybe_bomb[3] == 0:
        print("  ", end = "")
    elif me_maybe_bomb[3] == 1:
        print("●", end = "")
    if me_life[3] == 1:
        print("○", end = "")
    elif me_life [3] == 0:
        print("×", end = "")
    print(" 나4")

    print(" 나2 ", end = "")
    if me_life[1] == 1:
        print("○", end = "")
    elif me_life[1] == 0:
        print("×", end = "")
    if me_maybe_bomb[1] == 0:
        print("  ", end = "")
    elif me_maybe_bomb[1] == 1:
        print("●", end = "")
    print("      ", end = "")
    if C_maybe_bomb[2] == 0:
        print("  ", end = "")
    elif C_maybe_bomb[2] == 1:
        print("●", end = "")
    if computer_life[2] == 1:
        print("○", end = "")
    elif computer_life[2] == 0:
        print("×", end = "")
    print(" C3")

    print("         ", end = "")
    if C_maybe_bomb[1] == 0:
        print("  ", end = "")
    elif C_maybe_bomb[1] == 1:
        print("●", end = "")
    print("  ", end = "")
    if me_maybe_bomb[2] == 0:
        print("  ")
    elif me_maybe_bomb[2] == 1:
        print("●")
    print("         ", end = "")
    if computer_life[1] == 1:
        print("○", end = "")
    elif computer_life[1] == 0:
        print("×", end = "")
    print("  ", end = "")
    if me_life[2] == 1:
        print("○")
    elif me_life[2] == 0:
        print("×")
    print("         C2  나3")
    print()



def me_pick_number(score, number_dic, question_mark_dic, choice_list): # 내가 숫자 고르는 함수
    making_1_30_list = []
    plus_point = 0
    choice_number = 5 # 한 스테이지 당 최대 뽑을 수 있는 숫자 개수를 5개로 제한.
    for i in range(1, 31):
        making_1_30_list.append(str(i))
    while True:
        os.system("cls")
        print("현재 나의 점수 : %03d" % (score + plus_point))
        print("뽑을 수 있는 숫자 개수 : %d\n" % choice_number)
        for i in range(0, 3):
            for j in range(0, 10):
                print("%02d번 " % list(question_mark_dic.keys())[i * 10 + j], end = ": ")
                print(question_mark_dic.get(i * 10 + j + 1), end = ",  ")
            print()
        print()
        if choice_number == 0:
            print("더 이상 숫자를 뽑을 수 없으므로 게임으로 돌아갑니다.")
            score += plus_point
            os.system("pause")
            return score
        print("어느 숫자를 뽑으시겠습니까? (n 누를 시 종료)")
        select = input()
        if select in making_1_30_list and select not in choice_list: # 입력한 값이 1부터 30 안에 있고, 이전에 뽑은 숫자가 아니면
            choice_number -= 1
            choice_list.append(select) # 뽑은 숫자 저장 (안 겹치게)
            question_mark_dic[int(select)] = number_dic[int(select)] # 뽑은 숫자의 점수 또는 꽝을 보여주는 코드
            print("%s번!" % select)
            if number_dic.get(int(select)) != "●": # 선택한 숫자가 꽝이 아니면
                print("%s번을 뽑아 %d 점을 획득하였습니다!" % (select, number_dic.get(int(select))))
                plus_point += number_dic.get(int(select))
                os.system("pause")
            elif number_dic.get(int(select)) == "●": # 선택한 숫자가 꽝이면
                print("꽝(●)을 뽑으셨습니다!! 이번에 획득한 점수는 모두 사라졌습니다. 게임으로 돌아갑니다.")
                plus_point = 0 # 굳이 없어도 되는 코드
                os.system("pause")
                return score
        elif select in choice_list:
            print("%s번!" % select)
            print("이미 뽑은 숫자입니다. 다시 입력해주세요.")
            os.system("pause")
        elif select == "n" or select == "N":
            print("뽑기를 마치고 게임으로 돌아갑니다.")
            score += plus_point
            os.system("pause")
            return score
        else:
            print("잘못 입력하셨습니다.")
            os.system("pause")



def computer_pick_number(score, number_dic, question_mark_dic, choice_list): # 컴퓨터가 숫자 고르는 함수
    making_1_30_list = []
    plus_point = 0
    choice_number = 5 # 한 스테이지 당 최대 뽑을 수 있는 숫자 개수를 5개로 제한.
    computer_pick_count = 0 # 처음에는 컴퓨터도 숫자를 뽑아야 하므로, 숫자를 뽑고 나서는 1로 바뀌면서 뽑을지 말지 확률이 적용됨
    for i in range(1, 31):
        making_1_30_list.append(str(i))
    while True:
        os.system("cls")
        print("현재 컴퓨터의 점수 : %03d" % (score + plus_point))
        print("뽑을 수 있는 숫자 개수 : %d\n" % choice_number)
        for i in range(0, 3):
            for j in range(0, 10):
                print("%02d번 " % list(question_mark_dic.keys())[i * 10 + j], end = ": ")
                print(question_mark_dic.get(i * 10 + j + 1), end = ",  ")
            print()
        print()
        if choice_number == 0:
            print("더 이상 숫자를 뽑을 수 없으므로 게임으로 돌아갑니다.")
            score += plus_point
            os.system("pause")
            return score
        print("컴퓨터가 숫자를 뽑습니다.")
        os.system("pause")
        if computer_pick_count == 0 or random.randint(1, 4) <= 3: # 아직 뽑지 않았거나, 뽑고 난 후 다시 뽑을 확률이 75%일 때
            while True:
                select = str(random.randint(1, 30))
                if select not in choice_list:
                    break
        else:
            print("컴퓨터가 숫자 뽑기를 종료하였습니다. 게임으로 돌아갑니다.")
            score += plus_point
            os.system("pause")
            return score
        if select not in choice_list: # 입력한 값이 1부터 30 안에 있고, 이전에 뽑은 숫자가 아니면
            choice_number -= 1
            computer_pick_count = 1
            choice_list.append(select) # 뽑은 숫자 저장 (안 겹치게)
            question_mark_dic[int(select)] = number_dic[int(select)] # 뽑은 숫자의 점수 또는 꽝을 보여주는 코드
            print("%s번!" % select)
            if number_dic.get(int(select)) != "●": # 선택한 숫자가 꽝이 아니면
                print("%s번을 뽑아 %d 점을 획득하였습니다!" % (select, number_dic.get(int(select))))
                plus_point += number_dic.get(int(select))
                os.system("pause")
            elif number_dic.get(int(select)) == "●": # 선택한 숫자가 꽝이면
                print("꽝(●)을 뽑으셨습니다!! 이번에 획득한 점수는 모두 사라졌습니다. 게임으로 돌아갑니다.")
                plus_point = 0 # 굳이 없어도 되는 코드
                os.system("pause")
                return score



def bomb_throw_system():
    global me_score
    global computer_score
    global me_maybe_bomb
    global C_maybe_bomb
    global me_life
    global computer_life
    if game4_ROUND == 5:
        print("마지막 ROUND 폭탄 던지기 시스템\n")
    else:
        print("%d ROUND 폭탄 던지기 시스템\n" % game4_ROUND)
    print("나의 점수 : %03d, 컴퓨터의 점수 : %03d\n" % (me_score, computer_score))
    game4_Show_field()
    if me_score > computer_score:
        print("현재 '나'의 점수가 높으므로 먼저 '나'와 컴퓨터의 점수에 현재 컴퓨터의 점수를 각각 차감합니다.")
        me_score -= computer_score
        computer_score = 0
    elif me_score < computer_score:
        print("현재 컴퓨터의 점수가 높으므로 먼저 '나'와 컴퓨터의 점수에 현재 '나'의 점수를 각각 차감합니다.")
        computer_score -= me_score
        me_score = 0
    elif me_score == computer_score:
        print("현재 '나'의 점수와 컴퓨터의 점수와 같으므로 각각 0 이 됩니다.")
        computer_score = 0
        me_score = 0
    os.system("pause")
    if me_score > computer_score:
        while True:
            os.system("cls")
            if game4_ROUND == 5:
                print("마지막 ROUND 폭탄 던지기 시스템\n")
            else:
                print("%d ROUND 폭탄 던지기 시스템\n" % game4_ROUND)
            print("나의 점수 : %03d, 컴퓨터의 점수 : %03d\n" % (me_score, computer_score))
            game4_Show_field()
            print("1. 임시 폭탄 던지기 (하나) : 80, 2. 상대방의 임시 폭탄 위치 바꾸기 : 50, 3. 찬스 발동 종료")
            print()
            if me_maybe_bomb.count(1) == 0: # 임시 폭탄이 모두 '나'에게 있을 경우
                print("이미 임시 폭탄이 모두 컴퓨터에게 있으므로 찬스 발동을 종료합니다.")
                os.system("pause")
                break
            if me_score < 50:
                print("점수가 모자라여 찬스를 발동할 수 없습니다. 찬스 발동을 종료합니다.")
                os.system("pause")
                break
            print("어느 것을 선택하시겠습니까?")
            select = input()
            if select == "1":
                if me_maybe_bomb.count(1) == 0:
                    print("'나'가 갖고 있는 임시폭탄이 없습니다.")
                    os.system("pause")
                    continue
                if me_score >= 80:
                    me_score -= 80
                    print("'나'가 갖고 있는 폭탄을 컴퓨터에게 임의로 던집니다.")
                    os.system("pause")
                    while True:
                        a = random.randint(0, 3) # 내 임시폭탄이 있는 곳을 비어있게 만들기
                        if me_maybe_bomb[a] == 1:
                            me_maybe_bomb[a] = 0
                            break
                    while True:
                        b = random.randint(0, 3) # 컴퓨터의 빈 곳을 임시폭탄이 있게 만들기
                        if C_maybe_bomb[b] == 0:
                            C_maybe_bomb[b] = 1
                            break
                    print("\n컴퓨터에게 임시폭탄을 던졌습니다. enter를 눌러 확인하세요.")
                    os.system("pause")
                    continue
                elif me_score < 80:
                    print("\n점수가 모자라여 찬스를 발동할 수 없습니다")
                    os.system("pause")
            elif select == "2":
                if C_maybe_bomb.count(1) == 4:
                    print("이미 임시 폭탄이 모두 컴퓨터에게 있습니다.")
                    os.system("pause")
                    continue
                me_score -= 50
                print("\n컴퓨터가 들고 있는 임시 폭탄의 위치를 임의로 바꿉니다.")
                os.system("pause")
                random.shuffle(C_maybe_bomb)
                print("\n컴퓨터의 임시 폭탄의 위치를 변경하였습니다. enter를 눌러 확인하세요.")
                os.system("pause")
                continue
            elif select == "3":
                print("찬스 발동을 종료합니다.")
                os.system("pause")
                break
            else:
                print("잘못 입력하셨습니다.")
                os.system("pause")
    elif me_score < computer_score:
        while True:
            os.system("cls")
            if game4_ROUND == 5:
                print("마지막 ROUND 폭탄 던지기 시스템\n")
            else:
                print("%d ROUND 폭탄 던지기 시스템\n" % game4_ROUND)
            print("나의 점수 : %03d, 컴퓨터의 점수 : %03d\n" % (me_score, computer_score))
            game4_Show_field()
            print("1. 임시 폭탄 던지기 (하나) : 80, 2. 상대방의 임시 폭탄 위치 바꾸기 : 50, 3. 찬스 발동 종료")
            print()
            if C_maybe_bomb.count(1) == 0: # 임시 폭탄이 모두 '나'에게 있을 경우
                print("이미 임시 폭탄이 모두 '나'에게 있으므로 찬스 발동을 종료합니다.")
                os.system("pause")
                break
            if computer_score < 50:
                print("점수가 모자라여 찬스를 발동할 수 없습니다. 찬스 발동을 종료합니다.")
                os.system("pause")
                break
            a = random.randint(1, 3)
            if a <= 2: # 부분 확률
                if computer_score >= 80:
                    computer_score -= 80
                    print("컴퓨터가 폭탄 던지기 찬스를 발동하였습니다.")
                    print("컴퓨터가 갖고 있는 폭탄을 '나'에게 임의로 던집니다.")
                    print()
                    os.system("pause")
                    while True:
                        b = random.randint(0, 3) # 컴퓨터 임시폭탄이 있는 곳을 비어있게 만들기
                        if C_maybe_bomb[b] == 1:
                            C_maybe_bomb[b] = 0
                            break
                    while True:
                        a = random.randint(0, 3) # '나'의 빈 곳을 임시폭탄이 있게 만들기
                        if me_maybe_bomb[a] == 0:
                            me_maybe_bomb[a] = 1
                            break
                    print("\n'나'에게 임시폭탄을 던졌습니다. enter를 눌러 확인하세요.")
                    os.system("pause")
            else:
                b = random.randint(1, 2)
                c = random.randint(1, 3)
                if b == 1:
                    if (me_life[0] == 0 and me_maybe_bomb[0] == 1) or (me_life[1] == 0 and me_maybe_bomb[1] == 1) or (me_life[2] == 0 and me_maybe_bomb[2] == 1) or (me_life[3] == 0 and me_maybe_bomb[3] == 1):
                        computer_score -= 50
                        print("컴퓨터가 상대방의 임시 폭탄 위치 바꾸기 찬스를 발동하였습니다.")
                        print("'나'가 들고 있는 임시 폭탄의 위치를 임의로 바꿉니다.")
                        print()
                        os.system("pause")
                        random.shuffle(me_maybe_bomb)
                        print("'나'의 임시 폭탄의 위치를 변경하였습니다. enter를 눌러 확인하세요.")
                        os.system("pause")
                    elif computer_score >= 80 and C_maybe_bomb.count(1) >= c: # 컴퓨터의 점수가 80 이상인데 컴퓨터의 임시 폭탄 개수가 c개 이상일 경우 다시
                        continue
                    else:
                        print("컴퓨터가 찬스 발동을 종료했습니다.")
                        os.system("pause")
                        break
    elif me_score == computer_score:
        print()
        print("'나'와 컴퓨터의 점수가 0 이므로 찬스를 발동할 수 없어 그대로 넘어갑니다.")
        os.system("pause")
    os.system("cls")
    if game4_ROUND == 5:
        print("마지막 ROUND 폭탄 던지기 시스템\n")
    else:
        print("%d ROUND 폭탄 던지기 시스템\n" % game4_ROUND)
    print("나의 점수 : %03d, 컴퓨터의 점수 : %03d\n" % (me_score, computer_score))
    game4_Show_field()
    print("자, 여기서 진짜 폭탄은??")
    time.sleep(2.75)
    print(3)
    time.sleep(0.85)
    print(2)
    time.sleep(0.85)
    print(1)
    time.sleep(0.85)

    # 임시 폭탄 3개를 없애는 코드
    maybe_bomb_sum_list = me_maybe_bomb + C_maybe_bomb
    maybe_bomb_remove_count = 0
    while maybe_bomb_remove_count < 3:
        remove_element = random.randint(0, 7)
        if maybe_bomb_sum_list[remove_element] == 1:
            maybe_bomb_remove_count += 1
            maybe_bomb_sum_list[remove_element] = 0
    me_maybe_bomb = maybe_bomb_sum_list[:4]
    C_maybe_bomb = maybe_bomb_sum_list[4:]

    os.system("cls")
    if game4_ROUND == 5:
        print("마지막 ROUND 폭탄 던지기 시스템\n")
    else:
        print("%d ROUND 폭탄 던지기 시스템\n" % game4_ROUND)
    print("나의 점수 : %03d, 컴퓨터의 점수 : %03d\n" % (me_score, computer_score))
    game4_Show_field()
    print("저기에 있었습니다!!")
    os.system("pause")

    for i in range(4): # 이미 목숨이 소멸됐는데 임시 폭탄이 있으면 무효라고 출력하는 코드
        if (me_life[i] == 0 and me_maybe_bomb[i] == 1) or (computer_life[i] == 0 and C_maybe_bomb[i] == 1):
            os.system("cls")
            if game4_ROUND == 5:
                print("마지막 ROUND 폭탄 던지기 시스템\n")
            else:
                print("%d ROUND 폭탄 던지기 시스템\n" % game4_ROUND)
            print("나의 점수 : %03d, 컴퓨터의 점수 : %03d\n" % (me_score, computer_score))
            game4_Show_field()
            print("그러나 이미 목숨이 소멸되어 있는 곳이므로 진짜 폭탄은 없는 걸로 처리됩니다.")
            os.system("pause")
            return

    for i in range(4): # 진짜폭탄 있는 곳의 목숨을 없애는 코드
        if me_maybe_bomb[i] == 1:
            me_life[i] = 0
        elif C_maybe_bomb[i] == 1:
            computer_life[i] = 0

    os.system("cls")
    if game4_ROUND == 5:
        print("마지막 ROUND 폭탄 던지기 시스템\n")
    else:
        print("%d ROUND 폭탄 던지기 시스템\n" % game4_ROUND)
    print("나의 점수 : %03d, 컴퓨터의 점수 : %03d\n" % (me_score, computer_score))
    game4_Show_field()
    print("진짜 폭탄이 있는 곳은 목숨이 소멸됩니다.")
    os.system("pause")

################################## 3. 현재 장비 레벨 및 보유 금액

def CurrentState():
    print()
    for i in range(6):
        print(" %s 레벨 : %2d, %s 공격력 : %03d" % (equipment_sort[i], level[i], equipment_sort[i], equipment_power[i]))
        # print(" 상의 레벨 : %2d, 상의 공격력 : %03d" % (cloth_level, cloth_equipment_power))
        # print(" 하의 레벨 : %2d, 하의 공격력 : %03d" % (pants_level, pants_equipment_power))
        # print(" 모자 레벨 : %2d, 모자 공격력 : %03d" % (cap_level, cap_equipment_power))
        # print(" 망토 레벨 : %2d, 망토 공격력 : %03d" % (clock_level, clock_equipment_power))
        # print(" 무기 레벨 : %2d, 무기 공격력 : %03d" % (weapon_level, weapon_equipment_power))
        # print(" 방패 레벨 : %2d, 방패 공격력 : %03d" % (shield_level, shield_equipment_power))
    print()
    print(" 현재 장비 총 레벨 : %03d" % equipment_total_level)
    print(" 현재 공격력 : %03d" % ATTACK_POWER)
    print(" 보유 금액 : %d 한스" % money)
    print(" 현재 목숨 개수 : %d 개" % life)
    print()

################################## 4. 장비 강화

equipment_sort = ["상의", "하의", "모자", "망토", "무기", "방패"]
# 순서 : 상의, 하의, 모자, 망토, 무기, 방패
level = [0, 0, 0, 0, 0, 0] # 각 장비 레벨
equipment_power = [0, 0, 0, 0, 0, 0] # 각 장비 공격력
add_power = [3, 3, 4, 4, 8, 6] # 강화 성공 시 올라가는 제일 기초 공격력 증가량 / 가변
base_power = [3, 3, 4, 4, 8, 6] # 강화 성공 시 올라가는 제일 기초 공격력 증가량 / 불변

require_money = [30, 30, 40, 40, 100, 80] # 강화에 필요한 실제 금액 (장비 레벨이 오를수록 올라간다.)
add_money = [30, 30, 40, 40, 100, 80] # 강화에 필요한 제일 기초 금액. 5강, 10강, 15강 달성시 이것도 바뀐다.

probability = [100, 80, 60, 40] # 0강, 5강, 10강, 15강 이상시 각 요소 확률 적용
equipment_probability_step = [0, 0, 0, 0, 0, 0]

continuity_Reinforcement = 0 # 연속 강화시 1로 바뀌면서 "한 번 더" 라는 문구 출력



def Reinforcement_in():
    os.system("cls")
    print(" 어느 장비를 강화하시겠습니까?")
    print()
    print(" 1. 상의")
    print(" 2. 하의")
    print(" 3. 모자")
    print(" 4. 망토")
    print(" 5. 무기")
    print(" 6. 방패")
    print(" 7. 강화 종료")
    print()
    while True:
        select = input()
        if select in ["1", "2", "3", "4", "5", "6"]:
            os.system("cls")
            Reinforcement_Confirm(int(select))
            break
        elif select == "7":
            print("강화를 종료하고 메뉴로 돌아갑니다.")
            break
        else:
            print("잘못 입력하셨습니다.")



def Reinforcement_Confirm(i):
    global probability_step
    global continuity_Reinforcement
    if game2 == 0 and level[i - 1] == 5:
        print("첫 번째 보스를 클리어하지 않아 더 이상 강화를 할 수 없습니다. 첫 번째 보스를 클리어하고 오세요.\n")
        continuity_Reinforcement = 0
        return
    if game3 == 0 and level [i - 1] == 10:
        print("두 번째 보스를 클리어하지 않아 더 이상 강화를 할 수 없습니다. 두 번째 보스를 클리어하고 오세요.\n")
        continuity_Reinforcement = 0
        return
    if game4 == 0 and level [i - 1] == 15:
        print("세 번째 보스를 클리어하지 않아 더 이상 강화를 할 수 없습니다. 세 번째 보스를 클리어하고 오세요.\n")
        continuity_Reinforcement = 0
        return
    if level[i - 1] == 20:
        print(" 현재 %s 레벨이 최고 레벨에 도달하였으므로 더 이상 강화를 할 수 없습니다. 메뉴로 돌아갑니다." % equipment_sort[i - 1])
        print()
    elif money < require_money[i - 1]:
        if continuity_Reinforcement == 0:
            print(" 보유 금액 : %d 한스" % money)
        print(" 필요 한스 : %d 한스" % require_money[i - 1])
        print()
        print(" 한스가 모자라 강화를 할 수 없습니다. 메뉴로 돌아갑니다.")
        continuity_Reinforcement = 0
    else:
        if continuity_Reinforcement == 0:    # 메뉴에서 4번을 누르고 실행했을 경우 출력
            print(" 현재 %s 레벨 : %d" % (equipment_sort[i - 1], level[i - 1]))
            print(" 보유 금액 : %d 한스" % money)
            print()
        print(" 필요 한스 : %d 한스" % require_money[i - 1])
        print(" 공격력 증가량 : %d" % add_power[i - 1])
        if level[i - 1] in [0, 1, 2, 3, 4, 5, 10, 15]:
            print(" (성공 확률 : {}%, 유지 확률 : {}%)".format(probability[equipment_probability_step[i - 1]], 100 - probability[equipment_probability_step[i - 1]]))
        elif level[i - 1] in [6, 7, 8, 9, 11, 12, 13, 14, 16, 17, 18, 19]:
            print(" 강화시 실패하여 레벨이 떨어질 수 있습니다.")
            print(" (성공 확률 : {}%, 하락 확률 : {}%)".format(probability[equipment_probability_step[i - 1]], 100 - probability[equipment_probability_step[i - 1]]))
        while True:
            if continuity_Reinforcement != 0:
                print(" 한 번 더", end = "")
            print(" 강화하시겠습니까? (y/n)")
            select_Y_or_N = input()
            if select_Y_or_N == "y" or select_Y_or_N == "Y":
                continuity_Reinforcement = 1
                os.system("cls")
                print("강화를 시작합니다.")
                print("3")
                time.sleep(0.85)
                print("2")
                time.sleep(0.85)
                print("1")
                time.sleep(0.85)
                os.system("cls")
                my_number = random.randint(1, 100)
                if my_number <= probability[equipment_probability_step[i - 1]]:
                    Reinforcement_Success(i)
                    Reinforcement_Confirm(i)
                    break
                else:
                    Reinforcement_Fail(i)
                    Reinforcement_Confirm(i)
                    break
            elif select_Y_or_N == "n" or select_Y_or_N == "N":
                print("강화를 종료하고 메뉴로 돌아갑니다.")
                continuity_Reinforcement = 0
                return
            else:
                print("잘못 입력하셨습니다.")



def Reinforcement_Success(i):
    global money
    global probability_step
    print(" 강화에 성공하였습니다!!")
    print(" 이전 %s 레벨 : %d -> 현재 %s 레벨 : %d" % (equipment_sort[i - 1], level[i - 1], equipment_sort[i - 1], level[i - 1] + 1))
    print(" 이전 %s 공격력 : %d -> 현재 %s 공격력 : %d" % (equipment_sort[i - 1], equipment_power[i - 1], equipment_sort[i - 1], equipment_power[i - 1] + add_power[i - 1]))
    money -= require_money[i - 1]
    level[i - 1] += 1
    equipment_power[i - 1] += add_power[i - 1]
    if level[i - 1] in [5, 10, 15]:
        require_money[i - 1] *= 2
        add_money[i - 1] *= 10
        equipment_probability_step[i - 1] += 1
        add_power[i - 1] += base_power[i - 1]
    else:
        require_money[i - 1] += add_money[i - 1]
    print(" 현재 금액 : %d 한스" % money)
    print()



def Reinforcement_Fail(i):
    global money
    print(" 강화에 실패하였습니다.")
    if level[i - 1] in [5, 10, 15]:
        print(" 이전 %s 레벨 : %d -> 현재 %s 레벨 : %d" % (equipment_sort[i - 1], level[i - 1], equipment_sort[i - 1], level[i - 1]))
        print(" 이전 %s 공격력 : %d -> 현재 %s 공격력 : %d" % (equipment_sort[i - 1], equipment_power[i - 1], equipment_sort[i - 1], equipment_power[i - 1]))
    else:
        print(" 이전 %s 레벨 : %d -> 현재 %s 레벨 : %d" % (equipment_sort[i - 1], level[i - 1], equipment_sort[i - 1], level[i - 1] - 1))
        print(" 이전 %s 공격력 : %d -> 현재 %s 공격력 : %d" % (equipment_sort[i - 1], equipment_power[i - 1], equipment_sort[i - 1], equipment_power[i - 1] - add_power[i - 1]))
    money -= require_money[i - 1]
    if level[i - 1] in [6, 7, 8, 9, 11, 12, 13, 14, 16, 17, 18, 19]:
        require_money[i - 1] -= add_money[i - 1]
        level[i - 1] -= 1
        equipment_power[i - 1] -= add_power[i - 1]
    print(" 현재 금액 : %d 한스" % money)
    print()

################################## 5. 보스와 싸운다.

Boss_attack_require_equipment_total_level = [20, 45, 80, 108] # 보스 공격 시 필요한 장비 총 레벨
Boss_power = [90, 300, 700, 1180] # 각 보스 공격력
Boss_attack_success_reward = [3000, 30000, 300000] # 각 보스 클리어시 지급되는 한스



def Boss_attack():
    os.system("cls")
    print(" 어느 보스를 쓰러뜨리시겠습니까?")
    print()
    if game2 == 0:
        print(" 1. 크라운 롤리폴리 (첫 번재 보스) [ 공격력 : 90 ]")
    else:
        print(" 1. 첫 번째 보스 <격파>")
    if game2 == 0:
        print(" 2. ●●●●●● [잠겨 있습니다.]")
    elif game2 == 1 and game3 == 0:
        print(" 2. 킹 베드보그 (두 번째 보스) [ 공격력 : 300 ]")
    elif game2 == 1 and game3 == 1:
        print(" 2. 두 번째 보스 <격파>")
    if game3 == 0:
        print(" 3. ●●●●●● [잠겨 있습니다.]")
    elif game3 == 1 and game4 == 0:
        print(" 3. 스파도르 나이트 (세 번째 보스) [ 공격력 : 700 ]")
    elif game3 == 1 and game4 == 1:
        print(" 3. 세 번째 보스 <격파>")
    if game4 == 0:
        print(" 4. ●●●●●● [잠겨 있습니다.]")
    elif game4 == 1:
        print(" 4. 외눈 키클롭스 (마지막 보스) [ 공격력 : 1180 ]")
    print(" 5. 메뉴로 돌아간다.")
    print()
    while True:
        select = input()
        if select in ["1", "2", "3", "4"]:
            os.system("cls")
            Boss_attack_condition(select)
            break
        elif select == "5":
            print("메뉴로 돌아갑니다.")
            break
        else:
            print("잘못 입력하셨습니다.")



def Boss_attack_condition(select):
    if select == "2" and game2 == 0:
        print("첫 번째 보스를 클리어하지 않았습니다. 첫 번째 보스를 클리어하고 오세요.\n메뉴로 돌아갑니다.\n")
        return
    elif select == "3" and game3 == 0:
        print("두 번째 보스를 클리어하지 않았습니다. 두 번째 보스를 클리어하고 오세요.\n메뉴로 돌아갑니다.\n")
        return
    elif select == "4" and game4 == 0:
        print("세 번째 보스를 클리어하지 않았습니다. 세 번째 보스를 클리어하고 오세요.\n메뉴로 돌아갑니다.\n")
        return
    elif select == "1" and game2 == 1:
        print("이미 첫 번째 보스를 클리어하셨습니다. 메뉴로 돌아갑니다.\n")
        return
    elif select == "2" and game3 == 1:
        print("이미 두 번째 보스를 클리어하셨습니다. 메뉴로 돌아갑니다.\n")
        return
    elif select == "3" and game4 == 1:
        print("이미 세 번째 보스를 클리어하셨습니다. 메뉴로 돌아갑니다.\n")
        return
    print("현재 나의 장비 총 레벨 : %d" % equipment_total_level)
    print("보스를 쓰러뜨리기 위해 필요한 장비 총 레벨 : %d\n" % Boss_attack_require_equipment_total_level[int(select) - 1])
    if equipment_total_level < Boss_attack_require_equipment_total_level[int(select) - 1]:
        print("장비 총 레벨이 부족하여 보스를 공격을 할 수 없습니다. 메뉴로 돌아갑니다.")
        return
    else:
        Boss_attack_go(select)



def Boss_attack_go(select):
    if select == "1":
        print("첫 번째", end = "")
    elif select == "2":
        print("두 번째", end = "")
    elif select == "3":
        print("세 번째", end = "")
    elif select == "4":
        print("마지막", end = "")
    print(" 보스를 쓰러뜨리시겠습니까? (y/n)")
    while True:
        select_Y_or_N = input()
        if select_Y_or_N == "y" or select_Y_or_N == "Y":
            os.system("cls")
            ATTACK_POWER_COMPARE(select)
            break
        elif select_Y_or_N == "n" or select_Y_or_N == "N":
            print("메뉴로 돌아갑니다.")
            break
        else:
            print("잘못 입력하셨습니다.")



def ATTACK_POWER_COMPARE(select):
    global life
    global money
    global game2
    global game3
    global game4
    if ATTACK_POWER > Boss_power[int(select) - 1]:
        print("보스를 격파하였습니다!!")
        if select == "4": # 게임 승리 코드
            print("마지막 보스를 쓰려뜨렸습니다! 축하합니다!!!!")
            os.system("pause")
            exit(0)
        elif select == "1":
            print("첫 번째", end = "")
        elif select == "2":
            print("두 번째", end = "")
        elif select == "3":
            print("세 번째", end = "")
        print(" 보스를 쓰러뜨렸으므로 %d 한스를 드리겠습니다!\n" % Boss_attack_success_reward[int(select) - 1])
        money += Boss_attack_success_reward[int(select) - 1]
        if select == "1":
            print("두 번째", end = "")
            game2 = 1
        elif select == "2":
            print("세 번째", end = "")
            game3 = 1
        elif select == "3":
            print("네 번째", end = "")
            game4 = 1
        print(" 게임이 개방되었습니다!!")
    elif ATTACK_POWER == Boss_power[int(select) - 1]:
        print("보스와 공격력이 똑같으므로 비겼습니다. 메뉴로 돌아갑니다.")
        return
    elif ATTACK_POWER < Boss_power[int(select) - 1]:
        life -= 1
        if life >= 1:
            print("보스보다 공격력이 낮아 목숨이 하나 소멸되었습니다. 메뉴로 돌아갑니다.")
        print("현재 목숨 개수 : %d 개" % life)
        if life == 0: # 게임 오버 코드
            print("Game over!!!! 수고하셨습니다!!")
            os.system("pause")
            exit(0)
        return

################################## 게임 메뉴 출력 화면

money = 300000
life = 3



print("챙이네 게임에 오신 것을 진심으로 환영합니다!! ")
print("이 게임은 여러 가지 게임을 해서 한스(화폐단위)를 벌어 장비를 강화하여 보스를 이기면 승리하는 게임입니다.")
print("자세한 내용은 '게임 설명'을 참고하시길 바라고, 즐거운 게임 되시기 바랍니다! <enter키를 누르고 게임에 입장하세요>")

input()

while True:
    equipment_total_level = 0
    for i in range(6):
        equipment_total_level += level[i]
    ATTACK_POWER = 0
    for i in range(6):
        ATTACK_POWER += equipment_power[i]
    os.system("cls")
    print()
    print("\t1. 게임 설명")
    print("\t2. 게임 시작")
    print("\t3. 현재 장비 레벨 및 보유 금액")
    print("\t4. 장비 강화")
    print("\t5. 보스와 싸운다.")
    print("\t6. 게임을 종료한다.")
    print("\n메뉴를 선택하세요 : ", end ="")
    select = input()
    if select == "1":
        os.system("cls")
        game_explain()
    elif select == "2":
        game_in()
    elif select == "3":
        os.system("cls")
        CurrentState()
    elif select == "4":
        Reinforcement_in()
    elif select == "5":
        Boss_attack()
    elif select == "6":
        os.system("cls")
        while True:
            print("정말로 종료하시겠습니까? (y/n)")
            select = input()
            if select == "y" or select == "Y":
                print("게임을 종료합니다.")
                exit(0)
            elif select == "n" or select == "N":
                break
            else:
                print("잘못 입력하셨습니다.")
    else:
        print("잘못 입력하셨습니다.")
    os.system("pause")
