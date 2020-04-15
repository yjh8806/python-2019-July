#내가 원하는 만큼 다 입력받고 그 숫자들의 평균을 구하는 프로그램 제작
num = 1
count = 0 #몇 번 입력받았는지
result = 0 #총 합계
while num != 0: #num이 0이 아니면 반복
    num = int(input("정수 입력(0입력 시 종료) : "))
    count += 1
    result += num
count -= 1 #마지막에 0을 입력했을때의 횟수를 제외
avg = result / count
print("평균 : %.2f"%avg)
