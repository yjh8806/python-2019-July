#문자열변수[인덱스번호]
book = "Welcome to Python"
print(book[0])
print(book[3])
print(book[-1])
print(book[-6])

#len(문자열) : 문자열의 길이를 반환
length = len(book)
print("문자열의 길이 :",length)
print(book[length - 1]) #마지막 인덱스는 총 글자수보다 하나 작다

book = "Welcome to Python"
Wet = book[0] + book[1] + book[8]
print(Wet)

Phone = book[-6] + book[-3] + book[-2] + book[-1] + book[1]
print(Phone)
