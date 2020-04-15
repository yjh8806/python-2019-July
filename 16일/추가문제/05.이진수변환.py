#10진수를 거꾸로 만드는문제 응용하면 풀려요

#48 => 110000
#48 % 2 => 0 * 1
#24 % 2 => 0 * 10
#12 % 2 => 0 * 100
#6 % 2 => 0 * 1000
#3 % 2 => 1 * 10000
#1 % 2 => 1 * 100000
# bin(decimal)
decimal = int(input("10진 정수 입력 : "))
binary = 0 #이진수를 저장할 변수
digit = 1 #자릿수
while decimal > 0:
    binary += decimal % 2 * digit
    digit *= 10
    dicimal //= 2
print(binary)
