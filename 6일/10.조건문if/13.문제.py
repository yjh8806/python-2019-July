dumpling = int(input("만두 개수 입력 : "))
price = 1000
if dumpling > 0 and dumpling < 10:
    price *= dumpling #대입연산자 price = price * dumpling
elif dumpling >= 10 and dumpling < 100:
    price *= 0.85 * dumpling
elif dumpling >= 100:
    price *= 0.75 * dumpling
else: #0보다 작아
    print("잘못된 개수입니다.")
print("가격 : %d원, 현금결제가 : %s원"%(price,price*0.9))
