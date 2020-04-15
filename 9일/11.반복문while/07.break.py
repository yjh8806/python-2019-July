import os
while True:
    i = 1 #곱해주는 수를 항상 1로 초기화
    num = int(input("몇 단?(0을 입력 시 종료) : "))
    if num == 0:
        print("구구단 프로그램을 종료합니다.")
        break
    while i < 10:
        print("%d x %d = %d"%(num, i, num * i))
        i += 1
    os.system("pause")
    os.system("cls")
