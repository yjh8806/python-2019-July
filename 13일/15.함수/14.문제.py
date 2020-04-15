def data_unit(d, u):
    ex = ["T","G","M","K"]
    if u not in ex:
        print("잘못된 입력입니다.")
        return -1 #잘못된 입력시 -1을 반환
    elif u == "T":
        return d * 1024 * 1024 * 1024 * 1024
    elif u == "G":
        return d * 1024 * 1024 * 1024
    elif u == "M":
        return d * 1024 * 1024
    elif u == "K":
        return d * 1024

data, unit = input("용량 입력(k, m, g, t) : ").split()
data = int(data)
unit = unit.upper() #전부 다 대문자
#고급포매팅 {:,d} : 1000단위 구분기호
print("출력 : {:,d} {} => {:,d} byte입니다.".format(data,unit,data_unit(data,unit)))
