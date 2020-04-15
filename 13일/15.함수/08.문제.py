def reverse_number(a):
    while a > 0:
        print(a % 10,end = "")
        a //= 10
reverse_number(int(input("정수 입력 : ")))
