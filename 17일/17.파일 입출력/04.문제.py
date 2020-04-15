#현재 폴더에 movie.txt라는 파일로 올해 본 영화 두 개를 저장
#그 후 작년에 본 영화 두 개를 a를 사용해서 덮어씌워주세요
#잘 저장되었는가 r로 읽어줍시다.

f = open("movie.txt", "w")
for i in range(2):
    movie = input("올해영화 : ")
    f.write(movie + "\n")
f.close()

f = open("movie.txt", "a")
for i in range(2):
    movie = input("작년영화 : ")
    f.write(movie + "\n")
f.close()

f = open("movie.txt", "r")
while True:
    line = f.readline() #파일을 한 줄씩 들고와서 저장
    if line:
        print(line,end="")
    else:
        break
f.close()
