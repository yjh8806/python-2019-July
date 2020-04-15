mart = {"다이제":800, "메로나":500, "코카콜라":700, "츄파츕스":200}

#내장함수 : 자료형마다 가지고있는 함수들
a = "" #빈 문자열
b = [] #빈 리스트
c = () #빈 튜플

print("\n===key 리스트 만들기===")
mart_menu = list(mart.keys())
print(mart_menu)

print("\n===value 리스트 만들기===")
mart_price = list(mart.values())
print(mart_price)

print("\n===key로 value얻기===")
print(mart["다이제"])
print(mart.get("다이제"))

print("\n===☆☆☆☆☆해당 key가 있는지 찾아보기===")
#in : ~안에 있는
#not in : ~안에 없는
#컴퓨터에게 물어봐요 => True, False로 답을해줘요
print("다이제" in mart)
print("다이제" not in mart)
print("플레이스테이션4 프로" in mart)

#in은 모든 자료형에 사용가능
mart_menu = ["다이제", "메로나", "츄파츕스"]
print("다이제"  in mart_menu)
print("플레이스테이션4" in mart_menu)

print("\n===key와 value 모두 지우기===")
# del mart : 딕셔너리 변수가 없어짐
mart.clear()  #안에 내용물만 없어짐
print(mart)
