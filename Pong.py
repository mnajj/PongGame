# Import Modules
import turtle

# [1] Bulding Game screen
window = turtle.Screen()
window.title("Ping Pong")
window.bgcolor("darkslategray")
window.setup(width=800, height=600)
window.tracer(0)   # Stop Window from Screen Updating Rate

# [2] Game Objects
# paddle1
paddle1 = turtle.Turtle()
paddle1.speed(0)
paddle1.shape("square")
paddle1.shapesize(stretch_wid= 5, stretch_len= 1)
paddle1.color("blue")
paddle1.penup()
paddle1.goto(-350, 0)

# paddle2
paddle2 = turtle.Turtle()
paddle2.speed(0)
paddle2.shape("square")
paddle2.shapesize(stretch_wid= 5, stretch_len= 1)
paddle2.color("red")
paddle2.penup()
paddle2.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)

# Score object
score1 = 0
score2 = 0
score = turtle.Turtle()
score.speed(0)
score.color("white")
score.penup()
score.hideturtle()
score.goto(0, 260)
score.write(f"Player #1: {score1}  ||  Player #2: {score2}", align= "center", font=("courir", 20, "normal"))

# Ball Movement
# start at zero and move +0.07 every time loop run
ball.dx = 0.07  
ball.dy = 0.07

# [3] paddles Movement
# ------ [UP] -------
def paddle1_up():
    y = paddle1.ycor()   
    y += 20                        
    paddle1.sety(y)   

def paddle2_up():
    y = paddle2.ycor()   
    y += 20                        
    paddle2.sety(y)   

# ------ [Down] -------
def paddle1_down():
    y = paddle1.ycor()   
    y -= 20                        
    paddle1.sety(y)   

def paddle2_down():
    y = paddle2.ycor()   
    y -= 20                        
    paddle2.sety(y)   

# Keyboard Bindings
# Get inputs
window.listen()

# Call Functions
window.onkeypress(paddle1_up, "w")
window.onkeypress(paddle1_down, "s")

window.onkeypress(paddle2_up, "Up")
window.onkeypress(paddle2_down, "Down")


# Main Game Loop
while True:
    window.update()   # Updates screen every time loop runs

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border Check
    # --- Top Border | +300 px | ball is 20px ---
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1 

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    # --- Bottom Border | -300 px | ball is 20px ---
    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score.clear()
        score1 += 1
        score.write(f"Player #1: {score1}  ||  Player #2: {score2}", align= "center", font=("courir", 20, "normal"))


    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score.clear()
        score2 += 1
        score.write(f"Player #1: {score1}  ||  Player #2: {score2}", align= "center", font=("courir", 20, "normal"))


    # Ball Crash
    #paddel 2
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle2.ycor() + 40 and ball.ycor() > paddle2.ycor() - 40):
        ball.setx(340)
        ball.dx *= -1
    #paddel 1
    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle1.ycor() + 40 and ball.ycor() > paddle1.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1
