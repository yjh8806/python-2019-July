import os
import random as r
import time as t
ranklist=[]

f = open("D:\\rank.txt","r")
# print(ranklist)
while True:

    line = f.readline()

    if line:

        ranklist.append(int(line))

    else:

        break

f.close()

while True:
    menu = int(input( '''
    ▨▨▨▨▨ GenGa Game ▨▨▨▨▨
                        작성자 : 이수진 , 오서경

    1.게임 시작
    2.전적 보기
    3.종료
    어떻게 하시겠습니까? : '''))

    os.system('pause')
    os.system('cls')

    if menu == 1:
        usegenga = []#사용한 젠가 목록
        round= 1 ###게임 난이도 조절 재검토필요 작동안함
        play = 1#게임 진행 허락
        makecount=0
        tower =[]
        towertr=0
        a=10

        for i in range(18):#18층 총 54개의 젠가 배열
            tower.append([a+1,a+2,a+3])#1은 블록존재 0은 안존재 4는 폭탄
            a+=10########층수 구별 차후 지우기



        while play==1:
            stop=0##중복 입력 방지 용


            if round>0 and round<3:####라운드별 게임 난이도 조절
                makecount=r.randint(20,30)#폭탄개수1~10
                print('현재 난이도 : Easy')
            elif round<5:
                makecount=r.randint(25,35)#폭탄개수 5~15
                print('현재 난이도 : Nomal')

            elif round<7:
                makecount=r.randint(30,40)#폭탄개수 10~20
                print('현재 난이도 : Hard')
            elif round<10:
                makecount=r.randint(40,45)#폭탄개수 20~30
                print('현재 난이도 : Hell')

            bomb = []# 폭탄을 담을 리스트
            for i in range(makecount):#폭탄 랜덤 갯수
                bmaker = [r.randint(1,18),r.randint(0,2)]#폭탄 위치 지정
                bomb.append(bmaker)#폭탄추가 작업
            # for x, y in bomb:
            #     print('층수 %s 몇번째%s'%(x, y))
            # print('폭탄 배열 : %s'%bomb)#######폭탄이 지정된
            ##############폭탄생성 끝
            print('%d번째 도전입니다.'%(round))
            # pselect2=0
            #########################젠가 이미지 구현
            while True:
                print('▨▨▨▨젠가 게임▨▨▨▨▨\n')
                print('현재 시야 : 오른쪽 면 \n')
                for lblock,cblock,rblock in tower:#####홀수 층 이미지 구현
                    i=lblock//10# -1
                    if i%2==1 :### 홀수 층 0일때가 문제
                        lblock='【    】'
                        print(lblock)
                    else:
                        if lblock>0:
                            lblock=' ▩'
                        else :
                            lblock='   '
                        if cblock>0:
                            cblock='▩'
                        else :
                            cblock='  '
                        if rblock>0:
                            rblock='▩'
                        else :
                            rblock='   '
                        print(lblock,end='')
                        print(cblock,end='')
                        print(rblock)
                print('▨▨▨▨▨▨▨▨▨▨▨▨▨▨\n')
                print('1.다른면보기 2.젠가 뽑기')
                see = int(input('어떻게하시겠습니까? : '))
                os.system('pause')
                os.system('cls')

                if see ==1:
                    print('▨▨▨▨젠가 게임▨▨▨▨▨\n')
                    print('현재 시야 : 왼쪽 면 \n')

                    for lblock,cblock,rblock in tower:####짝수층 이미지 구현
                        i=lblock//10# -2
                        if i%2==0 and i !=0:### 짝수 층 0일때가 문제
                            lblock='【    】'
                            print(lblock)
                        else:
                            if lblock>0:
                                lblock=' ▩'
                            else :
                                lblock='   '
                            if cblock>0:
                                cblock='▩'
                            else :
                                cblock='  '
                            if rblock>0:
                                rblock='▩'
                            else :
                                rblock='   '
                            print(lblock,end='')
                            print(cblock,end='')
                            print(rblock)
                    print('▨▨▨▨▨▨▨▨▨▨▨▨▨▨\n')

                if see==2:
                    break

                elif see==1:
                    os.system('pause')
                    os.system('cls')
                    continue
                else:
                    print('잘못입력하셨습니다.')
                    continue


