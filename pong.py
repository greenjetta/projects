import turtle
from playsound import playsound


# setting the scene
wn = turtle.Screen()
wn.title("Pong Game")
wn.bgcolor("blue")
wn.setup(width=800, height=600)
wn.tracer()

# paddle a
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.penup()
paddle_a.goto(-350, 0)
paddle_a.shapesize(stretch_wid=5, stretch_len=1)

#paddle b
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("red")
paddle_b.penup()
paddle_b.goto(350, 0)
paddle_b.shapesize(stretch_wid=5, stretch_len=1)

#ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("black")
ball.penup()
ball.goto(0, 0)
ball.dx = 5
ball.dy = -5



# functions
def paddle_a_up():
    y = paddle_a.ycor()
    y += 35
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    y -= 35
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()
    y += 35
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y -= 35
    paddle_b.sety(y)



#keyboard binding
wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")


# pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write(f"Player A: 0  Player B: 0", align="center", font=("courier", 24, "normal"))

# score
player_a_score = 0
player_b_score = 0


# game loop
while True:
    wn.update()

    # move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    #music


    
    # border checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
    
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
    if ball.xcor() > 390:
        ball.goto(0,0)
        ball.dx *= -1
        player_a_score += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(player_a_score, player_b_score), align="center", font=("courier", 24, "normal"))
    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(player_a_score, player_b_score), align="center", font=("courier", 24, "normal"))
        player_b_score += 1
    
    
    # paddle and ball collisions
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() - 40):
        ball.dx *= -1
        ball.setx(340)
    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() - 40):
        ball.dx *= -1
        ball.setx(-340)