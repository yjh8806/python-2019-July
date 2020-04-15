class Tv:
    def __init__(self):
        self.power = False #bool자료형
        self.ch = 8
        self.vl = 20
    def powerSwitch(self):
        self.power = not(self.power) #not : True, False를 바꿔줍니다.
        self.show() #메소드 내부에서 다른 메소드 호출가능
    def chUp(self):
        self.ch += 1
        self.show()
    def chDown(self):
        self.ch -= 1
        self.show()
    def vlUp(self):
        self.vl += 1
        self.show()
    def vlDown(self):
        self.vl -= 1
        self.show()
    def show(self):
        if self.power == True:
            print("ch : %d, vl : %d"%(self.ch, self.vl))
        else:
            print("------------------")

LgTv = Tv()
LgTv.powerSwitch() #전원 켜짐
LgTv.chDown()
LgTv.chUp()
LgTv.vlUp()
LgTv.vlUp()
LgTv.powerSwitch() #전원 꺼짐
