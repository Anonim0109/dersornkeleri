import turtle as t, random as r

uzunluk=r.randint(-300,300)
kenarsayisi = r.randint(3,8)
t.up()
t.goto(r.randint(-300,300),r.randint(-300,300))
t.down()
for a in range(kenarsayisi):
    t.forward(uzunluk)
    t.right(360/kenarsayisi)

input()