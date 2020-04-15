gender = input("당신의 성별은[남/여]? : ")
age = int(input("당신의 나이는? : "))
genderlist = ["남", "여"]

#and(*) : 붙어있는 모든 조건식이 True여야지 True
#or(+) : 붙어있는 모든 조건식이 False여야지 fasle
if gender in genderlist: #gender가 genderlist안에 있으면 아래의 문장 실행
    if gender == "남" and age >= 19:
        print("군대 입영대상자 입니다.")
    if gender == "여" or age < 19:
        print("군대 입영대상자가 아닙니다.")
else:
    print("잘못된 성별 입력입니다.")
