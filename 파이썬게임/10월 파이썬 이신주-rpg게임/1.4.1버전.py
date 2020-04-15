

#안녕하세요/
# 이 게임의 목표는 던전으로 들어가 최종 보물방으로 들어가는 것입니다.
# 이 게임은 d&d의 기초 시스템 중 ac/dc 개념을 차용했습니다.
# ac는 armor class를 말하고,
# dc는 damage class를 말합니다.
# 각 값의 우위에 따라 공격의 ★성공률★이 결정합니다.
#예를 들어 ac가 10이고 dc가 12이면
# dc가 더 높으므로 공격이 성공합니다.
#그리고 데미지는 캐릭터의 힘 스텟 과 가지고 있는 아이템의 공격 속성에 따라 데미지 값이 결정됩니다.
#그런데 아이템 시스템은 제가 구현하지 않았습니다. 본래 게임을 만드려는 취지를 고려하였고, 구현하려고 하니 코딩이 자꾸 길어지고 시스템 추가할때마다 버그터지고 ○○나서 전투시스템만 구현했습니다.


#모듈 구간

import random as r
import os
import time
import sys

class Unit: #class Unit 선언했습니다. 플레이어와 몬스터들의 기본 틀이 되어줄 것입니다.

    def __init__(self, name, life, ap, str, dex, con):
        #초기값 stat
        self.name = name
        self.life = life #체력
        self.ap = ap #ability point(기술): 더 강한 공격을 쓸 때 사용하는 스텟
        self.str = str #strenth(힘): 데미지에 영향
        self.dex = dex #dexterity(민첩):  공격 성공률(ac/dc)에 영향
        self.con = con #constitution은 마법내성을 결정함. 하지만 마법이 없어서 그냥 잉여스텟이 되버림.
        self.dmg = r.randint(3,10)#기본데미지

        #초기값 damage class
        self.dice20 = r.randint(1,20) # d&d게임은 주사위 중심으로 시스템이 돌아갑니다. 주사위 2개가 될 수 있고 최대 3개까지 할 수 있습니다. 또한 주사위 눈도 굳이 1부터 시작할 필요는 없습니다. 지금은 주사위 1개만 구현했습니다.
        self.attack_bonus = r.randint(1,10) #attack_bonus는 캐릭터가 장착한 무기 속성에 따라 결정되지만 지금은 아이템을 구현하지 못했으므로 기본속성으로 설정했습니다.
        self.dc = 1*self.dice20 + self.attack_bonus + self.dex  # 사실 주사위가 1개고 아이템도 없어서 코딩 1줄로 만들어도 상관없으나 나중에 아이템을 구현하고 더 많은 시스템을 구축할 때를 대비하기위해 일부러 3줄로 만들었습니다.

        #초기값 amor class
        self.armor_bonus = r.randint(1,3) # 캐릭터가 장착한 방어구 속성에 따라 결정되지만 지금은 기본속성으로 만족하는 걸로...
        self.shield_bonus = r.randint(1,3)
        self.ac = 10 + self.armor_bonus + self.shield_bonus + self.dex


    def attack(self,Unit):

        print("\n%s 공격하였습니다."%self.name)

        print("\n휫!")
        time.sleep(1)
        print("\n휫!")
        time.sleep(1)

        print("\n▶%s의 공격력은 %.2f 입니다."% (self.name,self.dc))#dc 정보를 플레이어가 알 수 있도록 구현.
        print("\n▶%s의 방어력은 %.2f 입니다."% (Unit.name,Unit.ac))#ac 정보를 플레이어가 알 수 있도록 구현.
        time.sleep(1)

        if self.dc >= Unit.ac:  #나의 공격력(dc:damage class)과 상대방의 방어력(ac:armor class)의 우위에 따라 공격  성공이 정해집니다.

            print("\n%s의 공격이 성공했다!!!!!!"% self.name)

            print("\n 피 향기가 진동합니다.")
            time.sleep(1)
            print("\n 상처는 늘어나고 벌레가 마음을 먹습니다.")
            time.sleep(1)

            if self.dice20 == 20: # 공격이 성공하면 그 다음으로 데미지 값이 결정됩니다. 데미지 값은 주사위 값 (1~20)으로 결정됩니다.
                fatal_dmg = self.dmg + 20 # 치명타 : 주사위가 1에서 20까지 있는데 만약 20이 나오면 치명타가 나와 더 많은 데미지를 결정하는걸로 구현
                Unit.life -= fatal_dmg
                print("\n치명타!!!!!!!!!!!!!")
                time.sleep(1)
                print("\n죽음의 신이 당신을 바라봅니다.")
                time.sleep(1)
                print("\n▶%s의 데미지는 %.2f입니다."%(self.name, fatal_dmg))
                time.sleep(1)


            elif self.dice20 >16: #주사위 눈이 16보다 클 때 추가공격할 수 있도록 구현.
                serious_blow = self.dmg + 5
                Unit.life -= serious_blow
                print("\n추가공격!!!!!!!")
                time.sleep(1)
                print("\n웅~")
                time.sleep(1)
                print("\n웅~")
                print("\n▶%s의 데미지는 %.2f입니다."%(self.name, serious_blow))
                time.sleep(1)

            else: #일반공격
                dmg = self.dmg + self.str*0.8
                Unit.life -= dmg
                print("\n▶%s의 데미지는 %.2f입니다."% (self.name,dmg))
                time.sleep(1)

        else: # 공격이 실패하면 상대는 아무런 데미지를 받지 못합니다.
            print("\n%s의 무기는 허무하게 허공을 가릅니다."% self.name)
            time.sleep(1)
            print("\n%s는 회피하였습니다."% Unit.name)
            time.sleep(1)

        #초기값들을 다시 초기화, 주사위 값들은 전투 라운드별로 계속 굴립니다.
        self.dmg = r.randint(3,10)

        self.dice20 = r.randint(1,20)
        self.attack_bonus = r.randint(1,10)
        self.dc = 1*self.dice20 + self.attack_bonus + self.dex


        self.amor_bonus = r.randint(1,3)
        self.shield_bonus = r.randint(1,3)
        self.ac = 10 + self.amor_bonus + self.shield_bonus + self.dex


    def show(self): #스텟창
        print("\n▶▶\n◈이름: %s\n◈생명: %.2f\n◈기술:%.2f\n◈힘: %.2f\n◈기본데미지: %.2f\n◈민첩: %.2f\n◈체력: %.2f\n"%(self.name, self.life, self.ap, self.str, self.dmg, self.dex, self.con))

    def show2(self): #괴물 등장신
        print("\n▷▷▷▷%s 가 모습을 드러냈다!!!!."% self.name)

