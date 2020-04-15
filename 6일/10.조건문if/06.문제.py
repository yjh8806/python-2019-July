year,month,day = int(input("년 : ")), int(input("월 : ")), int(input("일 : "))
#2008 % 10 => 8

# if str(year - month + day)[-1] == '0':
if (year - month + day) % 10 == 0:
    print("올해 대박")
else:
    print("그럭저럭")
