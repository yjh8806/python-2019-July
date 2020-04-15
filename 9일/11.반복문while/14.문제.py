Battle = int(input("대결 횟수 : "))
count = 0
round = 1
while count < Battle:
    Ulist = [] #["Busan","Seoul","Ewha"]
    Dlist = [] #[100,400,300] => max(Dlist) => Dlist.index(400)
    uni_input = int(input("%s회차 비교 학교 수 : "%round))
    while uni_input > 0:
        name = input("대학이름 : ")
        drink = int(input("술 소비량 : "))
        Ulist.append(name)
        Dlist.append(drink)
        print("%s %s"%(name,drink))
        uni_input-=1
    Uindex = Dlist.index(max(Dlist)) #Dlist에서 가장 큰 숫자가 몇 번 인덱스에 있는지 저장
    print("%s회차 승리 : %s"%(round, Ulist[Uindex]))
    round += 1
    # del Dlist[:] #list의 내용물만 지워집니다.
    # del Ulist[:]
