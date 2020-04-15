a = [3, 5, 2, 6, 1, 4]
# len() : 문자열 -> 문자열의 길이
#리스트 => 리스트 요소의 개수
print(len(a))

avg = sum(a) / 6
print("평균 : %.2f"%avg)

a.append(7)
avg = sum(a) / len(a)
print("평균 : %.2f"%avg)
