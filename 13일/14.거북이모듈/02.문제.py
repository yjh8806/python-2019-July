import turtle as t
import math #수학모듈
#math.sqrt(16) => 4

t.shape("turtle")
for i in range(4):
    t.forward(100)
    t.right(90)
t.circle(-50)
t.right(90)
t.forward(100)
t.left(135)
t.forward(50 * math.sqrt(2))
t.right(90)
t.forward(50 * math.sqrt(2))

input()
