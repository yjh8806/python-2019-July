kor,eng,math = int(input("국어 : ")),int(input("영어 : ")),int(input("수학 : "))
avg = (kor + eng + math)/3
if kor >= 0 and kor <= 100 and eng >= 0 and eng <= 100 and math >=0 and math<=100:
    if avg >= 90: #90 ~ 100
        print("A등급")
    elif avg >= 80: #80 ~ 89
        print("B등급")
    elif avg >= 70: #70 ~ 79
        print("C등급")
    elif avg >= 60: #60 ~ 69
        print("D등급")
    else:#0 ~ 59
        print("F등급")
else:
    print("잘못된 입력입니다.")
