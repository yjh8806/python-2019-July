a = "You need Python"
#문자열[a:] : a부터 끝까지 슬라이싱
print(a[9:])

#문자열[:a] : 0부터 a-1까지 슬라이싱
print(a[:8])

#문자열[:] : 처음부터 끝까지 선택 => 문제로...
print(a[:])

#문자열[a:b:c] : a부터 b-1까지 c칸씩 건너띄면서 슬라이싱
#c를 생략시 1이 기본값
a = "123456789"
even = a[1::2]
odd = a[::2]
reverse = a[::-1]
print(even)
print(odd)
print(reverse)
