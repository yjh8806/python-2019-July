#리스트안의 데이터를 요소라고 부를게요!
print("===요소 수정===")
a = [1, 2, 3]
a[1] = 22
print(a)

#리스트는 슬라이싱과 인덱싱의 연산결과가 다릅니다.
a = [1, 2, 3]
a[1:2] = ["a", "b", "c"]
print(a)

a = [1, 2, 3]
a[1] = ["a", "b", "c"]
print(a)

print("\n===요소 삭제===")
a = [1, 2, 3, 4, 5]
a[1:3] = []
print(a)

a = [1, 2, 3, 4, 5]
a[1] = []
a[2] = []
print(a)

#del은 인덱싱이든 슬라이싱이든 그 범위의 데이터를 없애줍니다!
del a[2:4]
print(a)

#del은 리스트 명령어가 아니라 파이썬 전체 명령어
a = 5
del a
# print(a) a라는 공간이 삭제되었다.

#문자열은 한번 선언되면 수정, 삭제가 안되요
b = "itbank"
# b[3] = " "
# del b[3]
