import random as r
import time as t
import os

class Team:
    attack = 0
    defense = 0
    chem = 0
    def __init__(self,attack,defense,chem):
        self.attack = attack
        self.defense = defense
        self.chem = chem

class Manchester_United(Team):
    pass
class Chelsea(Team):
    pass
class Liverpool(Team):
    pass
class Arsenal(Team):
    pass
class Real_Madrid(Team):
    pass
class Barcelona(Team):
    pass
class Munich(Team):
    pass
class AC_Milan(Team):
    pass
class AS_Roma(Team):
    pass
class Tottenham(Team):
    pass
class Inter_Milan(Team):
    pass
class Juventus(Team):
    pass
class NewCastle(Team):
    pass
class Atletico_Madrid(Team):
    pass
class Aston_Villa(Team):
    pass
class Amiens(Team):
    pass
class Dijon(Team):
    pass
class Alaves(Team):
    pass
class Celta_Vigo(Team):
    pass
class Eibar(Team):
    pass
class Borussia_Dortmund(Team):
    pass
class Hamburger(Team):
    pass
class Hertha(Team):
    pass
class Bayer_Leverkusen(Team):
    pass
class Hannover(Team):
    pass
class Chievo(Team):
    pass
class Empoli(Team):
    pass
class Genoa(Team):
    pass
class Napoli(Team):
    pass
class Torino(Team):
    pass


Manchester_United = Manchester_United(87,83,84)
Chelsea = Chelsea(85,74,86)
Liverpool = Liverpool(82,69,86)
Arsenal = Arsenal(75,76,84)
Tottenham = Tottenham(75,76,86)
NewCastle = NewCastle(75,76,77)
Aston_Villa = Aston_Villa(75,77,79)
Real_Madrid = Real_Madrid(93,83,84)
Barcelona = Barcelona(91,81,84)
Atletico_Madrid = Atletico_Madrid(69,70,71)
Amiens = Amiens(56,53,57)
Dijon = Dijon(75,75,72)
Alaves = Alaves(61,62,63)
Celta_Vigo = Celta_Vigo(59,61,62) #Naming convention
Eibar = Eibar(52,53,59)
Munich = Munich(74,86,84)
Borussia_Dortmund = Borussia_Dortmund(70,72,76)
Hamburger = Hamburger(53,59,59)
Hertha = Hertha(57,58,51)
Bayer_Leverkusen = Bayer_Leverkusen(61,65,66)
Hannover = Hannover(62,63,69)
AC_Milan = AC_Milan(73,72,65)
AS_Roma = AS_Roma(72,84,86)
Inter_Milan = Inter_Milan(75,83,75)
Juventus = Juventus(82,83,84)
Chievo = Chievo(52,57,58)
Empoli = Empoli(58,56,59)
Genoa = Genoa(51,52,59)
Napoli = Napoli(81,83,86)
Torino = Torino(61,62,67)

Attack_stat1 = {"Manchester_United":87,"Chelsea":85, "Liverpool":82,"Arsenal":75,"Tottenham":75,"NewCastle":75, "Aston_Villa":75,"Real_Madrid":93,"Barcelona":91, "Atletico_Madrid":69}
Attack_stat2 = {"Amiens":56,"Dijon":75, "Alaves":61,"Celta_Vigo":59,"Eibar":52,"Munich":74, "Borussia_Dortmund":70,"Hamburger":53,"Hertha":57, "Bayer_Leverkusen":61}
Attack_stat3 = {"Hannover":62,"AC_Milan":73, "AS_Roma":72,"Inter_Milan":75,"Juventus":82,"Chievo":52, "Empoli":58,"Genoa":51,"Napoli":81, "Torino":61}
Attack_stat1.update(Attack_stat2)
Attack_stat1.update(Attack_stat3)
Total_attack_stat = Attack_stat1

Defense_stat1 = {"Manchester_United":83,"Chelsea":74, "Liverpool":69,"Arsenal":76,"Tottenham":76,"NewCastle":76, "Aston_Villa":77,"Real_Madrid":83,"Barcelona":81, "Atletico_Madrid":70}
Defense_stat2 = {"Amiens":53,"Dijon":75, "Alaves":62,"Celta_Vigo":61,"Eibar":53,"Munich":86, "Borussia_Dortmund":72,"Hamburger":59,"Hertha":58, "Bayer_Leverkusen":65}
Defense_stat3 = {"Hannover":63,"AC_Milan":72, "AS_Roma":84,"Inter_Milan":83,"Juventus":83,"Chievo":57, "Empoli":56,"Genoa":52,"Napoli":83, "Torino":62}
Defense_stat1.update(Defense_stat2)
Defense_stat1.update(Defense_stat3)
Total_defense_stat = Defense_stat1

