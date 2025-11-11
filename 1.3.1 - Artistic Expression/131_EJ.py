import turtle as trtl

#Screen setup
wn = trtl.Screen()
wn.setup(width=800, height =600)
wn.bgcolor("lightgrey")
wn.title("Veteran Letter")

setup = trtl.Turtle()
setup.pendown()
setup.goto(300,200)

wn.mainloop()