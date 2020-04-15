#elif : else if => 그 밖에 만약에... => if가 거짓말이면 와서 물어본다
money = int(input("밥 뭐먹지? 돈 얼마있어? : "))
if money >= 50000:
    print("소고기 먹으러 가자")
elif money >= 30000:
    print("돼지고기 먹자")
elif money >= 10000:
    print("쟈니로켓 먹자")
else:
    print("한솥먹자...")
