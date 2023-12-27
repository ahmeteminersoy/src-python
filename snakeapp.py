import turtle
import time
import random

sleepidx = 0.1
score = 0
maxScore = 0
L = []

# screen settings
w = turtle.Screen()
w.title("Snake Game")
w.setup(600, 600)
w.bgcolor(0.6, 0.7, 0.17)
w.tracer(0)

# snake's head
sk = turtle.Turtle()
sk.speed(0)
sk.shape("circle")
sk.color(0.2, 0.4 , 0.1)
sk.penup()
sk.goto(0, 0)

sk.direction = "stop"


def move():
    if sk.direction == "up":
        y = sk.ycor()
        sk.sety(y + 20)
    if sk.direction == "down":
        y = sk.ycor()
        sk.sety(y - 20)
    if sk.direction == "right":
        x = sk.xcor()  
        sk.setx(x + 20)
    if sk.direction == "left":
        x = sk.xcor()  
        sk.setx(x - 20)

def goUp():
    if sk.direction != "down":
        sk.direction = "up"


def goDown():
    if sk.direction != "up":
        sk.direction = "down"


def goRight():
    if sk.direction != "left":
        sk.direction = "right"


def goLeft():
    if sk.direction != "right":
        sk.direction = "left"


w.listen()
w.onkeypress(goUp, "Up")
w.onkeypress(goDown, "Down")
w.onkeypress(goRight, "Right")
w.onkeypress(goLeft, "Left")


food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("brown")
food.penup()
food.goto(random.randint(0, 100), 100)


def eat():
    if sk.distance(food) < 20:
        x = random.randint(-280, 280)
        y = random.randint(-280, 280)
        food.goto(x, y)
        global sleepidx
        sleepidx *= 0.96 

        tail = turtle.Turtle()
        tail.speed(0)
        tail.shape("circle")
        tail.color("white")
        tail.penup()
        L.append(tail)
        global score
        global maxScore
        score += 5  
        if score > maxScore: 
            maxScore = score
        w.title("Score: {}, The Max Score: {}".format(score, maxScore))

    tailLength = len(L)
    for idx in range(tailLength - 1, 0, -1):
        x = L[idx - 1].xcor()
        y = L[idx - 1].ycor()
        L[idx].goto(x, y)

    if len(L) > 0:
        x = sk.xcor()
        y = sk.ycor()
        L[0].goto(x, y)


def start():
    time.sleep(0.1)
    global sleepidx
    sleepidx = 0.1
    sk.goto(0, 0)
    sk.direction = "stop"
    for link in L:
        link.goto(1000, 1000)
    L.clear()
    global score
    score = 0
    w.title("Score: {} Highest Score {}".format(score, maxScore))


while True:
    w.update()
    eat()
    move()

    if (sk.xcor() > 290 or sk.xcor() < -290 or sk.ycor() > 290 or sk.ycor() < -290):
        start()

    for link in L:
        if link.distance(sk) < 20:
            start()

    time.sleep(sleepidx) 

w.mainloop()