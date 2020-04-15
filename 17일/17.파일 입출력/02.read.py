#r => read
f = open("D:\\8월 평일 파이썬 송진우\\student.txt", "r")
while True:
    line = f.readline() #파일을 한 줄씩 들고와서 저장
    if line:
        print(line,end="")
    else:
        break
f.close()
