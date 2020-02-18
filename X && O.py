import turtle

win = turtle.Screen()
win.title("TIC TAC TOE")
win.bgcolor("black")
win.setup(width=1000, height=800)
win.tracer(0)
pen = turtle.Turtle()
pen.speed(0)
pen.goto(0, 350)
pen.color("white")
pen.write("Player \"X\" : 0   Player \"O\" : 0", align="center", font=("Arial", 24, "normal"))
pen.penup()
pen.color("white")
pen.penup()
pen.hideturtle()
pen.penup()
pen.goto(-400, -100)
pen.pendown()
pen.goto(400, -100)
pen.penup()
pen.goto(-400, 100)
pen.pendown()
pen.goto(400, 100)
pen.penup()
pen.goto(-150, 300)
pen.pendown()
pen.goto(-150, -300)
pen.penup()
pen.goto(150, 300)
pen.pendown()
pen.goto(150, -300)
pen.penup()
count_place_9_x = 0
count_place_8_x = 0
count_place_7_x = 0
count_place_6_x = 0
count_place_5_x = 0
count_place_4_x = 0
count_place_3_x = 0
count_place_2_x = 0
count_place_1_x = 0
count_x = 0

count_place_9_o = 0
count_place_8_o = 0
count_place_7_o = 0
count_place_6_o = 0
count_place_5_o = 0
count_place_4_o = 0
count_place_3_o = 0
count_place_2_o = 0
count_place_1_o = 0
count_o = 0

arr = [0, 0, 0, 0, 0, 0, 0, 0, 0]
count = 2


def place_9_x():
    global arr
    global count
    if arr[8] != 'o' and count == 2 and arr[8] != 'x':
        pen.color("white")
        pen.goto(275, 175)
        pen.write("X", align="center", font=("Arial", 50, "normal"))
        pen.penup()
        global count_place_9_x
        count_place_9_x = 1
        arr[8] = 'x'
        count = 3


def place_9_o():
    global arr
    global count
    if arr[8] != 'x' and count == 3 and arr[8] != 'o':
        pen.color("white")
        pen.goto(275, 175)
        pen.write("O", align="center", font=("Arial", 50, "normal"))
        pen.penup()
        global count_place_9_o
        count_place_9_o = 1
        arr[8] = 'o'
        count = 2


def place_8_x():
    global arr
    global count
    if arr[7] != 'o' and count == 2 and arr[7] != 'x':
        pen.color("white")
        pen.goto(0, 175)
        pen.write("X", align="center", font=("Arial", 50, "normal"))
        pen.penup()
        global count_place_8_x
        count_place_8_x = 1
        arr[7] = 'x'
        count = 3


def place_8_o():
    global arr
    global count
    if arr[7] != 'x' and count == 3 and arr[7] != 'o':
        pen.color("white")
        pen.goto(0, 175)
        pen.write("O", align="center", font=("Arial", 50, "normal"))
        pen.penup()
        global count_place_8_o
        count_place_8_o = 1
        arr[7] = 'o'
        count = 2


def place_7_o():
    global arr
    global count
    if arr[6] != 'x' and count == 3 and arr[6] != 'o':
        pen.color("white")
        pen.goto(-275, 175)
        pen.write("O", align="center", font=("Arial", 50, "normal"))
        pen.penup()
        global count_place_7_o
        count_place_7_o = 1
        arr[6] = 'o'
        count = 2


def place_7_x():
    global arr
    global count
    if arr[6] != 'o' and count == 2 and arr[6] != 'x':
        pen.color("white")
        pen.goto(-275, 175)
        pen.write("X", align="center", font=("Arial", 50, "normal"))
        pen.penup()
        global count_place_7_x
        count_place_7_x = 1
        arr[6] = 'x'
        count = 3


def place_6_o():
    global arr
    global count
    if arr[5] != 'x' and count == 3 and arr[5] != 'o':
        pen.color("white")
        pen.goto(275, -25)
        pen.write("O", align="center", font=("Arial", 50, "normal"))
        pen.penup()
        global count_place_6_o
        count_place_6_o = 1
        arr[5] = 'o'
        count = 2


def place_6_x():
    global arr
    global count
    if arr[5] != 'o' and count == 2 and arr[5] != 'x':
        pen.color("white")
        pen.goto(275, -25)
        pen.write("X", align="center", font=("Arial", 50, "normal"))
        pen.penup()
        global count_place_6_x
        count_place_6_x = 1
        arr[5] = 'x'
        count = 3