Chem_stat1 = {"Manchester_United":84,"Chelsea":86, "Liverpool":86,"Arsenal":84,"Tottenham":86,"NewCastle":77, "Aston_Villa":79,"Real_Madrid":84,"Barcelona":84, "Atletico_Madrid":71}
Chem_stat2 = {"Amiens":57,"Dijon":72, "Alaves":63,"Celta_Vigo":62,"Eibar":59,"Munich":84, "Borussia_Dortmund":76,"Hamburger":59,"Hertha":51, "Bayer_Leverkusen":66}
Chem_stat3 = {"Hannover":69,"AC_Milan":65, "AS_Roma":86,"Inter_Milan":75,"Juventus":84,"Chievo":58, "Empoli":59,"Genoa":59,"Napoli":86, "Torino":67}
Chem_stat1.update(Chem_stat2)
Chem_stat1.update(Chem_stat3)
Total_chem_stat = Chem_stat1

Team_list = ["Manchester_United","Chelsea","Liverpool","Arsenal","Real_Madrid","Barcelona","Munich","AC_Milan","AS_Roma","Tottenham","Inter_Milan","Juventus","NewCastle","Atletico_Madrid","Aston_Villa",]
Extra_list = ["Torino","Napoli","Genoa","Empoli","Chievo","Hannover","Bayer_Leverkusen","Borussia_Dortmund","Eibar","Celta_Vigo","Alaves","Dijon","Amiens","Hertha","Hamburger"]
Team_list += Extra_list
Match_list = []

i = 0
while i < 15:
    line = []
    choice_1 = r.choice(Team_list)
    line.append(choice_1)
    Team_list.remove(choice_1)
    choice_2 = r.choice(Team_list)
    line.append(choice_2)
    Team_list.remove(choice_2)
    Match_list.append(line)
    i += 1

Total_rounds = len(Match_list)
Start = 0                               #필요한가?
Margin_account = 0
Initial_margin = 0
Margin_call = 1000

# Team1 = "MU"
# Team2 = "MC"
# Team_list = [["MU","MC"],["TOT","CHELSEA"]]

Welcome = input("""
안녕하십니까 2018/19시즌 유러피언 축구 대항전이 시작되었습니다.
올해 처음 시행되는 리그인 만큼 세계 유명 클럽들이 한 자리에 모였습니다.
2018/19 클럽대항전 스케줄을 확인하시려면 아무키나 눌러주세요.
""")

for i in range (1,Total_rounds+1):
    print("\n=========================================")
    print("          {0}일차".format(i))
    print('────────────────────────────────────────')
    print('          {0}    '.format(Match_list[i-1][0]))
    print('           vs    ')
    print('          {0}    '.format(Match_list[i-1][1]))
    print('========================================')
os.system("pause")
os.system("cls")
while True:
    Initial_margin = int(input("시작하시기전 본인 계좌에 넣을 금액($)을 정해주세요: "))# #Initial_margin, Maintenance_margin, Margin_call
    if Initial_margin <= 0:
        print("넣을 금액은 0보다 커야합니다.")
        os.system("pause")
        os.system("cls")
        continue
    else:
        break
os.system("cls")

i = 1
while i < (Total_rounds+1):
    print("{0}일차 오늘의 경기는 {1} vs. {2}입니다.".format(i,Match_list[i-1][0], Match_list[i-1][1]))
    Bet_team = input("{0}팀에 배팅시 1을 눌러주세요. {1}팀을 선택할 경우 2를 눌러주세요. 마지막으로 비길것같은 경우에는 3을 눌러주세요: ".format(Match_list[i-1][0], Match_list[i-1][1]))

    if Bet_team != "1" and Bet_team != "2" and Bet_team != "3":
        continue

    elif Bet_team == "1":
        My_team = Match_list[i-1][0]
        Opponent_team = Match_list[i-1][1]
        Bet_goal = int(input("몇 골차이로 승리 할것 같은지 맞혀주십시오 (1~5골차이까지): "))
        Bet_amount = int(input("배당액($)을 입력해주세요 (배당율: 승리팀&점수차이 맞출시 2배율, Only 승리팀만 맞출시 1.5배율, 틀릴경우 0배율, 배팅 하지 않으실 경우 0을 눌러주세요.): "))
        print("{0}팀에 {1}골 승리에 ${2}만큼 배팅하셨습니다.\n".format(My_team,Bet_goal,Bet_amount))

