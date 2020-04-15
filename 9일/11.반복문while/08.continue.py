#while, break, continue : 문법이 다른언어에서도 똑같아요

num = int(input("정수 입력 : "))
i = 0
while i < num:
    i += 1
    if i % 3 != 0:
        continue #아래의 코드를 실행하지 않고 반복문의 조건식으로 이동
    print(i)
