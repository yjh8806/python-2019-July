import os
def sum(a, b):
    return a + b
def sub(a, b):
    return a - b
def mul(a, b):
    return a * b
def divi(a, b):
    return a // b
while(1): #무한반복문 : 조건식이 거짓말이 안되면 무한반복문
    num1, num2 = map(int, input("정수 두 개 입력 : ").split())
    print("1.더하기\n2.빼기\n3.곱하기\n4.나누기\n5.종료") #메뉴판
    select = int(input("계산할 방식을 선택하세요 : "))
    if select == 1:
        print("%d + %d = %d"%(num1,num2,sum(num1,num2)))
    elif select == 2:
        print("%d - %d = %d"%(num1,num2,sub(num1,num2)))
    elif select == 3:
        print("%d * %d = %d"%(num1,num2,mul(num1,num2)))
    elif select == 4:
        print("%d / %d = %d"%(num1,num2,divi(num1,num2)))
    elif select == 5:
        break
    else:#잘 못 입력할때 오류메시지
        print("잘못된 입력입니다.")
    os.system("pause")
    os.system("cls")
