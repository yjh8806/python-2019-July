#dict{key:value}
me = {"name":"jinwoo", "phone":"010-5567-1430", "birth":"901129"}
print(me)

print("\n===딕셔너리 생성/추가===")
mart = {"다이제" : 2000}
print(mart)

#앞에서 사용한 모든 자료형이 [인덱스]
#딕셔너리는 [key]
#딕셔너리변수[key] = value
mart["밀키스"] = 1000
print(mart)

#이미 있는 key를 적어주시면 value가 수정됩니다.
mart["다이제"] = 2500
print(mart)

print("\n===딕셔너리 요소 추가===")
mart["츄파츕스"] = 200
mart[999] = "999"
mart["우바이봉"] = [200, 300]
#value에는 자료형이 상관없고
#key에는 단일 자료형이 저장되어야 된다.
# mart[["초코맛 우마이봉", "콘스프맛 우마이봉"]] = [200, 300]
print(mart)

print("\n===딕셔너리 요소 삭제===")
del mart["다이제"]
print(mart)
