num = int(input("출력할 별의 행 : "))
for i in range(num): #i는 별을 몇 행 출력할지
    for j in range(i + 1): #j는 한 행당 별을 몇 개 출력할지
        print("*",end="")
    print()
