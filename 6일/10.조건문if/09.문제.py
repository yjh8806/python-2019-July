eng_dict = {"money":"돈","variable":"변수","function":"함수","recursive":"반복적인"}
print(list(eng_dict.keys()))
answer = input("영어 단어 입력 : ")

if answer in eng_dict: #dict의 in은 key에서만 찾아본다
    mean = input("영어 단어 뜻 : ")
    if mean == eng_dict[answer]: #eng_dict.get(answer)
        print("정답입니다.")
    else:
        print("오답입니다.")
else:
    print("없는 단어입니다.")
