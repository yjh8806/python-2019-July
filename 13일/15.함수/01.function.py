#함수를 사용하면 코드의 길이가 짧아져요
#유지보수가 쉬워져요 => 어디서 오류가 낫는지 찾기 쉬워져요
#재사용이 가능하다. => print(), randint(), system() => 라이브러리 함수

def func(x): #def 함수명(매개변수(parameter)):
    y = x * 2 + 1
    return y #반환값 : 함수를 호출한 곳으로 돌려보낼 데이터

result = func(2) #함수호출(인자값(argument))
print(result)

#반환값이 있다 : 돌아온 데이터를 출력 또는 저장
def avg(a, b):
    result = (a + b) / 2
    return result
print("평균 : %.2f"%avg(10, 20))
print("평균 : %.2f"%avg(3, 17))
print("평균 : %.2f"%avg(4, 7))

#곱하기 함수를 만들어주세요 이름은 mul
