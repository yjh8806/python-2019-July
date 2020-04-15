import turtle as t
import random as r

t.shape("turtle")
t.speed(0)

color = ["blue", "green", "yellow", "red", "black", "pink"]

for i in range(500):
    if i % 2 == 0:
        t.color(r.choice(color))
        t.pensize(r.randint(1, 10))
        t.lt(r.randint(30, 120))
    t.rt(r.randint(30, 120))
    t.fd(r.randint(1, 20))
    t.onscreenclick(t.goto) #스크린을 클릭한 곳으로 거북이 이동
input()
