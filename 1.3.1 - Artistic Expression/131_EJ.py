import turtle as trtl

#Screen setup
wn = trtl.Screen()
wn.setup(width=800, height =600)
wn.bgpic("bg.gif")
wn.bgpic()
wn.title("Veteran Letter")
wn.addshape("envv.gif")



#Setup envelope
setup = trtl.Turtle(shape= "envv.gif")
setup.shapesize()

wn.mainloop()