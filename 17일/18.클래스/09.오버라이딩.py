class Fruit:
    def __init__(self, gram, price):
        self.gram = gram
        self.price = price
    def printInfo(self):
        print("무게 : %d g, 가격 : %d원"%(self.gram, self.price))

class BigFruit(Fruit):
    def printInfo(self):
        print("무게 : %.2f kg, 가격 : %d원"%(self.gram * 0.001, self.price))

banana = Fruit(500, 5000)
banana.printInfo()

wattermelon = BigFruit(1600, 17000)
wattermelon.printInfo()
