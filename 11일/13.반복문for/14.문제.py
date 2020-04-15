num = int(input("출력할 별의 행 : "))
for i in range(num): #i는 별을 몇 행 출력할지
    for j in range(i): #공백을 출력하는 for
        print(" ",end="")
    for j in range((num - i) * 2 - 1):
        print("*",end="")
    print()
