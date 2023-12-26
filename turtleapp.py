from turtle import *
pensize(4)
w = Screen()
w.setup(1000,1000)

def sagadon():
    rt(90)
def soladon():
    lt(90)
def duzgit():
    fd(200)
w.onkeypress(sagadon, "Right")
w.onkeypress(soladon, "Left")
w.onkeypress(duzgit, "Up")

listen()
mainloop()