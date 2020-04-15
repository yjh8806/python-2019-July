#계산기를 만들건데 값을 따로 저장할 열개의 계산기(값이 누적되야되요)

result1 = 0
result2 = 0
result3 = 0
def calc1(num):
    global result1
    result1 += num
def calc2(num):
    global result2
    result2 += num
def calc3(num):
    global result3
    result3 += num
calc1(3)
calc1(3)
print(result1)
calc2(5)
calc3(7)
