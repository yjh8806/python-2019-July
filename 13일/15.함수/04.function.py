import turtle as t

def move_right():
    t.setheading(0) #거북이의 머리 방향의 각도를 결정
    t.fd(5) #forward의 약자
def move_up():
    t.setheading(90)
    t.fd(5)
def move_left():
    t.setheading(180)
    t.fd(5)
def move_down():
    t.setheading(270)
    t.fd(5)
def circle():
    t.circle(50)
def triangle():
    for i in range(3):
        t.lt(120)
        t.fd(100)
def square():
    for i in range(4):
        t.lt(90)
        t.fd(100)

t.shape("turtle")
t.speed(0)
t.onkeypress(move_up,"Up")
t.onkeypress(move_down,"Down")
t.onkeypress(move_right,"Right")
t.onkeypress(move_left,"Left")
t.onkeypress(circle,"c")
t.onkeypress(triangle,"t")
t.onkeypress(square,"s")
t.listen()
t.mainloop()
input()