class Player(Unit): # class Unit를 상속받아 class Player를 따로 만들어 ability를 구현했습니다. 주인공은 특수 기술을 장착해서 전투를 좀더 수월하게 할 수 있도록 만들었습니다.

    def ability(self,Unit):
        print("""
1.[이단베기]: 2번 휘둘러 2배 데미지를 입힌다.                                    [SP 소모]: 10
2.[척추가르기]: 상대의 척추를 노린다.                                            [SP 소모]: 20
3.[이름짓기귀찮아]: SP소모는 심하지만 효과는 크다. 단, 실패시 내상을 입는다.     [SP 소모]: 25
4. 뒤로 가기
""")
        choice = int(input("숫자로 선택해주세요: "))



        if choice == 1:

            if self.dc >= Unit.ac and self.ap>=10: #역시 마찬가지로 dc와 ac 우위에 따라 기술성공이 결정됩니다. 그리고 이 기술이 요구하는 sp 조건을 충족시켜야 합니다.
                dmg = self.dmg*2
                Unit.life -= dmg
                self.ap -= 10

                print("\n%s의 [이단베기]가 명중했다!!!!!!"% self.name)
                time.sleep(1)
                print("휙~~!")
                time.sleep(1)
                print("휙~~!")
                time.sleep(1)
                print("\n%.2f 데미지!!!"% dmg)
                time.sleep(1)

            elif self.ap <10: # 특수 기술은 기본공격보다 데미지가 크기 때문에 ability point를 만들어서 기술제한을 두었습니다.
                print("\n이 기술은 ap가 부족해서 쓸 수 없습니다.")
                player.ability(self.Unit)#

            else:
                print("\n%s의 [이단베기] 시도는 실패했습니다."%self.name)
                time.sleep(1)

        elif choice == 2:

            if self.dc >= Unit.ac and self.ap>=20:
                dmg = r.randint(20,25)
                Unit.life -= dmg
                self.ap -= 20

                print("\n%s의 [척추가르기]가 명중했다!!!!!!"% self.name)
                time.sleep(1)
                print("슥~~!")
                time.sleep(1)
                print("삭~~!")
                time.sleep(1)
                print("\n%.2f 데미지!!!"% dmg)
                time.sleep(1)

            elif self.ap <20:
                print("\n이 기술은 ap가 부족해서 쓸 수 없습니다.")

            else:
                print("\n%s의 [척추가르기] 시도는 실패했습니다."%self.name)
                time.sleep(1)

        elif choice == 3 :
            if self.dc >= Unit.ac and self.ap>=25:
                dmg = r.randint(40,50)
                Unit.life -= dmg
                self.ap -= 20

                print("\n%s의 [이름짓기귀찮아]가 명중했다!!!!!!"% self.name)
                time.sleep(1)
                print("!!!!!!!!!")
                time.sleep(1)
                print("!!!!!!!!!")
                time.sleep(1)
                print("\n%.2f 데미지!!!"% dmg)
                time.sleep(1)

            elif self.ap <25:
                print("\n이 기술은 ap가 부족해서 쓸 수 없습니다.")

            else: #3번째 기술 실패시 오히려 자신이 데미지 입는 것을 구현.
                dmg = r.randint(10,15)
                self.life -= dmg
                print("\n%s의 [이름짓기귀찮아]시도는 실패했습니다."%self.name)
                print("\n%s는 %.2f만큼 피를 토합니다."%(self.name, self.dmg))
                time.slep(1)

        elif choice == 4:
            battle_system()

        else:
            print("잘못된 입력입니다.")
            ability(self,Unit)

        print("\n▶%s의 생명력 %.2f입니다, "% (monster.name, monster.life))
        os.system("pause")
        os.system("cls")

