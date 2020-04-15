import time

print(time.time()) #현재 시간을 초단위로 반환하는 함수
print(time.localtime(time.time())) #초에 단위를 붙여줌

# time.sleep(3)
# print("이것이 슬립이다.")

print("\n===스톱워치 만들기===")
input("엔터를 누르고 3초를 마음속으로 세시오")
start = time.time() #시작시간 저장

input("3초가 되면 다시 엔터를 누르세요")
end = time.time() #끝나는 시간 저장

result = end - start

print("걸린시간 : %.2f"%result)
print("오차 : %.2f"%abs(result - 3))
