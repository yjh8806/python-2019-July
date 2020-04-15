def find_word(word): #word = word_dict
    for i in range(len(word)):
        search = input("찾는 단어 입력 : ")
        if search in word:
            print(search, " : ", word[search])
        else:
            print("없는 단어입니다.")

word_dict = {"apple":"사과", "banana":"바나나", "cat":"고양이"}
find_word(word_dict)#딕셔너리를 전달
