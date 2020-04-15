import turtle as t
# t.shape("turtle")
# t.bgcolor("black") #배경색
# t.pensize(10)
#
# t.begin_fill() #여기서부터 칠할거야
# t.color("white")
# for i in range(3):
#     t.forward(100)
#     t.left(120)
# t.end_fill() #요기까지 칠할거야

t.shape("triangle")
t.bgcolor("black")
t.color("white")
t.speed(0) #거북이 속도 : 0이 제일 빠름

for i in range(200):
    t.forward(i)
    t.lt(55) #left => lt
input()
