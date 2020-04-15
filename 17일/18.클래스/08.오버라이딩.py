class Bank:
    def __init__(self, name, num):
        self.name = name #은행이름
        self.num = num  #은행계좌
    def deposit(self, money):
        if money > 0:
            self.money = money
            print("%s은행 %s계좌로 %s원 입금"%(self.name, self.num, self.money))
        else:
            print("잘못된 입력입니다.")
    #실제로는 메소드가 훨씬 많아요

#메소드 오버라이딩 : 수퍼클래스의 메소드를 같은이름, 다른 기능으로 덮어씌운다.
class BusanBank(Bank):
    def __init__(self, num):
        self.num = num  #은행계좌
    def deposit(self, money):
        if money > 0:
            self.money = money
            print("부산은행 %s계좌로 %s원 입금"%(self.num, self.money))
        else:
            print("잘못된 입력입니다.")

jinwoo = BusanBank("1122014901801")
jinwoo.deposit(50000)
