#소수는 1과 자신으로만 나눠지는 수
num = int(input("숫자 입력 : "))
count = 0 #나눠진 횟수를 저장하는 변수
for i in range(1, num + 1): # 1 ~ num
    if num % i == 0:
        count += 1
if count == 2:
    print("%d는 소수입니다."%num)
else:
    print("%d는 소수가 아닙니다."%num)
