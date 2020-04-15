#문자열과 똑같이 인덱싱 가능
#인덱싱을 통해서 저장된 데이터를 끄집어올 수 있다.
a = [1, 2, 3] #연관있는 데이터를 저장
print(a)
print(a[0])
print(a[2])
print(a[0] + a[2])

student = ["kim", "lee", "park"]
print(student[0])
print(student[1])
print(student[2][1])

a = [1, 2, 3, ["a", "b", "abc"]]
# print(a[5][2]) 리스트의 인덱스 범위를 넘어갔어요!
print(a[3][2][2])