def place_5_o():
    global arr
    global count
    if arr[4] != 'x' and count == 3 and arr[4] != 'o':
        pen.color("white")
        pen.goto(0, -25)
        pen.write("O", align="center", font=("Arial", 50, "normal"))
        pen.penup()
        global count_place_5_o
        count_place_5_o = 1
        arr[4] = 'o'
        count = 2


def place_5_x():
    global arr
    global count
    if arr[4] != 'o' and count == 2 and arr[4] != 'x':
        pen.color("white")
        pen.goto(0, -25)
        pen.write("X", align="center", font=("Arial", 50, "normal"))
        pen.penup()
        global count_place_5_x
        count_place_5_x = 1
        arr[4] = 'x'
        count = 3


def place_4_o():
    global arr
    global count
    if arr[3] != 'x' and count == 3 and arr[3] != 'o':
        pen.color("white")
        pen.goto(-275, -25)
        pen.write("O", align="center", font=("Arial", 50, "normal"))
        pen.penup()
        global count_place_4_o
        count_place_4_o = 1
        arr[3] = 'o'
        count = 2


def place_4_x():
    global arr
    global count
    if arr[3] != 'o' and count == 2 and arr[3] != 'x':
        pen.color("white")
        pen.goto(-275, -25)
        pen.write("X", align="center", font=("Arial", 50, "normal"))
        pen.penup()
        global count_place_4_x
        count_place_4_x = 1
        arr[3] = 'x'
        count = 3


def place_3_o():
    global arr
    global count
    if arr[2] != 'x' and count == 3 and arr[2] != 'o':
        pen.color("white")
        pen.goto(275, -225)
        pen.write("O", align="center", font=("Arial", 50, "normal"))
        pen.penup()
        global count_place_3_o
        count_place_3_o = 1
        arr[2] = 'o'
        count = 2


def place_3_x():
    global arr
    global count
    if arr[2] != 'o' and count == 2 and arr[2] != 'x':
        pen.color("white")
        pen.goto(275, -225)
        pen.write("X", align="center", font=("Arial", 50, "normal"))
        pen.penup()
        global count_place_3_x
        count_place_3_x = 1
        arr[2] = 'x'
        count = 3


def place_2_o():
    global arr
    global count
    if arr[1] != 'x' and count == 3 and arr[1] != 'o':
        pen.color("white")
        pen.goto(0, -225)
        pen.write("O", align="center", font=("Arial", 50, "normal"))
        pen.penup()
        global count_place_2_o
        count_place_2_o = 1
        arr[1] = 'o'
        count = 2


def place_2_x():
    global arr
    global count
    if arr[1] != 'o' and count == 2 and arr[1] != 'x':
        pen.color("white")
        pen.goto(0, -225)
        pen.write("X", align="center", font=("Arial", 50, "normal"))
        pen.penup()
        global count_place_2_x
        count_place_2_x = 1
        arr[1] = 'x'
        count = 3


def place_1_o():
    global arr
    global count
    if arr[0] != 'x' and count == 3 and arr[0] != 'o':
        pen.color("white")
        pen.goto(-275, -225)
        pen.write("O", align="center", font=("Arial", 50, "normal"))
        pen.penup()
        global count_place_1_o
        count_place_1_o = 1
        arr[0] = 'o'
        count = 2


def place_1_x():
    global arr
    global count
    if arr[0] != 'o' and count == 2 and arr[0] != 'x':
        pen.color("white")
        pen.goto(-275, -225)
        pen.write("X", align="center", font=("Arial", 50, "normal"))
        pen.penup()
        global count_place_1_x
        count_place_1_x = 1
        arr[0] = 'x'
        count = 3


