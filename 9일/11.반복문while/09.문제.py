num = 0
result = 0
while num < 1000:
    num += 1
    if num % 3 == 0 and num % 5 == 0:
        result += num
    if num % 3 == 0:
        continue
    result += num
print("합계 : %d"%result)
