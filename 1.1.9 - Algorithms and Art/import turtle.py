import turtle
import random

def turtle_celebration():
    screen = turtle.Screen()
    screen.bgcolor("lightblue")
    screen.title("Simple Celebration!")

    t = turtle.Turtle()
    t.speed(0) # Fastest speed

    colors = ["red", "orange", "yellow", "green", "blue", "purple"]

    for _ in range(30):
        t.color(random.choice(colors))
        t.circle(random.randint(20, 100))
        t.penup()
        t.goto(random.randint(-200, 200), random.randint(-200, 200))
        t.pendown()
    
    t.hideturtle()
    screen.exitonclick()

# turtle_celebration() # Uncomment to run the turtle graphics