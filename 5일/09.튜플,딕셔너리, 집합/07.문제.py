print("===문제1===")
a = set([1, 2, 3, 4, 5, 6])
b = set([4, 5, 6, 7, 8, 9])
c = set([5, 6, 7, 8, 9, 10])

#교집합 a & b & c
#합집합 a | b | c
#차집합 a - b - c
print(tuple(a.intersection(b, c)))
print(tuple(a.union(b, c)))
print(tuple(a.difference(b, c)))

print("\n===문제2===")
a = [1, 1, 5, 5, 4, 3, 6, 7, 2, 1, 5, 5, 8, 5]
#데이터가 한 오백개라고 상상 => set() => 중복된게 없어지고 => list() => 인덱싱까지 가능
a = list(set(a))
print(a)

print("\n===문제3===")
d = set([1, 2, 3, 4, 5, 6])
e = set([4, 5, 6, 7, 8, 9])
f = set([5, 6, 7, 8, 9, 10])
e.remove(4)
e.remove(5)
f.remove(5)
e.update([1, 2])
print(d - e - f)
