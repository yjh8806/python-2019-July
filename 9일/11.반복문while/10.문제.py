import os
menu = {"콜라":1200, "사이다":1200,"조지아":1000,"컨피던스":600}
money = int(input("돈을 입력해주세요 : "))
while True: #무한반복문
    print("==============자판기==============")
    print("""
    콜라 : 1,200원
    사이다 : 1,000원
    조지아 : 1,000원
    컨피던스 : 600원
    >> 종료
    """)
    choice = input("음료 선택 : ")
    if choice == "종료":
        print("잔액 : %d"%money)
        print("자판기 프로그램을 종료합니다.")
        break
    elif choice not in menu: #key에 없는걸 눌렀네?
        print("잘못된 입력입니다.")
    elif menu[choice] <= money: #내 돈으로 물건을 살 수있는가?
        money -= menu[choice]
        print("%s를 샀습니다."%choice)
        print("잔액 : %d"%money)
    elif menu[choice] > money:
        print("잔돈 부족")
    os.system("pause") #코드 일시정지
    os.system("cls") #콘솔창 지우기