def clear_screen():
    win.reset()
    win.bgcolor("black")
    pen.color("white")
    pen.hideturtle()
    pen.penup()
    pen.goto(0, 350)
    pen.color("white")
    pen.write("Player \"X\" : 0   Player \"O\" : 0", align="center", font=("Arial", 24, "normal"))
    pen.penup()
    pen.goto(-400, -100)
    pen.pendown()
    pen.goto(400, -100)
    pen.penup()
    pen.goto(-400, 100)
    pen.pendown()
    pen.goto(400, 100)
    pen.penup()
    pen.goto(-150, 300)
    pen.pendown()
    pen.goto(-150, -300)
    pen.penup()
    pen.goto(150, 300)
    pen.pendown()
    pen.goto(150, -300)
    pen.penup()

    global count_place_1_o
    global count_place_1_x
    global count_place_2_o
    global count_place_2_x
    global count_place_3_o
    global count_place_3_x

    global count_place_4_o
    global count_place_4_x
    global count_place_5_o
    global count_place_5_x
    global count_place_6_o
    global count_place_6_x

    global count_place_7_o
    global count_place_7_x
    global count_place_8_o
    global count_place_8_x
    global count_place_9_o
    global count_place_9_x
    global arr

    count_place_9_x = 0
    count_place_8_x = 0
    count_place_7_x = 0
    count_place_6_x = 0
    count_place_5_x = 0
    count_place_4_x = 0
    count_place_3_x = 0
    count_place_2_x = 0
    count_place_1_x = 0

    count_place_9_o = 0
    count_place_8_o = 0
    count_place_7_o = 0
    count_place_6_o = 0
    count_place_5_o = 0
    count_place_4_o = 0
    count_place_3_o = 0
    count_place_2_o = 0
    count_place_1_o = 0
    arr = [0, 0, 0, 0, 0, 0, 0, 0, 0]


win.listen()
win.onkeypress(place_9_x, "9")
win.onkeypress(place_8_x, "8")
win.onkeypress(place_7_x, "7")
win.onkeypress(place_6_x, "6")
win.onkeypress(place_5_x, "5")
win.onkeypress(place_4_x, "4")
win.onkeypress(place_3_x, "3")
win.onkeypress(place_2_x, "2")
win.onkeypress(place_1_x, "1")
win.onkeypress(place_9_o, "F9")
win.onkeypress(place_8_o, "F8")
win.onkeypress(place_7_o, "F7")
win.onkeypress(place_6_o, "F6")
win.onkeypress(place_5_o, "F5")
win.onkeypress(place_3_o, "F3")
win.onkeypress(place_4_o, "F4")
win.onkeypress(place_2_o, "F2")
win.onkeypress(place_1_o, "F1")
win.onkeypress(clear_screen, "c")

while True:
    win.update()
    count_sum = count_place_1_x + count_place_1_o + count_place_2_x + count_place_2_o + count_place_3_x + count_place_3_o + count_place_4_x + count_place_4_o + count_place_5_x + count_place_5_o + count_place_6_x + count_place_6_o + count_place_7_x + count_place_7_o + count_place_8_x + count_place_8_o + count_place_9_x + count_place_9_o

    if count_place_9_x + count_place_6_x + count_place_3_x == 3 or count_place_8_x + count_place_5_x + count_place_2_x == 3 or count_place_7_x + count_place_4_x + count_place_1_x == 3 or count_place_9_x + count_place_7_x + count_place_8_x == 3 or count_place_4_x + count_place_6_x + count_place_5_x == 3 or count_place_1_x + count_place_2_x + count_place_3_x == 3 or count_place_9_x + count_place_5_x + count_place_1_x == 3 or count_place_7_x + count_place_5_x + count_place_3_x == 3:
        pen.goto(0, 0)
        pen.write("PLAYER \"X\" WINS", align="center", font=("Arial", 50, "normal"))
        pen.penup()
        arr = ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x']

    elif count_place_9_o + count_place_6_o + count_place_3_o == 3 or count_place_8_o + count_place_5_o + count_place_2_o == 3 or count_place_7_o + count_place_4_o + count_place_1_o == 3 or count_place_9_o + count_place_7_o + count_place_8_o == 3 or count_place_4_o + count_place_6_o + count_place_5_o == 3 or count_place_1_o + count_place_2_o + count_place_3_o == 3 or count_place_9_o + count_place_5_o + count_place_1_o == 3 or count_place_7_o + count_place_5_o + count_place_3_o == 3:
        pen.goto(0, 0)
        pen.write("PLAYER \"O\" WINS", align="center", font=("Arial", 50, "normal"))
        arr = ['o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o']

    else:
        if count_sum == 9:
            pen.goto(0, 0)
            pen.color("green")
            pen.write("\"DRAW\"", align="center", font=("Arial", 50, "normal"))
