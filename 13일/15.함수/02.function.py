#매개변수가 있다 : 함수를 호출할 때 인자를 넣어준다
#반환값이 있다 : 함수를 호출한 곳으로 데이터를 돌려보낸다. => 저장, 출력

#store = input("인자값") => 매개변수와 반환값이 있는 함수
#store = print("인자값") => 매개변수는 있는데 반환값이 없는 함수
#A = "abc".upper() => 매개변수는 없는데 반환값이 있는 함수
#list.sort() => 매개변수와 반환값이 없는 함수

#매개변수와 반환값이 있는 함수
def avg(a, b):
    return (a + b) / 2

x, y = int(input("정수 1 : ")), int(input("정수 2 : "))
print("평균 : %.2f"%avg(x, y))

#매개변수는 있고 반환값이 없는 함수
def avg(a, b):
    print("평균 : %.2f"%((a + b) / 2))

x, y = int(input("정수 1 : ")), int(input("정수 2 : "))
avg(x, y)

#매개변수는 없고 반환값이 있는 함수
def avg():
    x, y = int(input("정수 1 : ")), int(input("정수 2 : "))
    return (x + y) / 2

print("평균 : %.2f"%avg())

#매개변수와 반환값이 없는 함수
def avg():
    x, y = int(input("정수 1 : ")), int(input("정수 2 : "))
    print("평균 : %.2f"%((x + y) / 2))

avg() #함수호출
