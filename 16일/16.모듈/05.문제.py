import time as t
import random as r

def Quiz(w): #list를 w라는 이름으로 받아먹음
    answer = r.choice(w) #랜덤으로 한 단어 들고옴
    print(answer) #출력 => 이거보고 맞춥니다.
    player = input()
    if player == answer:
        print("맞췄습니다.(+1점)")
        return 1
    else:
        print("틀렸습니다.(+0점)")
        return 0

wordlist = ["apple","current","cake","blend","chat","game","python"]
score = 0
input("게임을 시작하려면 Enter키를 누르세요")
start = t.time()
while score<5:
    print("="*10)
    score += Quiz(wordlist)
    print("점수 = %d"%score)
