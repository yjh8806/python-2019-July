import os #system함수를 사용하기 위한 모듈
#C언어 배우신 분들은 #include<> => header파일과 유사
num = 0
while True: #무한반복문 : 조건식이 거짓말이 안되는 반복문
    print("""
    ====메뉴====
    1.정수 입력
    2.입력된 정수 출력
    3.종료""")
    select = int(input("메뉴 선택 : "))
    if select == 1:
        num = int(input("정수 입력 : "))
    elif select == 2:
        if num != 0:
            print("입력된 정수 : %d"%num)
        else:
            print("정수를 먼저 입력하세요")
    else:
        exit(0) #프로그램 종료함수
    os.system("pause") #코드 일시정지
    os.system("cls")   #콘솔창을 지워줍니다.
