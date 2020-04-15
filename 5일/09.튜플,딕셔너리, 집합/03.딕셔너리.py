people_skill = {"김연아":"피겨", "박지성":"축구", "송진우":"강의","귀도_반_로섬":"파이썬"}
#딕셔너리변수[key] => key옆의 value를 반환
print(people_skill["김연아"])
people_skill["김연아"] = "빵 먹기"
print(people_skill)

#없는 key를 적어주면 추가
people_skill["이승우"] = "축구"
print(people_skill)

#해운대여고 매점 아들내미
mart = {"다이제":800, "메로나":500, "코카콜라":700, "츄파츕스":200}
print("Market O가 다이제를 들고갔어요")
mart["다이제"] = 2500
print(mart)

print("\n===딕셔너리 유의사항===")
#key값은 중복불가능, value는 중복가능
mart = {"다이제":2000, "메로나":500, "다이제":800}
print(mart)
