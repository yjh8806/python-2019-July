import random

lotto = [] #내가 적을 로또 번호
lotto_answer = [] #정답 로또 번호
#1.lotto리스트에 1 ~ 45의 숫자 중 6개를 입력(중복되지 않은 6개)
#2.lotto_answer리스트에 1 ~ 45의 숫자 중 랜덤한 6개를 저장(중복되지 않은 6개)
#3.내가 몇개를 맞췄는지 출력
count = 1
while len(lotto) < 6:
    lotto_num = int(input("%d번째 숫자 입력 : "%count))
    if lotto_num >= 1 and lotto_num <= 45 and lotto_num not in lotto:
        lotto.append(lotto_num)
        count += 1
print(lotto)

while len(lotto_answer) < 6:
    num = random.randint(1,45)
    if num not in lotto_answer:
        lotto_answer.append(num)
lotto_answer.sort()
print(lotto_answer)

count = 0
for i in lotto_answer:
    if i in lotto:
        count += 1

count = 0
for i in lotto_answer:
    for j in lotto:
        if i == j:
            count += 1
print("%d개 맞췄습니다."%count)
