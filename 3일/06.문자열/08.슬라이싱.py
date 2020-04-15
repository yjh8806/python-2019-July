#문자열변수[start:end-1]
a = "Life is too short, You need Python"
book = a[0:7] #0 ~ 6번 인덱스까지 슬라이싱
print(book)
book = a[12:17]
print(book)

print(a[0:7] + " " + a[12:17])