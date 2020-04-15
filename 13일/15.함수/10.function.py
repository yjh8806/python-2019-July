#정확한 매개변수의 개수를 모를때
#애스터리스크(*)가 붙은 매개변수 => 여러개의 매개변수를 전부 받아서 튜플로 저장할거야~
#args : arguments의 약자 => 관례적으로 사용
def total(*args):
    print(args)
    result = 0
    for i in args:
        result += i
    return result

print(total(1, 2, 3, 4, 5))

#항상 마지막에 적어줍시다!
def calc(oper, *args):
    if oper == '+':
        result = 0
        for i in args:
            result += i
    elif oper == '*':
        result = 1
        for i in args:
            result *= i
    return result

print(calc('+', 1, 2, 3, 4, 5))

print("\n===키워드 파라미터===")
#애스터리스크(*)가 매개변수 앞에 두 개 붙어요 => 딕셔너리로 저장
#{"key1":"value1"}
#func(name="song", age=30) key는 ""없이도 다 글자로 저장

def dict_kwargs(**kwargs):
    print(kwargs)

dict_kwargs(rank1="java", rank2="C",rank3="C++",rank4="Python")

print("\n===함수의 return===")
#함수의 종료조건
#1.함수의 모든 코드 실행
#2.return을 만나면 종료

def calc(a, b):
    return a + b
    return a - b

print(calc(10, 20))

print("\n===함수의 return2===")
#다른언어에서는 에러가 떠요
#return값은 딱 하나의 요소만 return
#,로 묶어주면 튜플이 됩니다 => 하나의 요소
def calc(a, b):
    return a + b, a - b

print(calc(10, 20))

print("\n===함수의 return3===")
def nick_name(a):
    if a == "바보":
        return #함수 종료
    print("나의 별명은 %s입니다."%a)
nick_name("바보")
nick_name("송선생")

print("\n===함수의 디폴트 매개변수===")
#매개변수와 인자의 개수가 같아야됩니다.
#인자값은 왼쪽의 매개변수부터 하나씩 차례로 들어갑니다.
def r_c_p(i, you="안냈다"):
    if you == "안냈다":
        print("안냈으니 내가 이겼다!")
        return #함수 종료
    if i == you:
        print("비겼다")
    elif (i == "가위" and you == "바위") or (i == "바위" and you == "보") or (i == "보" and you == "가위"):
        print("졌다ㅜㅜ")
    else:
        print("이겼다!")

print("안내면 진거 가위바위보!")
r_c_p("가위")
r_c_p("가위", "바위")
