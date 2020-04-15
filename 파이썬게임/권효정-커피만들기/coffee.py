import time as t
import os

star = 5
menu = ["에스프레소", "아메리카노", "카페라떼", "카푸치노", "카페모카", "카라멜 마키아또"]
ingredients = ["에스프레소", "물", "우유", "우유거품", "초코시럽", "카라멜시럽", "휘핑크림"]

class Coffee:
    def __init__(self,order):
        self.order = order

    def Recipe(self,order):
        self.order = order
        if order == menu[0]:
            print()
            recipe = [ingredients[0]]
            print("%s 레시피는 %s 입니다."%(menu[0],recipe))
        elif order == menu[1]:
            recipe = [ingredients[0],ingredients[1]]
        elif order == menu[2]:
            recipe = [ingredients[0],ingredients[2]]
        elif order == menu[3]:
            recipe = [ingredients[0],ingredients[2],ingredients[3]]
        elif order == menu[4]:
            recipe = [ingredients[4],ingredients[0],ingredients[2],ingredients[6]]
        elif order == menu[5]:
            recipe = [ingredients[4],ingredients[0],ingredients[2],ingredients[3]]

    def Ingredients(self,ingredient):
        self.ingredient = ingredient
        ingredient = input("재료 : ")
        if ingredient != "에스프레소":
            print("재료를 잘못넣었습니다.")
            star -= 3

#에스프레소 타임
    def ET(self):
        global star

        start = t.time()
        input("<Enter>를 누르면 시간만큼 재료가 들어갑니다.")
        end = t.time()
        result = end - start

        if result == 3:
            print("%s 원샷을 넣었습니다."%self)
        elif result > 3:
            if result < 4:
                print("조금 많이 넣었습니다.")
                star -= 1
            elif result == 6 :
                print("더블샷입니다.")
            elif result == 9:
                print("쓰리샷입니다.")
            else:
                print("너무 많이 넣었습니다.")
                star -= 2
        elif result < 3:
            if result < 1:
                print("너무 적습니다.")
                star -= 2
            elif result < 2:
                print("조금 적습니다.")
                star -= 1

class CoffeeTime(Coffee):

    def OT(self):
        global star
        ingredient = input("재료 : ")
        start = t.time()
        input("<Enter>를 누르면 시간만큼 재료가 들어갑니다.")
        end = t.time()
        result = end - start

        if result == 1:
            print("%s 정량을 넣었습니다."%self)
        elif result > 1:
            print("많이 넣었습니다.")
            star -= 1
        elif result < 1:
            print("조금 넣었습니다.")
            star -= 1

#3초 카운트
    def TT(self):
        global star
        ingredient = input("재료 : ")
        start = t.time()
        input("<Enter>를 누르면 시간만큼 재료가 들어갑니다.")
        end = t.time()
        result = end - start

        if result == 3:
            print("%s 정량을 넣었습니다."%self)
        elif result > 3:
            if result < 4:
                print("조금 많이 넣었습니다.")
                star -= 1
            else:
                print("너무 많이 넣었습니다.")
                star -= 2
        elif result < 3:
            if result < 1:
                print("너무 적습니다.")
                star -= 2
            elif result < 2:
                print("조금 적습니다.")
                star -= 1


#7초 카운트
    def ST(self):
        global star
        ingredient = input("재료 : ")
        start = t.time()
        input("<Enter>를 누르면 시간만큼 재료가 들어갑니다.")
        end = t.time()
        result = end - start

        if result == 7:
            print("%s 정량을 넣었습니다."%self)
        elif result > 7:
            if result < 10:
                print("조금 많이 넣었습니다.")
                star -= 1
            else:
                print("너무 많이 넣었습니다.")
                star -= 2
        elif result < 7:
            if result < 3:
                print("너무 적습니다.")
                star -= 2
            elif result < 5:
                print("조금 적습니다.")
                star -= 1

#12초 카운트
    def TlT(self):
        global star
        ingredient = input("재료 : ")
        start = t.time()
        input("<Enter>를 누르면 시간만큼 재료가 들어갑니다.")
        end = t.time()
        result = end - start

        if result == 12:
            print("%s 정량을 넣었습니다."%self)
        elif result > 12:
            if result < 15:
                print("조금 많이 넣었습니다.")
                star -= 1
            else:
                print("너무 많이 넣었습니다.")
                star -= 2
        elif result < 12:
            if result < 8:
                print("너무 적습니다.")
                star -= 2
            elif result < 10:
                print("조금 적습니다.")
                star -= 1

#15초 카운트
    def FT(self):
        global star
        ingredient = input("재료 : ")
        start = t.time()
        input("<Enter>를 누르면 시간만큼 재료가 들어갑니다.")
        end = t.time()
        result = end - start

        if result == 15:
            print("%s 정량을 넣었습니다."%self)
        elif result > 15:
            if result < 17:
                print("조금 많이 넣었습니다.")
                star -= 1
            else:
                print("너무 많이 넣었습니다.")
                star -= 2
        elif result < 15:
            if result < 10:
                print("너무 적습니다.")
                star -= 2
            elif result < 12:
                print("조금 적습니다.")
                star -= 1

#입출력
# menu = ["에스프레소", "아메리카노", "카페라떼", "카푸치노", "카페모카", "카라멜 마키아또"]
while True:
    print("메뉴 : %s"%menu)
    order = input("주문하시겠습니까?  ")
    print("%s, 주문 받았습니다."%order)
    print()
    print("☆★"*10)

#제작
# ingredients = ["에스프레소", "물", "우유", "우유거품", "초코시럽", "카라멜시럽", "휘핑크림"]
    print()
    print("커피를 만들어요. 컵을 꺼냈습니다. 재료를 선택해서 정량을 넣어주세요.")
    print("10ml 당 1초 입니다.")
    print(ingredients)

    CT = CoffeeTime(order)

    if order == menu[0]:

        CT.EI(order)
        CT.ET()
    elif order == menu[1]:
        print("%s 레시피는 에스프레소 30ml, 물 150ml 입니다."%menu[1])
        CT.ET()
        CT.FT()
    elif order == menu[2]:
        print("%s 레시피는 에스프레소 30ml, 우유 150ml 입니다."%menu[2])
        CT.ET()
        CT.FT()
    elif order == menu[3]:
        print("%s 레시피는 에스프레소 30ml, 우유 70ml, 우유거품 70ml 입니다."%menu[3])
        CT.ET()
        CT.ST()
        CT.ST()
    elif order == menu[4]:
        print("%s 레시피는 초코시럽 30ml, 에스프레소 30ml, 우유 120ml, 휘핑크림 입니다."%menu[3])
        CT.TT()
        CT.ET()
        CT.TlT()
        CT.OT()
    elif order == menu[5]:
        print("%s 레시피는 카라멜시럽 30ml, 에스프레소 30ml, 우유 120ml, 우유크림,카라멜시럽 입니다."%menu[5])
        CT.TT()
        CT.ET()
        CT.TlT()
        CT.OT()
        CT.OT()
    else:
        print("잘못된 입력입니다.")
        os.system("pause")
        os.system("cls")

    print("커피맛은...!")
    t.sleep(3)
    print("★"*star)
    os.system("pause")
    os.system("cls")
