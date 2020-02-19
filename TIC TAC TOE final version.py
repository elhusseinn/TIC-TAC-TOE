import os
import turtle

win = turtle.Screen()
win.bgcolor("black")
win.setup(width=900, height=600)
win.tracer(0)
pen = turtle.Turtle()
pen.color("white")
pen.hideturtle()
pen.speed(0)
pen.goto(0, 0)
pen.write("For 1 player press \'o\' & for 2 players press\'t\'", align="center", font=("Arial", 30, "normal"))
win.listen()


def startBOT():
    os.system('python BOT.py')


def startPLAYER():
    os.system('python PLAYER.py')


win.onkeypress(startBOT, 'o')
win.onkeypress(startPLAYER, 't')

while True:
    win.update()