def battle_system(): # 전투시스템 구현

    while monster.life > 0 and player.life >0 :
        player.show()
        monster.show()
        print("""\n
1. 공격
2. 기술
3. 도망""")


        choice = int(input("\n숫자로 선택해주세요: "))
        if choice == 1:

            player.attack(monster)
            print("\n▶%s의 생명력 %s입니다, "% (monster.name, monster.life))
            if monster.life < 0: # 중간에 몬스터 체력이 0이되면 루프를 종결시킵니다.
                break

            time.sleep(2)
            print("\n▶상대의 턴 입니다.")
            time.sleep(2)

            monster.attack(player)
            print("\n▶%s의 생명력 %.2f입니다, "% (player.name,player.life))

        elif choice == 2:
            player.ability(monster)

        elif choice == 3:
            print("\n당신은 도망갔습니다.")
        else:
            print("\n잘못된 입력입니다.")
        os.system("pause")
        os.system("cls")

    if player.life < 0 : # 체력 0 이하가 되면 게임은 종료가 되고 메인화면으로 다시 돌아갑니다.
        print("당신은 싸늘한 시체가 되었습니다.")
        time.sleep(1)
        print("파리가 당신에게 속삭입니다.")
        time.sleep(1)
        print("유다희")
        main() #메인화면 호출

    elif monster.life < 0 :
        print("당신은 승리하였습니다.")


