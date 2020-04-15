a = [] #바깥 리스트
num = 1
for i in range(8): #행의 개수
    line = [] #안쪽 리스트
    for j in range(8): #열의 개수
        line.append(num)
        num += 1
    a.append(line)
    print(line) #행만 출력
print(a)

num = 1
a = [[(num + j) + (i * 8) for j in range(8)] for i in range(8)]
print(a)
