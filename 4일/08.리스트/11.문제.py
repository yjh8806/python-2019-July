a = [3, 5, 2, 6, 1, 4]
a.sort()#오름차순정렬
a.reverse()#내림차순정렬
print(a)

b = [input("입력 : "),input("입력 : "),input("입력 : "),input("입력 : ")]
print(b)
c = b #c가 리스트형 변수가 된다.

c = [] #비어있는 리스트변수 => 내장함수 사용하기 위해
c.extend(b) #b를 추가

print(c)
