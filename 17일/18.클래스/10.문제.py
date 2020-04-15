class Animal: #모든 동물의 공통 기능
    def __init__(self, weight, sound):
        self.weight = weight
        self.sound = sound
    def sleep(self):
        print("코 잔다")
    def speak(self):
        print(self.sound)
    def eat(self):
        print("먹는다")
    def show(self):
        print("동물 : %.2fkg"%self.weight)
class Cat(Animal):
    def eat(self):
        print("츄르를 먹는다")
    def show(self):
        print("고양이 : %.2fkg"%self.weight)
class Dog(Animal):
    def eat(self):
        print("개껌을 먹는다")
    def show(self):
        print("개 : %.2fkg"%self.weight)


jinwoo = Animal(66, "진우진우")
jinwoo.sleep()
jinwoo.eat()
jinwoo.speak()
jinwoo.show()
print()
cheeze = Cat(3.5, "냥냥")
cheeze.sleep()
cheeze.eat()
cheeze.speak()
cheeze.show()
print()
dangdang = Dog(6.5, "멍멍")
dangdang.sleep()
dangdang.eat()
dangdang.speak()
dangdang.show()
print()
