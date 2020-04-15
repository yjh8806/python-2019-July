def odd_even(num):
    if num % 2 == 0:
        print("짝수입니다.")
    else:
        print("홀수입니다.")

num = int(input("정수 입력 : "))
odd_even(num)

def total(a):
    result = 0
    for i in range(1, a + 1):
        result += i
    return result #반환값

print("누적합계 : %d"%total(10))

#제곱
def power(a, b):
    result = 1
    for i in range(b):
        result *= a
    return result

print(power(2, 3))
print(power(2, 10))
