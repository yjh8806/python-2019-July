MonsterHp = 1000
turn = 0
while MonsterHp > 0: #조건식을 만족할때까지만 반복
    turn += 1
    print("[=====%d턴=====]"%turn)
    print("어떤 기술을 사용하겠습니까?")
    print("1 : 기본공격\n2 : 기술공격")
    skill = int(input("선택 : "))
    if skill == 1:
        print("몬스터에게 300의 데미지를 입혔습니다.")
        MonsterHp -= 300
    elif skill == 2:
        print("몬스터에게 500의 데미지를 입혔습니다.")
        MonsterHp -= 500
    else:
        print("잘못된 입력입니다.")
    print("몬스터의 체력 : %d\n"%MonsterHp)
print("몬스터가 죽었습니다.")
