#원의 반지름을 입력받고 원의 넓이를 구하시오
#반지름 * 반지름 * pi
from math import pi
r = int(input("원의 반지름 : "))
print("%.2f"%(r*r*pi))
print("%.2f"%(r**2*pi))
