parking_time = int(input("주차한 시간 입력 : "))
parking_fee = 1000
if parking_time >= 0 and parking_time <= 30:
    print("주차요금은 %d원 입니다."%parking_fee)
elif parking_time > 30:
    parking_time -= 30 #추가시간
    if parking_time % 10 == 0:
        parking_fee += (parking_time // 10) * 500
    else:
        parking_fee += (parking_time // 10) * 500 + 500 #500원을 수동으로 더해주시면 됩니다.
    print("주차요금은 %d원 입니다."%parking_fee)
else:
    print("시간을 잘 못 입력했습니다.")
