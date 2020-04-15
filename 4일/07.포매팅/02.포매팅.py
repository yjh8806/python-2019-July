#2개 이상의 값을 대입할때
#%(값1, 값2) : %뒤에 괄호를 열고 데이터를 넣어준다.
#차례대로 포맷코드에 대입된다.
num = 5
disert = "cakes"
print("I eat %s %s"%(num, disert))

print("\n===포매팅을 이용한 정렬===")
#%s 사이에 양수를 적어주면 우측정렬
#음수를 적으면 좌측정렬
print("%10s%5s"%("name","age"))
print("="*20)
print("%10s%5s"%("jinwoo","30"))
print("%10s%5s"%("dongyul","30"))
print("%10s%5s"%("bomin","22"))

print("="*20)
print("%-10s%-5s"%("jinwoo","30"))
print("%-10s%-5s"%("dongyul","30"))
print("%-10s%-5s"%("bomin","22"))

print("\n===포매팅을 이용한 소수점 표현===")
a = 3.141592
#%와 f사이에 .정수를 적으면 그 숫자만큼만 표현
print("%.4f"%a)
print("%.2f"%a)
#소수점 표현시에는 s를 적으면 안되요!
print("%.2s"%a)
