import turtle
import random

# Ekran oluşturma
screen = turtle.Screen()
screen.title("Rastgele Şekiller")
screen.bgcolor("white")

# Turtle oluşturma
pen = turtle.Turtle()
pen.speed(0)
pen.width(2)

# Renk listesi
colors = ["red", "blue", "green", "orange", "purple", "pink", "yellow"]

# Rastgele şekiller çizme fonksiyonu
def draw_random_shape():
    sides = random.randint(3, 8)  # 3 ile 8 arasında rastgele kenar sayısı seçme
    length = random.randint(50, 150)  # Kenar uzunluğunu rastgele seçme

    pen.color(random.choice(colors))  # Rastgele bir renk seçme

    # Belirlenen kenar sayısına göre şekli çizme
    for _ in range(sides):
        pen.forward(length)
        pen.right(360 / sides)

# Rastgele şekilleri çizme
for _ in range(10):  # 10 adet rastgele şekil çizme
    x = random.randint(-200, 200)  # X koordinatını rastgele belirleme
    y = random.randint(-200, 200)  # Y koordinatını rastgele belirleme

    pen.penup()
    pen.goto(x, y)
    pen.pendown()

    draw_random_shape()

# Çizimi ekranda tutmak için bekleme
turtle.done()
