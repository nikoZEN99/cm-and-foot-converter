import turtle
import time
import random

# screen
wn = turtle.Screen()
wn.bgcolor("green")
wn.setup(600, 600)

# head
head = turtle.Turtle()
head.shape("square")
head.shapesize(stretch_wid=5, stretch_len=1)
head.penup()
head.goto(-285, 0)
head.speed(0)

# ball
ball = turtle.Turtle()
ball.shape("arrow")
ball.color("red")
ball.penup()
# pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)

# Functions and bounds
def up():
    y = head.ycor()
    if y < 245:
        head.sety(y + 20)

def down():
    y = head.ycor()
    if y > -245:
        head.sety(y - 20)

# binds
wn.listen()
wn.onkeypress(up, "w")
wn.onkeypress(down, "s")
# score
score = 0

# ball loop
ball_speed = 3
try:
    while True:
        wn.update()
        ball.forward(ball_speed)

        head_y = head.ycor()
        ball_y = ball.ycor()
        ball_x = ball.xcor()

        if ball_x < -268 and head_y - 50 < ball_y and head_y + 50 > ball_y:
            ball.setx(-268)
            new_angle = random.randint(-45, 30)
            ball.setheading(new_angle)
            ball_speed += 0.3
            score += 1
            right = 1
        while ball_x < -280:
            pen.write("Score: {}".format(score), align="center", font=("Courier", 24, "normal"))
        if ball_y > 299 and right == 1:
            ball.setheading(random.randint(315, 345))
            ball.sety(290)
        if ball_y > 299 and right == 0:
                    ball.setheading(random.randint(195, 225))
                    ball.sety(290)
        if ball_y < -299 and right == 1:
            ball.setheading(random.randint(30, 60))
            ball.sety(-290)
        if ball_y < -299 and right == 0:
                    ball.setheading(random.randint(135, 165))
                    ball.sety(-290)
        if ball_x > 268:
            ball.setx(268)
            ball.setheading(random.randint(160, 200))  
            right = 0
except turtle.Terminator:
    print("Window closed — game ended.")

    

    

    
    
