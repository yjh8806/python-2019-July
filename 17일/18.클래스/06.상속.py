#상속 : 기존 클래스를 변경하지 않고 기능을 추가하거나 기존 기능을 변경하여 사용할때 사용
#개발기간을 단축하거나 코드의 중복을 피할 수 있다.
#SmartTv를 만들고 싶어 => 기존의 Tv클래스를 상속받아서 기능을 추가하면 SmartTv
class Tv: #부모클래스, 수퍼클래스
    def powerOn(self):
        print("TV를 켭니다.")
    def powerOff(self):
        print("TV를 끕니다.")

class SmartTv(Tv): #자식클래스, 서브클래스
    def settopOn(self):
        print("셋톱을 켭니다.")
    def settopOff(self):
        print("셋톱을 끕니다.")
    def search(self, search):
        print("%s를 검색합니다."%search)

#상속받은 부모의 모든 필드, 메소드를 사용할 수 있다.
#상속, 오버라이딩 => 클래스개념의 기초
stv = SmartTv() #자식객체 생성
stv.powerOn() #부모
stv.settopOn() #내꺼
stv.search("나혼자산다") #내꺼
stv.settopOff() #내꺼
stv.powerOff() #부모
