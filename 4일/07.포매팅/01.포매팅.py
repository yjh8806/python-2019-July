#c언어의 서식문자
a = "현재 통장의 잔고는 %d억원 입니다."
print(a%17)
print(a%100)
print(a%23)

#%d : 정수(decimal)
print("I eat %d cakes"%3)
#%s : 문자열(string)
print("I eat %s cakes"%"two")
#%f : 실수(float) : 소수점 6자리까지 표시
#%.2f : 소수점 2자리까지 출력
print("I eat %.2f cakes"%3.5)

#%s => 모든 데이터 타입을 다 받아먹어요
print("I eat %s cakes"%3)
print("I eat %s cakes"%3.5)
