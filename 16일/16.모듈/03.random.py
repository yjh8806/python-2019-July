import random as r
import time as t
import os

num1 = r.randint(2, 9)
num2 = r.randint(1, 9)
start = t.time()
calc = int(input("%d * %d = "%(num1,num2)))
end = t.time()
t.sleep(2) #뜸들이기
if calc == num1 * num2:
    if end - start < 2:
        print("천재")
    else:
        print("보통")
else:
    print("실망이야...")

doll = ["피카츄","라이츄","파이리","꼬북이"]
while doll: #0, "", [], (), {} 거짓말이 되죠
    input("""
    =====인형뽑기=====
    <Enter 누르면 게임 시작>
    """)
    print("**인형목록**")
    print(doll)
    crain = int(input("숫자 입력(1 ~ 3) : "))
    answer = r.randint(1, 3)
    if crain == answer:
        select = r.choice(doll)
        print("윙~")
        t.sleep(1)
        print("윙~")
        t.sleep(1)
        print("윙~")
        t.sleep(1)
        print("딸캉~")
        print("%s가 뽑혔습니다."%select)
        doll.remove(select)
    else:
        print("크레인 기계가 이상하게 움직여ㅜ")
    os.system("pause")
    os.system("cls")
print("☆☆인형을 모두 뽑았습니다.☆☆")
