print("a" in ("a" , "b", "c"))
print(7 in [1, 2, 3, 4, 5])
print("a" in "itbank")
#딕셔너리는 key에서만 찾아본다.
print("b" in {1:"a",2:"b",3:"c"})

pocket = ["phone", "card", "세종대왕"]

print("떡볶이를 사먹고 싶은데 주머니에 현금이 있나?")

if "세종대왕" in pocket:
    print("떡튀순에 라면추가")
else:
    print("현금인출기로 간다.")

num = int(input("숫자 입력 : "))
if num % 3 != 0:
    pass #일단 잠시 비워두고 싶을때
else:
    print("3의 배수 입니다.")
