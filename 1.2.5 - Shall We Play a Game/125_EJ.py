import turtle as trtl
import random


trtl.addshape("hanger",((0,0),(0,7),(-6,7),(-6,2),(-5,2),(-5,6),(-1,6),(-1,-6),(-2,-6),(-4,-6),(-4,-7),(5,-7),(5,-6),(0,-6)))
hanger = trtl.Turtle(shape = "hanger")
hanger.color("black")
hanger.setheading(90)
hanger.shapesize(20)

word_list = ["alden", "tanush", "sid", "nehemiah", "sammi"]
chosen_word = random.choice(word_list)
display = ["_"] * len(chosen_word)
lives = 6
guessed_letters = []

estartx = hanger.xcor()
estarty = hanger.ycor()
hanger.setheading(90)
hanger.penup()
hanger.goto(0,100)
estartx = hanger.xcor()
estarty = hanger.ycor()
startx = -100 
starty = -50

trtl.write("Welcome to Hangman!")













# TODO Starting screen with the hanger, letters, and the lines that show how letters  lines there are and where they will go.
# TODO Have a number in the corner that shows how many guesses there is left 
# TODO Have it where it makes a body part everytime they get a guess wrong 
# TODO If they get all the guesses have a winning screen at the end 
# TODO If they don't get all the guesses have a losing screen


















wn = trtl.Screen()
wn.mainloop()