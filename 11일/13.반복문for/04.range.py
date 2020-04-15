#range : 범위를 지정
print(range(5))
print(list(range(5)))
print(tuple(range(5)))
print(list(range(1, 10, 2)))
a = list(range(1, 1001))

for i in range(5):
    print("i = %d"%i)
for i in range(3, 10):
    print(i)

print("\n===for + range활용===")
result = 0
for i in range(1, 11, 2):
    result += i
print(result)

result = 0
i = 1
while i < 11:
    if i % 2 != 0:
        result += i
    i += 1
print(result)

for i in range(10, 0, -1):
    print(i)
