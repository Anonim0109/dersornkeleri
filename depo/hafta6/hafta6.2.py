import turtle

# Turtle oluşturma
t = turtle.Turtle()
s = turtle.Screen()

# Ekran ve kalem ayarları
s.bgcolor("black")
t.pencolor("red")
t.speed(10)

a = 0
b = 0

t.penup()
t.goto(0, 200)
t.pendown()

while True:
    t.forward(a)
    t.right(b)
    a += 3
    b += 1

    if b == 210:
        break

t.hideturtle()
turtle.done()
input()
