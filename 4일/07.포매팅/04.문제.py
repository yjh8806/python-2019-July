kg = "KG ITBANK"
address = "부산광역시 수영구 민락동"
start = 15
name = "송진우"
end = 18
height = 170.2145
age = 30
Phone = "010-5567-1430"
#위의 변수를 이용하여 아래와 같이 출력

print("{}{}{}".format("☆"*10,kg,"☆"*10))
print("파이썬 강의 : {0}시 ~ {1}시".format(start,end))
print("본인 이름 : {}".format(name))
print("본인 나이 : {}".format(age))
print("핸드폰 : %s"%Phone)
print("주소 : %s"%address)
print("키 : %.2f"%height)
print("%s%s%s"%("☆"*10,kg,"☆"*10))

#고급포매팅 소수점
#{인덱스번호:0.2f}
print("{0:.2f}".format(height))

#고급포매팅 간격
#{:<10} : 좌측정렬
#{:>10} : 우측정렬
#{:^10} : 가운데 정렬
print("이름 : {:<10}, 나이 : {:<3}".format("jinwoo",29))
print("이름 : {:>10}, 나이 : {:>3}".format("jinwoo",29))
print("이름 : {:^10}, 나이 : {:^3}".format("jinwoo",29))
