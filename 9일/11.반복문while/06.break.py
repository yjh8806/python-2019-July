# num1 = int(input("정수1 : "))
# num2 = int(input("정수2 : "))
# i = 1
#
# while True: #무한반복문
#     if i % num1 == 0 and i % num2 == 0:
#         break #반복문을 탈출
#     i += 1
#
# print("최소공배수 : %d"%i)

while True:
    string = input("알파벳을 입력(q를 누르면 종료) : ")
    if string == 'q':
        break
    else:
        print(string.upper())