######################################################
            print('▨▨▨▨▨▨▨▨▨▨▨▨▨▨\n')
            print('현재 뽑은 젠가위치 ',end='')
            for x,y in usegenga:#usegenga안의 뽑았던 젠가 로그 데이터 글자화
                if y==0:
                    y='왼쪽'
                elif y==1:
                    y='중앙'
                elif y==2:
                    y='오른쪽'
                print('%d 층 %s , '%((x+1),y),end = '')
            print()
                # if x==pselect1 and y==pselect2:
####################################################################
            pselect1 = int(input('뽑을 층수를 입력해주세요. : '))#int#######중복잡기

            if pselect1>18 or pselect1<1:
                print('층수는 18층까지 존재합니다.다시 입력해주세요.\n')

                os.system('pause')
                os.system('cls')
                continue
            pselect1 =pselect1-1##0번쨰 배열을 1층으로 인식하기 위해
            pselect2str= input('왼쪽,중앙,오른쪽 블록 중 하나뽑아주세요. : ')#012를 왼쪽 중앙 오른쪽 입력으로 구분 하게 만들기

            if pselect2str=='왼쪽':
                pselect2=0
            elif pselect2str=='중앙':
                pselect2=1
            elif pselect2str=='오른쪽':
                pselect2=2
            else:
                print('왼쪽,중앙,오른쪽 중에 골라주세요.\n')

                os.system('pause')
                os.system('cls')
                continue
###########################중복 뽑기 방지 코드

            for x,y in usegenga:#usegenga안의 뽑았던 젠가 로그 데이터
                # print('usegenga for문 정상 작동')
                if x==pselect1 and y==pselect2: #현재 선택사항과 뽑았던 로그 데이터 검증
                    stop=1 #같을시 1부여
            if stop==1:#로그 데이터와 현재 선택 데이터가 같을시 while내에서 continue작동
                print('이미 사용한 블록입니다. 다른것을 뽑아주세요.\n')
                os.system('pause')
                os.system('cls')
                continue
########################
            print('%d층 %s 블록을 선택하셨습니다.\n'%((pselect1+1),pselect2str))
            # pselect1=-1
            # pselect2=-1
            ############################################타워 이미지 엉킹 문제 해결점
            if towertr==1:
                tower.reverse()#입력받은 배열 위치에 값을 부여하기 위해 뒤집는다.
            #############--------#############--------#############--------#############--------#############--------#############--------#############--------#############--------#############--------#############--------#############--------#############--------#############--------#############--------#############--------
            i2=tower[pselect1][pselect2]//10
            if i2%2==1 :### 홀수 층 0일때가 문제
                tower[pselect1][pselect2]=-1001# 홀수라인 폭탄
            elif i2%2==0:##짝수 일때
                tower[pselect1][pselect2]=-1000# 짝수라인 폭탄



            tower.reverse()#배열을 오름차순으로 출력하기 위해 뒤집어준다.
            towertr=1

            ##################################################사용한 젠가 데이터 기록
            selsave = [pselect1,pselect2]
            usegenga.append(selsave)

            ##########################
            for x,y in bomb:##폭탄 검증
                if x==pselect1 and y==pselect2:#게임패배 트리거
                    print('젠가탑이 흔들립니다.')
                    t.sleep(1)
                    print("흔들 흔들")
                    t.sleep(1)
                    print('와르르르 젠가가 무너집니다\n.')
                    print('Enter누르시면 메뉴로 돌아갑니다.')
                    os.system('pause')
                    os.system('cls')
                    play=-1
                    ranklist.append(round)

            if play ==1:
                print("젠가탑이 흔들립니다.")
                t.sleep(1)
                print("흔들~")
                t.sleep(1)
                print('블록을 무사히 뽑았습니다.')
                print('\n▨▨▨▨▨▨▨▨▨▨▨▨▨▨\n')
                round +=1
                os.system('pause')
                os.system('cls')


    elif menu == 2 :

        rankcount=0

        if ranklist == []:

            print("게임을 하고 와주세요")

        else:

            ranklist.sort()

            ranklist.reverse()
            print('▨▨▨▨▨▨ 젠가 랭킹 ▨▨▨▨▨▨')
            print()

            for i in ranklist:

                rankcount+=1

                print('%d등 : %d점 입니다.'%(rankcount,i))
            print()
            print('▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨')
            os.system('pause')
            os.system('cls')

    elif menu == 3 :
        # print(ranklist)


        f=open("D:\\rank.txt","w")
        for i in ranklist:

            data='%s\n'%i
            f.write(data)
        f.close()
        print("게임종료")
        exit(0)

    else:
        print('잘못입력하셨습니다.')
