print("===문자열 개수 세기===")
#문자열.count("문자") : 문자열에서 문자의 개수를 세어줌
a = "happy"
print(a.count("p"))
print(a.count("k"))

print("===위치 알려주기1===")
#문자열.find("문자") : 문자열에서 문자의 인덱스번호를 반환
a = "Python is best choice"
print(a.find("b"))
print(a.find("k")) #없는 글자는 -1을 반환

print("\n===위치 알려주기2===")
a = "Python is best choice"
print(a.index("b"))
# print(a.index("k")) 없는 글자면 에러메시지를 출력

print("\n===문자열 삽입===")
a = "★"
print(a.join("가나다라마바사"))

print("\n===대문자 변환===")
a = "upper case"
A = a.upper() #대문자로 바뀐 글자를 A에 저장
print(a)
print(A)

print("\n===소문자 변환===")
A = "LOWER CASE"
a = A.lower()
print(a)

print("\n===왼쪽 공백지우기===")
#left strip
a = "               hi!"
print(a.lstrip())

print("\n===오른쪽 공백지우기===")
a = "hi!               "
print(a.rstrip() + "오른쪽")

print("\n===양쪽 공백지우기===")
a = "          hi!          "
print("왼쪽" + a.strip() + "오른쪽")

print("\n===문자열 교체===")
a = "Life is too short"
print(a.replace("Life", "Your leg"))

print("\n===문자열 나누기===")
a = "떡볶이 치킨 피자"
print(a.split()) #안에 아무것도 안적으면 공백을 기준으로 나눠준다
a = "떡볶이,치킨,피자"
print(a.split(",")) #안에 적은 글자를 기준으로 나줘준다. => 리스트로 나눠줘요
