count = [0, 1, 2, 3]

for num in count:
    print("num = %d"%num)

count = ["one", "two", "three", "four", "five"]

for i in count:
    print(i)

#interable => 반복가능객체 => list, tuple, dict
# num = 10
# for i in num:
#     print(i)

#튜플
jumsu = (90, 50, 60, 80, 40)
number = 1
for i in jumsu:
    if i >= 60:
        print("%d번째 학생 : 합격"%number)
    else:
        print("%d번째 학생 : 불합격"%number)
    number += 1

people = {"송새봄":29, "송여름":16, "송가을":32, "송겨울":5}
minor = []
adult = []
#dict는 key만 들고온다!
for i in people:
    if people[i] < 20:
        print("%s님 : %d살 ==> 미성년자"%(i, people[i]))
        minor.append(i)
    else:
        print("%s님 : %d살 ==> 성인"%(i, people[i]))
        adult.append(i)
print("성인 : %s"%adult)
print("미성년자 : %s"%minor)
