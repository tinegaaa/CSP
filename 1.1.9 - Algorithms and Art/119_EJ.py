import turtle as trtl

#create custom turtle
trtl.addshape("e", ((0,0),(0,3),(-4,3),(-4,7),(1,7),(1,10),(-7,10),(-7,-7),(1,-7),(1,-4),(-4,-4),(-4,0)))
trtl.addshape("football", ((5,0),(5,3),(4,5),(3,7),(1,9),(0,9),(-1,9),(-3,7),(-4,5),(-5,3),(-5,0),(-5,-3),(-4,-5),(-3,-7),(-1,-9),(0,-9),(1,-9),(3,-7),(4,-5),(5,-3)))
#Add the O-Linemen and B-back
turtle_shapes = ["square", "square", "circle", "square", "square", "e","football"]

#Add the football
fb = trtl.Turtle(shape = "football")
fb.setheading(90)
startx = -100 
starty = 0

line = []
for i in range(5):
    var = ("lineman" + str(i))
    if i == 2: 
        tshape = "circle"
    else:
        tshape = "square"

    var = trtl.Turtle(shape = tshape)
    var.penup()
    var.goto(startx, starty)
    startx += 50
    line.append(var)
print(line)



#Add the question for which play to run
#dive = trtl.textinput("Chose Play","12 or 13?")
#if dive == "12":
 
 
 

#Have the linemen block down
#Have the B-back run thru the gap with the ball
wn = trtl.Screen()
wn.mainloop()