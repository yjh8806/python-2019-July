#C언어는 {}로 종속문장을 구분
#파이썬은 공백으로 구분 => 스페이스바 4번
# time = float(input("현재 시간 : "))
# if time >= 18.5:
#     print("집에가자~")
# else:
#     print("공부합시다.^^")

#print()내부에 end공간에 "\n"를 넣어놓은거에요
age = int(input("당신의 나이를 입력 : "))
if age > 19:
    print("당신은 성인",end="☆")
else:
    print("당신은 미성년자",end="☆")
print("입니다.")

money = True #bool자료형 : 컴퓨터가 대답해주는형태(True, False)
print("케이크 집에 가서 ",end="")
if money:
    print("먹는다")
    print("냠냠")
else:
    print("손가락만 빨고 있어ㅜ")

num = int(input("정수 입력 : "))
#print("%d"%포맷코드, end="")
if num < 0:
    print("%d는 음의 정수"%num, end="")
else:
    print("%d는 양의 정수"%num, end="")
print("입니다.")
