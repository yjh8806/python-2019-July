#최대공약수!
max_list = []
MAX = 0
num1, num2 = int(input("첫 번째 : ")), int(input("두 번째 : "))
for i in range(1, min(num1, num2) + 1):
    if num1 % i == 0 and num2 % i == 0: #공약수
        max_list.append(i)
        MAX = i
print("최대공약수 : %d"%MAX)
print("최대공약수 : %d"%max(max_list))
