print("===문제1===")
num = int(input("숫자 입력 : "))
count = 1
result = 0
while count <= num:
    result += count
    count += 1
print("1부터 %d까지의 누적합계 : %d"%(num, result))

print("===문제2===")
count = 0 #0부터 시작
while count < 10: # 0 ~ 9 : 10번 반복
    print("Hello Python")
    count += 1

# print("===문제3===")
# result = 0
# num = 1
# while num != 0:
#     num = int(input("숫자 입력(0 입력 시 종료) : "))
#     result += num
# print("합계 : %d"%result)

print("===문제4===")
num = int(input("거꾸로 할 정수 입력 : "))
# 1234 % 10 => 4
# 123 % 10 => 3
# 12 % 10 => 2
# 1 % 10 => 1
while num > 0:
    print(num % 10,end="")
    num //= 10

#1234 % 10 => 4
#123 % 10 => 40 + 3
#12 % 10 => 430 + 2
#1 % 10 => 4320 + 1

# reverse_num = 0
# while num > 0:
#     reverse_num = reverse_num * 10 + num % 10
#     num //= 10
# print(reverse_num)

print("===문제5===")
num = int(input("정수 입력 : "))
count = 1
while count <= num:
    print("%d"%(num * count),end=" ")
    count += 1
