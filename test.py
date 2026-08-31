import turtle

# --- Setup screen ---
screen = turtle.Screen()
screen.title("Rotating Arrow")
screen.setup(width=600, height=600)
screen.tracer(0)  # manual screen updates for smoother redraw

# --- Arrow turtle ---
arrow = turtle.Turtle()
arrow.shape("arrow")
arrow.shapesize(3)
arrow.color("cyan")
arrow.penup()
arrow.goto(0, 0)
arrow.setheading(0)

# --- Text turtle (shows degree at top of screen) ---
label = turtle.Turtle()
label.hideturtle()
label.penup()
label.color("white")
label.goto(0, 250)

angle = 0  # current heading in degrees


def update_label():
    label.clear()
    label.write(f"{angle}°", align="center", font=("Arial", 24, "bold"))


def turn_left():
    global angle
    angle = (angle + 15) % 360
    arrow.setheading(angle)
    update_label()
    screen.update()


def turn_right():
    global angle
    angle = (angle - 15) % 360
    arrow.setheading(angle)
    update_label()
    screen.update()


update_label()
screen.update()

screen.bgcolor("black")
screen.listen()
screen.onkey(turn_left, "a")
screen.onkey(turn_right, "d")

screen.mainloop()