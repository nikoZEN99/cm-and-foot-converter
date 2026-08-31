import turtle
import time
import random

# screen
wn = turtle.Screen()
wn.setup(600, 600)
wn.bgcolor("green")
wn.tracer(0)

# bird
bird = turtle.Turtle()
bird.penup()
bird.speed(0)
bird.shape("square")
bird.goto(-250, 0)

# tube creation
tube_height = 220
half_tube = tube_height / 2
gap_size = 100
tubes = []
def create_pair_of_tubes(x_position):
    gap_center = random.randint(-100, 100)
    tube_y = gap_center - (gap_size / 2) - half_tube
    tube_y_s = gap_center + (gap_size / 2) + half_tube

    tube = turtle.Turtle()
    tube.speed(0)
    tube.color("blue")
    tube.penup()
    tube.goto(x_position, tube_y)
    tube.shape("square")
    tube.shapesize(stretch_wid=11, stretch_len=3)

    tube_s = turtle.Turtle()
    tube_s.speed(0)
    tube_s.color("blue")
    tube_s.penup()
    tube_s.goto(x_position, tube_y_s)
    tube_s.shape("square")
    tube_s.shapesize(stretch_wid=11, stretch_len=3)

    tubes.append([tube, tube_s])

for x in range(1, 30):
    create_pair_of_tubes(x * 300)

# physics
bird_dy = 0
gravity = 0.5
jump_strength = 8

def up():
    global bird_dy
    bird_dy = -jump_strength

# binds
wn.listen()
wn.onkeypress(up, "w")

# game loop
try:
    while True:
        wn.update()

        for pair in tubes:
            top, bottom = pair
            top.setx(top.xcor() - 5)
            bottom.setx(bottom.xcor() - 5)

        bird_dy += gravity
        bird_y = bird.ycor()
        bird.sety(bird_y - bird_dy)

        time.sleep(0.02)

except turtle.Terminator:
    print("Window closed — game ended.")