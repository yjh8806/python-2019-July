#서바이벌퀴즈게임
#처음 100명이서 같이 퀴즈 시작->단계별로 몇명씩 죽었는지 알려주는 게임
#만약 틀리면 게임오버
#만약 게임 다 맞추면 상금부여(1억)
import random as r
class Quiz: #클래스 선언
    def __init__(self):
        self.quiz_list1 = {"2006년 팬택 SKY 휴대폰 CF에 출연한 배우 박기웅이 추었던 춤으로, 거북이 처럼 목을 뺀 뒤 빙빙 돌리는 이 춤의 이름은":"맷돌춤",
"조선 중기에 지었다고 하는 고전소설인 '홍길동전'의 저자는":"허균",
"이탈리아의 물리학자 및 천문학자. '그래도 지구는 돈다' 라는 명언을 남긴 이 인물은":"갈릴레오 갈릴레이",
"곤충의 몸통은 세 가지의 부분으로 나뉩니다. 이 세가지의 기준은":"머리 가슴 배",
"조선시대 서울에 설치했던 최고의 교육기관":"성균관",
"프랑스어로 '이미 보았다' 라는 의미로, 처음 가본 곳인데 전에 와본 느낌이 드는 현상":"데자뷰",
"정식 명칭은 중앙공안정보기관. 1951년 총리 직속기관으로 설립된 이스라엘의 비밀정보기관은":"모사드",
"밀가루 반죽에 잘게 썬 문어를 넣고 구운 일본 간식으로, 가쓰오부시와 소스를 함께 뿌려 먹는 이 음식은":"타코야키",
"우리나라가 일제에게 나라를 빼앗긴 1910년부터 해방된 1945년까지의 민족 수난기는 무엇인가":"일제강점기",
"태극기의 4괘중 <물>을 상징하는것은":"감"}
#일반 상식 퀴즈 리스트 : 키값에 문제넣고 밸류값에 답 넣음
        self.quiz_list2 = {"5 + 3 = 28\n9 + 1 = 810\n8 + 6 = 214\n5 + 4 = 19\n7 + 3 = ?":"410",
        "이 연속체에서 빠진 문자는 무엇인가\nB C D E I K O X":"H"}
#최종 3인 이하일때 출제 할 최종 문제 리스트: 키값에 문제넣고 밸류값에 답 넣음
    def quiz(self):# 퀴즈 함수 선언
        d = 100     #초기값: 100명 설정
        print("""☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆서바이벌 게임을 시작합니다☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆\n
        <Enter> 를 누르면 게임 시작>>>""")
        print(input())

        while True: #반복문
            a = r.choice(list(self.quiz_list1.keys())) #랜덤으로 뽑아올 문제
            a1 = r.choice(list(self.quiz_list2.keys())) #랜덤으로 뽑아올 최종문제
            b = self.quiz_list1[a] #랜덤으로 뽑은 문제의 답
            b1 = self.quiz_list2[a1] #랜덤으로 뽑은 최종문제의 답
            del self.quiz_list1[a] #나온 문제는 리스트에서  문제 삭제
            print(a)
            c = input(">>>") #답 적는 곳
            e = r.randint(1,(d*2)//3) # 생존자 (1로 했을때 문제가 넘 빨리 끝나서 D //3으로 함)
            d -= e
            if b == c: #만약 문제의 답과 내가 적은 답이 일치했을때
                print("정답입니다")
                print("남은 생존자는 %d명 입니다"%d)
                count = 0
                for i in range(d): #100명을  i에 넣겠다
                    count += 1
                    print("●",end=" ") #검은 동그라미가 생존자 수
                    if count % 10 ==0: # 동그라미를 10개씩 정렬하겠다
                        print("\n")
                for i in range(100-d):
                    count += 1
                    print("○",end=" ") #흰색 동그라미가 죽은 사람 수
                    if count % 10 ==0:
                        print("\n")

            elif b != c: #내가 적은 답이 틀렸을때
                print("""오답입니다\n
                최종 탈락!!!!""")
                break

            if d <=3: #생존자 수가 3명이하일때 최종문제를 낸다
                print("최종문제입니다")
                print(a1) #최종문제 출력
                c1 = input(">>>")
                if b1 == c1: #최종문제 맞췄을때
                    print("☆☆☆☆☆☆☆☆최종 승자가 됬음으로 상금 1억원을 드립니다☆☆☆☆☆")
                    break
                else: #최종문제 틀렸을때
                    print("☆☆☆☆☆☆☆☆아깝게 탈락하셨습니다☆☆☆☆☆☆☆☆")
                    break

a = Quiz()
a.quiz()
