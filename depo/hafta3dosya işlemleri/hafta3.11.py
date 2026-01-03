import turtle
import time
turtle.hideturtle()

# Ekran ayarları
ekran = turtle.Screen()
ekran.bgcolor("black")
ekran.title("Mükemmel Python Uygulaması")

# Turtle ayarları
kalp = turtle.Turtle()
kalp.color("red")
kalp.pensize(3)
kalp.speed(3)

# Kalp çizme fonksiyonu
def ciz_kalp():
    kalp.begin_fill()
    kalp.left(50)
    kalp.forward(100)
    kalp.circle(50, 200)
    kalp.right(140)
    kalp.circle(50, 200)
    kalp.forward(100)
    kalp.end_fill()

# Kalbi çiz
ciz_kalp()

# Mesaj yaz
kalp.penup()
kalp.goto(0, -10)
kalp.color("white")
kalp.write("DEĞERLİ BİRİSİN!", align="center", font=("Arial", 16, "bold"))

# 5 saniye bekle
time.sleep(10)

# Ekranı kapat
turtle.bye()
