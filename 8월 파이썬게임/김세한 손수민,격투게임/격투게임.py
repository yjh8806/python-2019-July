#이 게임은 격투게임으로 게임에 입장하여 보스몬스터들을 5명정도 토너먼트식으로해서 싸워 이기는 게임입니다.
import random as r
import time
import sys
import os
class Unit:
    #유닛은 이름, 체력, 공격력
    def __init__(self, name):
        self.name = name
        self.life = r.randint(50,60)
        self.dmg = r.randint(3,10)

class Player(Unit):
    def __init__(self, name): #오버라이딩
        self.name = name
        self.life = r.randint(50,60)
        self.str = r.randint(10,20)
        self.ap = r.randint(1,10) # #ability point(기술): 더 강한 공격을 쓸 때 사용하는 스텟
        self.dice20 = r.randint(1,20)
        self.attack_bonus = r.randint(1,10)
        self.dc = 1*self.dice20 + self.attack_bonus
        self.dmg = r.randint(3,10)
        self.dc = 1*self.dice20 + self.attack_bonus
    def ability(self,Unit):
        dmg = self.dmg*2
        Unit.life -= dmg
        self.ap -= 10
        print("""
1.[어퍼컷] : 상대방의 얼굴을 가격한다.
2.[날라차기] : 힘껏 몸을 날려 몸을 가격한다.
3.[로우킥] : 두번 돌아서 상대방 다리를 가격한다.""")

        if choice ==  1:
            print("어퍼컷 데미지가 들어갔습니다.")
        elif choice == 2:
            print("날라차기가 들어갔습니다.")
        elif choice == 3:
            print("로우킥이 들어갔습니다.")
        else:
            print("공격이 안들어갔습니다.")
def battle_system():

                    choice = int(input("\n숫자로 선택해주세요: "))
                    player.show()
                    monster.show()
                    print("""\n
                        1. 공격
                        2. 기술
                    3. 도망""")

                    if  choice == 1:
                        player.attack(monster)
                        print("\n▶%s의 생명력 %s입니다, "% (monster.name, monster.life))
                    elif monster.life < 0: # 중간에 몬스터 체력이 0이되면 루프를 종결시킵니다.
                        time.sleep(2)
                        print("\n▶상대의 턴 입니다.")
                        tme.sleep(2)
                        monster.attack(player)
                        print("\n▶%s의 생명력 %.2f입니다, "% (player.name,player.life))

                    elif choice == 2:
                        player.ability(monster)

                    elif choice == 3:
                        print("\n당신은 도망갔습니다.")
                    else:
                        print("\n잘못된 입력입니다.")
                        s.system("pause")
                        os.system("cls")

                    if player.life < 0 : # 체력 0 이하가 되면 게임은 종료가 되고 메인화면으로 다시 돌아갑니다.
                        print("당신은 싸늘한 시체가 되었습니다.")
                        time.sleep(1)
                        print("파리가 당신에게 속삭입니다.")
                        time.sleep(1)
                        print("유다희")
                        main() #메인화면 호출
class Enemy(Unit):
    def __init__(self, name, life, num):
        self.num = num
        self.name = name
        self.life = life
        self.life = r.randint(50,60)
        self.dmg = r.randint(3,10)
    def ability(self,Unit):
        if dmg == self.dmg*2:
            Unit.life -= dmg
            print("""
            1.[기본공격] : 보스몬스터가 당신을(를) 기본공격합니다.
            """)
        elif ability(self,Unit):
            print("펑 펑\n %s가 당신을 공격하였습니다."%self.name)
            time.sleep(1)
        else:
            print("%s의 공격이 허공을 가릅니다."%self.name)
            time.sleep(1)
            print("%s는 회피하였습니다."%Unit.name)
            time.sleep(1)

monster_list = [Enemy("보스1",80,1),Enemy("보스2",130,2),Enemy("보스3",150,3),Enemy("보스4", 180,3),Enemy("라스트 보스", 200, 4)]
num = 0
def main():
    os.system("cls")
    print("""격투게임에 들어오신 거 환영합니다.
    1. 시작
    2. 종료""")
    choice = int(input("숫자로 선택해주세요: "))
    if choice ==1:
        print("게임을 시작합니다.")
        start()
    elif choice ==2:
        print("게임을 종료합니다.")
        sys.exit(0)
    else:
        print("잘못된 입력입니다.")
        main()

def start(): #캐릭터 생성
        os.system("cls")
        print("당신의 캐릭터를 만들어주세요.")
        name = input("이름을 입력해주세요 : ")

        global player
        player = Player(name)
        print("""
        [이 름] : %s
        [생명력] : %s
        [ 힘  ] : %s
        """ %(player.name, player.life, player.str))
        print("""
        1. 그대로 게임을 진행한다.
        2. 다시 캐릭터를 생성한다.
        3. 처음시작메뉴로 돌아간다.""")
        choice = int(input("\n숫자로 선택해주세요: "))


        if choice == 1:
            print("게임을 시작하겠습니다..")
            os.system("cls")
            battle_system()
        elif choice ==3:
            os.system("cls")
            main()
        else:
            print("잘못된 입력입니다.")
            os
def battle_system():
        global num
        os.system("cls")
        print("""당신은 보스몬스터와 대결을하게됩니다.
    호흡을 가다듬으시고 이제 격투게임을 시작하겠습니다.
    1.공격한다.
    2.기술을 쓴다.
    3.게임을 종료한다.
    """)
        choice = int(input(">> "))
        if choice == 1:
            print("당신은 %s를 공격합니다."%monster_list[num].name)
            num += 1
            ability()
        elif choice ==2:
            ability(Player)
        elif choice ==3:
            print("종료한다.")
            sys.exit(0)

main()




    # def end(): 엔딩화면
    # time.sleep(1)
    # print("축하합니다.")
    # time.sleep(2)
# Unit 보스몬스터(이름,LIFE,str, )

#보스1~5몬스터까지 차례대로 공격해서 게임을 클리어하는 방식이였으나...코드들이 뒤엉키고 엉켜버려서 여기까지만 하도록하겠습니다.
