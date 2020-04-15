a = [[10, 20], [30, 40], [50, 60]]
print(a)

a = [[10, 20],
    [30, 40],
    [50, 60]]

#이차원리스트[행][열]
a[0][0] = 1000
a[1][1] = 2000
a[2][1] = 3000
print(a)

for i, j in a:
    print(i, j)

for i in range(len(a)): #행의 개수
    for j in range(len(a[i])): #열의 개수
        print(a[i][j],end=" ")
    print()

print("\n===2중 for문 리스트 초기화===")
a = []
num = 10
for i in range(8): #행
    line = [] #안쪽에 넣을 리스트
    for j in range(8): #열
        line.append(num)
        num += 10
    a.append(line)
print(a)

print("\n===리스트 표현식===")
#중급자용 문법
num_list = [num for num in range(1, 6)]
print(num_list)

num_list = [num for num in range(1, 11) if num % 2 == 0]
print(num_list)

num = 10
a = [[num for j in range(2)] for i in range(3)]
print(a)
