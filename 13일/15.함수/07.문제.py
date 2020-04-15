#기본 자료형8개 매개변수나 반환값으로 사용가능
def fiveover(a): #a는 매개변수 -> 리스트형 변수가 되겠네요
    result = []
    for i in a:
        if i > 5:
            result.append(i)
    return result #반환값을 리스트로 해봤네요

numlist = []
for i in range(5):
    numlist.append(int(input("%d번째 정수 입력 : "%(i+1))))
print(fiveover(numlist))
