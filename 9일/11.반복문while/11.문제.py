import random #choice()를 사용하기 위한 모듈
print("===랜덤 단어 맞추기 게임===")
wordlist = ["itbank", "hello", "python", "dog"]
#random.choice(list, tuple, dict)
print(random.choice(wordlist))
while wordlist: #wordlist가 비어있지 않으면 반복
    print(wordlist)
    answer = random.choice(wordlist)
    print(answer[0])
    answer_input = input("단어 입력 : ")
    if answer == answer_input:
        print("정답입니다!")
        wordlist.remove(answer)
    else:
        print("오답입니다.")
print("★모두 맞췄습니다★")
