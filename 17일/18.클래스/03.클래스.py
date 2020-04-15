class Waffle:
    taste = "아무맛도 안나" #self.taste
    #self는 매개변수와 내 필드를 구분하는 문법
    #self => 자바가면 this라고 사용
    def __init__(self, taste):
        #요때 객체 만들어져요
        self.taste = taste
    def Taste(self):
        return self.taste

#waffle1.__init__("플레인")
waffle1 = Waffle("플레인")
waffle2 = Waffle("딸기")

print(waffle1.Taste())
print(waffle2.Taste())
