kor = int(input("국어 점수 : "))
eng = int(input("영어 점수 : "))
math = int(input("수학 점수 : "))
sum = kor + eng + math
avg = sum / 3 #c언어때는 둘중 하나를 실수로 바꿔줘야 실수로 나옵니다.
print("합계 : %d, 평균 : %.2f"%(sum,avg))
