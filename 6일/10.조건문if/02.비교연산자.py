# num = int(input("구구단을 외자! 17 x 5 = "))
# if num == 17 * 5:
#     print("정답! 똑똑해")
# else:
#     print("실망이야...")

#elif를 배우고 해결해봅시다
# money = int(input("밥 뭐먹지? 돈 얼마있어? : "))
# if money >= 50000:
#     print("소고기 먹으러 가자")
# if money >= 30000:
#     print("돼지고기 먹자")
# if money >= 10000:
#     print("쟈니로켓 먹자")
# else:
#     print("한솥먹자...")

print("오늘도 지각이다... 대중교통을 탈까? 택시를 탈까?")
money = input("택시 탈 돈이 있나[y/n] : ")
if money == 'n':
    print("어쩔수 없지... 대중교통을 타자")
    print("지하철, 버스 뭘 타지?")
    time = input("출근 시간인가[y/n] : ")
    if time == 'y':
        print("지하철 타고 가자")
    else:
        print("버스 타고 가자")
else:
    print("남는게 돈이야 택시타고 얼른가자!")
