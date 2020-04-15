year, reginum = int(input("생년월일 6자리 : ")), int(input("성별번호 : "))
#reginum이 1, 2면 1900년대
#reginum이 3, 4면 2000년대
#901129 1 => 901129 // 10000 => 2019 - (90 + 1900) + 1
#080823 4 => 080823 // 10000 => 2019 - (08 + 2000) + 1
birth_year = year // 10000

if reginum == 1 or reginum == 2:
    print("성별정보가 %d이므로, %d년생, %d살 입니다."%(reginum,birth_year + 1900 , 2019-(birth_year + 1900) + 1 ))
elif reginum == 3 or reginum == 4:
    print("성별정보가 %d이므로, %d년생, %d살 입니다."%(reginum,birth_year + 2000 , 2019-(birth_year + 2000) + 1 ))
else:
    print("잘못된 입력입니다.")