def main(): #메인화면
    os.system("cls")
    print("""던전게임에 들어오신 거 환영합니다.
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

    name = input("이름을 입력해주세요: ")
    life = r.randint(80,100)
    sp   = r.randint(60,100) # skill point는 RPG에서 마나와 비슷한 개념입니다.
    str = r.randint(10,30) # strength(힘)은damage 값을 결정하는 요소입니다.
    dex = r.randint(10,30) # dexterity(민첩)은 damage class, amor class를 결정하는 요소입니다.
    con = r.randint(10,15) # constitution은 마법내성을 결정하는데 현재 제가 마법을 구현하지 않아서 필요없는 잉여스텟입니다.
    print("""
【이  름】: %s

【생명력】: %s

【기술력】: %s

【  힘  】: %s

【민첩성】: %s

【체  질】: %s
"""% (name, life, sp, str, dex, con,))

    global player
    player = Player(name, life, sp, str, dex, con)
    print("""
    1. 그대로 게임을 진행한다.
    2. 다시 캐릭터를 생성한다.
    3. 처음시작메뉴로 돌아간다.""")
    choice = int(input("\n숫자로 선택해주세요: "))

    if choice == 1:
        print("던전으로 들어갑니다.")
        front_dungeon()
    elif choice == 2:
        os.system("cls")
        start()
    elif choice ==3:
        os.system("cls")
        main()
    else:
        print("잘못된 입력입니다.")
        os
        main()

def front_dungeon(): #첫번째 던전 구현, 첫 입장이기 때문에 몬스터는 약합니다.
    os.system("cls")
    print("""던전 안은 어두운 묵빛과 햇불만이 당신의 시야에 들어옵니다.
조금 안으로 들어가니 어떤 생물의 형체가 보입니다.
1. 공격한다.
2. 던전 밖으로 도망간다.""")
    choice = int(input("\n숫자로 선택해주세요: "))
    if choice == 1:
        print("고블린의 악취와 누런 이빨이 당신을 위협합니다.")
        time.sleep(1)
        global monster # 지역함수를 뛰어넘기 위해서 global선언
        monster = Unit("고블린",50,1,5,5,5) # monster 객체 선언
        battle_system()

    elif choice ==2:
        print("당신은 공포심을 이겨내지 못했습니다.")
        time.sleep(1)
        main()
    else:
        print("잘못된 입력입니다.")
        time.sleep(1)
        front_dungeon()
    dungeon()


def dungeon(): #본격 던전시작 8라운드가 되면 엔딩을 볼 수 있게 구현
    os.system("cls")
    print(r.choice(sentence))
    count = 0
    while count < 8:

        print("""
    1.공격한다.
    2.던전 밖으로 도망간다.""")
        choice = int(input("\n숫자로 선택해주세요: "))
        if choice == 1:

            global monster  # 지역함수를 뛰어넘기 위해서 monster 변수를 global 선언
            monster = r.choice(monster_list) # 몬스터 출현을 랜덤화
            monster.show2() #랜덤 등장하는 몬스터 이름을 알려줌.

            time.sleep(1)
            print("!!")
            time.sleep(1)
            print("!!")
            time.sleep(1)

            battle_system()#전투시스템 호출

        elif choice ==2:
            print("실성한 사람처럼 소리를 지르며 밖으로 도망갑니다.")
            time.sleep(1)
            main()#메인화면 호출
        else:
            print("잘못된 입력입니다.")
            time.sleep(1)
            dungeon()#다시 처음으로 돌아감.
        count += 1
    end()#엔딩화면 호출

def end(): #엔딩화면
    time.sleep(1)
    print("당신은 무사히 던전 안에 있는 보물이 있는 방안에 도착했다.")
    time.sleep(1)
    print("하지만 다시 던전 밖으로...")
    time.sleep(1)
    print("괴물이 가득한 그곳으로 나가야 한다.")
    time.sleep(1)
    os.system("cls")
    print("END")
    time.sleep(2)
    main()#다시 첫 메인화면으로 돌아갑니다.

###저장 구간
#문구저장
sentence =["던전 안은 어두운 묵빛과 햇불만이 당신의 시야에 들어옵니다.조금 안으로 들어가니 어떤 생물의 형체가 보입니다.",
           "조금 앞으로 들어가니 악취가 코를 찌릅니다. 악취의 존재가 당신에게 다가옵니다.",
           "소름끼치는 소리가 당신의 등줄기를 타고 귓가에 울립니다. 위협을 느끼고 공격할 준비를 해야합니다.",
           "자그마한 휴식도 용납하지 않습니다.",
           "썩어가는 시체들이 보입니다. 괴물의 발톱이 불빛 속에서 번들거립니다."]

#몬스터 데이터 저장
#Unit(이름,life, ap, str, dex, con)
monster_list = [Unit("오크",80,1,25,10,10),Unit("드래곤",120,1,35,25,10),Unit("발록",85,1,15,35,10),Unit("장남 고블린",50,1,10,5,5,),Unit("차남 고블린",50,1,15,5,5),Unit("막내 고블린",30,1,5,15,5),Unit("장녀 고블린",30,1,10,15,5)]

#현금 구현하지 않음.
#money = 0

#아이템 데이터 저장/지금은 구현하지 않음.
#item = []

#경험치에 따른 레벨업 데이터 저장/지금은 구현하지 않음.
#Experience = []

#magic_list = []

#ability_list = []


###메인 코딩구간
main() # 코팅명령 첫 스타트입니다.



#player = Player("이신주",100,100,10,10,10)

#monster = Unit("괴물",100,1,5,5,5)

#battle_system()
