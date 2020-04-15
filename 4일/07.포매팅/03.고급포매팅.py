print("I have a {0}".format("Pen"))
print("I have a %s"%"Pen")

print()
#"{숫자}".format(데이터) : 데이터의 인덱스번호
print("""I have a {0}, I have a Apple,
Apple{0},
I have a {0}, I have a PineApple,
PineApple{0}""".format("Pen"))

print("\n===고급포매팅 변수이용===")
a = "Pen"
b = "Apple"
print("""I have a {0}, I have a {1},
{1}{0},
I have a {0}, I have a Pine{1},
Pine{1}{0}""".format(a, b))

print("\n===고급포매팅 혼합이용===")
#공간에 이름을 지정할 수 있다.
print("""I ate {number} cakes,
so I was sick for {day}days""".format(number = 10, day = 3))
