print("\n===요소 추가===")
#하나씩 요소 추가
a = [1, 2, 3]
a.append(4)
print(a)

print("\n===리스트 확장===")
a = [1, 2, 3]
a.extend([4, 5, 6])
print(a)

b = [7, 8]
a.extend(b)
print(a)

print("\n===정렬===")
#sort : 오름차순 정렬
a = [4, 8, 2, 7, 6]
a.sort()
print(a)

#a ~ z까지 오름차순 정렬
a = ["i", "t", "b", "a", "n", "k"]
a.sort()
print(a)

print("\n===뒤집기===")
a = ["a", "b", "c", "d", "e"]
a.reverse()
print(a)

a = [4, 8, 2, 7, 6]
a.sort() #오름차순 정렬
a.reverse() #내림차순 정렬
print(a)

print("\n===위치 찾기===")
a = [1, 2, 3]
print(a.index(3))

print("\n===요소 삽입===")
#insert(인덱스번호, 삽입할 데이터)
a = [1, 2, 3]
a.insert(0, 4)
print(a)

print("\n===요소 제거===")
a = [1, 2, 3, 1, 2, 3]
a.remove(2)
print(a)
a.remove(2)
print(a)

print("\n===요소 끄집어내기===")
#자료구조 => push, pop을 배울건데
a = [1, 2, 3]
num1 = a.pop()
print(num1)
print(a)

print("\n===요소 개수 세기===")
a = [1, 2, 3, 4, 1]
print(a.count(1))
