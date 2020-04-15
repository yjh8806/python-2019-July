import time as t

correct1 = "내가 그린 목이긴 기린그림은 잘 그린 기린그림이고"
correct2 = "니가 그린 그린기린그림은 못 그린 기린그림이다"

input("""
문장을 따라 적으시오
<Enter를 누를 시 게임 시작>
""")
start = t.time() #시작시간 저장

while True:
    print(correct1)
    answer1 = input()
    if correct1 == answer1:
        break
    else:
        print("틀렸습니다.\n")

while True:
    print(correct2)
    answer2 = input()
    if correct2 == answer2:
        break
    else:
        print("틀렸습니다.\n")

end = t.time() #끝나는 시간 저장
result = end - start

print("소요시간 : %.2f"%result)
