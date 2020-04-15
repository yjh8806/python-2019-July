#w => write : 없는 문서는 만들어줄거야
#현재 파이썬 파일이 있는 폴더에 넣어줄거야
f = open("new.txt", "w")
f.write("배가 고파요")
f.close() #열고나면 닫아줘야되요

#이미 있는 파일은 덮어씌워줄거야
f = open("new.txt", "w")
f.write("피자")
f.close()

f = open("D:\\8월 평일 파이썬 송진우\\student.txt","w")

for i in range(1, 5 + 1):
    name = input("%d번째 학생이름 : " %i)
    data = "%d번째 : %s\n"%(i, name)
    f.write(data)
f.close()

#with를 사용하면 자동으로 close해줍니다.
with open("D:\\8월 평일 파이썬 송진우\\student.txt","w") as f:
    f.write("with연습")
