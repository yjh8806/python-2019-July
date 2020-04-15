mart = {"다이제":800, "메로나":500, "코카콜라":500, "츄파츕스":200}
menu = tuple(mart.keys())
print(menu)

price = sum(mart.values())
print(price)

#=은 오른쪽 항의 연산을 끝낸 후 그 결과를 왼쪽항에 대입
mart[input("과자 : ")] = int(input("가격 : "))
print(mart)

#언패킹 : 오른쪽의 데이터를 왼쪽에 풀어준다.
a, b = input("과자 : "), int(input("가격 : "))
mart[a] = b

print(mart)
