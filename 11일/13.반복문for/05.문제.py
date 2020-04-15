num = int(input("정수 입력 : "))
for i in range(num, 0, -1):
    print(i,end=" ")
print()

for i in range(1, num+1)[::-1]:
    print(i,end=" ")
print()

for i in range(4): #0, 1, 2, 3
    num = int(input("양수 입력 : "))
    if num < 0:
        print("음수입니다.")
    elif num == 0:
        print("0입니다.")
    elif num % 2 == 0:
        print("짝수 입니다.")
    elif num % 2 != 0:
        print("홀수 입니다.")
