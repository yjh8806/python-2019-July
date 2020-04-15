song = [input("이름 : "), int(input("나이 : ")), float(input("왼쪽 시력 : ")), float(input("오른쪽 시력 : "))]
kim = [input("이름 : "), int(input("나이 : ")), float(input("왼쪽 시력 : ")), float(input("오른쪽 시력 : "))]

age = (song[1] + kim[1])/2
see = (song[3] + kim[3])/2

print("평균 나이 : %.2f, 평균 오른쪽 시력 : %.2f"%(age, see))