#금액이 모자랄시 혹은 잘못된 입력을 할 경우 에 처음으로 돌아가는 방법?

    elif Bet_team == "2":
        My_team = Match_list[i-1][1]
        Opponent_team = Match_list[i-1][0]
        Bet_goal = int(input("몇 골차이로 승리 할것 같은지 맞혀주십시오 (1~5골차이까지): "))
        Bet_amount = int(input("배당액($)을 입력해주세요 (배당율: 승리팀&점수차이 맞출시 2배율, Only 승리팀만 맞출시 1.5배율, 틀릴경우 0배율, 배팅 하지 않으실 경우 0을 눌러주세요.): "))
        print("{0}팀에 {1}골 승리에 ${2}만큼 배팅하셨습니다.\n".format(My_team,Bet_goal,Bet_amount))

    elif Bet_team == "3":
        Bet_goal = 0
        My_team = Match_list[i-1][1]
        Opponent_team = Match_list[i-1][0]
        Bet_amount = int(input("배당액($)을 입력해주세요 (배당율: 승리팀&점수차이 맞출시 2배율, Only 승리팀 혹은 무승부 결과만 맞출시 1.5배율, 틀릴경우 0배율, 배팅 하지 않으실 경우 0을 눌러주세요.): "))
        print("{0}팀과 {1}팀의 무승부 결과에 {2}만큼 배팅하셨습니다.\n".format(Match_list[i-1][0], Match_list[i-1][1],Bet_amount))

    if Bet_amount > Initial_margin:
        print("잘못된 금액입니다. (배당액이 계좌잔고보다 클수가 없습니다. 현재 계좌 잔고 {0})".format(Initial_margin))
        os.system("pause")
        os.system("cls")
        continue

    My_team_stat = (Total_attack_stat[My_team]+Total_defense_stat[My_team]+Total_chem_stat[My_team])/4
    Opponent_team_stat = (Total_attack_stat[Opponent_team]+Total_defense_stat[Opponent_team]+Total_chem_stat[Opponent_team])/4

    My_team_luck = r.randint(1,30)
    Opponent_team_luck = r.randint(1,30)

    My_team_result = My_team_stat + My_team_luck
    Opponent_team_result = Opponent_team_stat + Opponent_team_luck

    if My_team_result == Opponent_team_result:
        My_team_score = r.randint(0,3)
        Opponent_team_score = r.randint(0,3)

    elif My_team_result > Opponent_team_result:
        My_team_score = r.randint(1,5)
        Opponent_team_score = r.randint(0,3)

    elif My_team_result < Opponent_team_result:
        My_team_score = r.randint(0,3)
        Opponent_team_score = r.randint(1,5)

    print("90분 치열한 경기 완료되었습니다. 최종스코어를 발표드리겠습니다.")
    t.sleep(2)
    print("\n {0} ({1}) vs {2} ({3}) \n".format(My_team, My_team_score, Opponent_team, Opponent_team_score))
    os.system("pause")


    if My_team_score > Opponent_team_score:
        Winning_team = My_team
        Winning_amount = Bet_amount*1.5
        Initial_margin += Winning_amount
        print("축하드립니다. 선택하신 {0}이 이겼습니다. ${1}를 얻고 현재 계좌 잔고 ${2}입니다.".format(Winning_team, Winning_amount, Initial_margin))
        os.system("pause")
        os.system("cls")

        if My_team_score - Opponent_team_score == Bet_goal:
            Winning_amount = Bet_amount*2
            Initial_margin += Winning_amount
            print("축하드립니다. 선택하신 팀이 {0}골 차이로 이겼습니다. ${1}를 얻고 현재 계좌 잔고 ${2}입니다.".format(Bet_goal, Winning_amount, Initial_margin))
            os.system("pause")
            os.system("cls")

    elif My_team_score < Opponent_team_score:
        Winning_team = Opponent_team
        Winning_team_score = Opponent_team_score - My_team_score
        Initial_margin -= Bet_amount
        print("안타깝지만 상대팀인 {0}이 {1}골 차이로 이겼습니다. 현재 계좌 잔고 ${2}입니다.".format(Winning_team, Winning_team_score, Initial_margin))
        os.system("pause")
        os.system("cls")

    elif My_team_score == Opponent_team_score:
        print("{0}과 {1}의 경기 결과 {2}:{3}으로 무승부입니다.".format(Match_list[i-1][0], Match_list[i-1][1], My_team_score, Opponent_team_score))
        if Bet_team == "3":
            Winning_amount = Bet_amount*1.5
            Initial_margin += Winning_amount
            print("축하드립니다. 선택하신 무승부 승부로 ${0}을 얻고 현재 계좌 잔고 ${1}입니다.".format(Winning_amount, Initial_margin))
            os.system("pause")
            os.system("cls")
        else:
            Initial_margin -= Bet_amount
            print("현재 계좌 잔고 ${0}입니다.".format(Initial_margin))
            os.system("pause")
            os.system("cls")



    i += 1
