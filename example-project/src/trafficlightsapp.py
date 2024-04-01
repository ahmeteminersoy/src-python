from turtle import *
import time
w = Screen()
w.setup(300, 700)
w.title("Traffic Lights")

penup()
goto(0, 180)
pendown()
pensize(4)
for i in range(2):
    fd(80)
    rt(90)
    fd(220)
    rt(90)
def red():
    penup()
    goto(40, 140)
    fillcolor("red")
    shape("circle")
    shapesize(3)

def green():
    penup()
    goto(40, 0)
    fillcolor("green")
    shape("circle")
    shapesize(3)

def yellow():
    penup()
    goto(40, 70)
    fillcolor("yellow")
    shape("circle")
    shapesize(3)
while True:
    green()
    time.sleep(9)
    yellow()
    time.sleep(3)
    red()
    time.sleep(5)
w.mainloop()