#밖의 반복문이 한번 반복할때 안의 반복문이 처음부터 끝까지 반복
#i, j : index의 i j는 알파벳 순서상으로 i뒤에 글자
for i in range(3):
    print("====={0}학년=====".format(i + 1))
    for j in range(5):
        print("---{0}학년--{1}반---".format(i + 1, j + 1))
    print()#엔터키

print("\n===이중 for로 구구단 만들기===")
for i in range(2, 10):
    for j in range(1, 10):
        print("%d x %d = %d"%(i, j, i * j))
    print()
