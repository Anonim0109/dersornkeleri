import turtle as n
import random
j=0
def cizbakalim (r, ycap, x, y):
    n. penup()
    n.goto (x, y)
    n.pendown()
    n.fillcolor (r)
    n.begin_fill()
    n.circle (ycap)
    n.end_fill()
renk=["green", "red", "yellow", "blue", "purple"]
ycap=15

for i in range (-30, 120, 30):
    cizbakalim (renk [j], ycap, i, 0)
    j=random.randint (0, 4)
for i in range (90,-60, -30):
    cizbakalim (renk [j], ycap, i, 30)
    j=random.randint (0,4)
input() 

