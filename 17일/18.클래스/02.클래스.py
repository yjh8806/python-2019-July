class Calc: #계산기 클래스 선언(클래스의 첫 글자는 대문자로)
    #필드 : 클래스 내부의 변수
    #메소드 : 클래스 내부의 함수
    #메소드의 첫 번째 매개변수는 self => 현재 객체가 들어감
    result = 0
    def __init__(self): #생성자 : 클래스로 객체를 만들때 호출되는 함수
        self.result = 0
    def adder(self, num):
        self.result += num
        return self.result

#객체 : 클래스로 만든 변수
#calc1.__init__() 생성자 호출
calc1 = Calc() #계산기 클래스로 calc1객체(변수) 생성
calc2 = Calc()
calc3 = Calc()

print(calc1.adder(3))
print(calc1.adder(5))
print(calc1.adder(7))
print()
print(calc2.adder(2))
print(calc2.adder(4))
print(calc2.adder(6))
