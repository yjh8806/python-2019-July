sumlist = []
sum(sumlist)
sum = 0 #기존의 sum()함수 sum변수로 덮어씌어짐
while True: #0을 입력할때까지 숫자 입력
    num = int(input("정수 입력(0 입력 시 종료) : "))
    if num == 0:
        break
    sumlist.append(num)
for i in sumlist: #안에 뭐가 들었는지 출력하면서 더해주세요
    print(i)
    sum += i
# print("합계 : %d"%sum(sumlist))
print("합계 : %d"%sum)
