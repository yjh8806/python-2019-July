import random
import os
r_c_p = ["가위","바위","보"]
input("""
=====가위 바위 보=====
<Enter 누르면 게임시작>
""")
player_score =0
computer_score =0
while player_score < 3 and computer_score < 3: #둘 다 3보다 작을때만 반복할거야!
    computer = random.choice(r_c_p)
    player = input("[가위, 바위, 보] : ")
    if player not in r_c_p:
        print("잘못된 입력입니다.")
    else:
        if player == computer:
            print("비겼습니다.")
        elif (player == "가위" and computer == "바위") or (player == "바위" and computer == "보") or (player == "보" and computer == "가위"):
            print("내가 졌어ㅜㅜ")
            computer_score += 1
        else:
            print("내가 이겼어!!")
            player_score += 1
        print("player : %d, computer : %d"%(player_score,computer_score))
        os.system("pause")
        os.system("cls")
if player_score == 3:
    print("☆내가 이겼어☆")
else:
    print("내가 졌어ㅜㅜ")
