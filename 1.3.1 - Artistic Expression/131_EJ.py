import turtle as trtl

#Screen setup
wn = trtl.Screen()
wn.setup(width=800, height =600)
wn.bgpic("bg.gif")
wn.bgpic()
wn.title("Veteran Letter")

wn.tracer(0)
wn.tracer(1)

trtl.addshape("envv.gif")
trtl.addshape("open_envv.gif")
trtl.addshape("airforce.gif")
trtl.addshape("spaceforce.gif")
trtl.addshape("coastguard.gif")
trtl.addshape("army.gif")
trtl.addshape("marine.gif")
trtl.addshape("navy.gif")
branch_images = ["marine.gif", "navy.gif", "army.gif", "airforce.gif", "coastguard.gif", "spaceforce.gif"]
emblems = []

#Setup envelope
envelope = trtl.Turtle(shape= "envv.gif")

def branch_click(x,y,emblems):
   print("Hello")
   print(str(emblems))
   wn.clearscreen()
   wn.bgcolor("waterbg.gif")
   

def open_envelope(x,y):
    print("en_clicked")
    envelope.shape("open_envv.gif")
    user_message = wn.textinput("Name", "Whats your name?")

    if user_message:
        writer = trtl.Turtle()
        writer.hideturtle()
        writer.penup()
        writer.goto(-395, 140)
        writer.write(f"Thank you for your service, {user_message}!", font=("Airborne 86", 40, "bold"))
        writer.hideturtle()
        writer.penup()
        writer.goto(-395,70)
        writer.write("Choose a branch...", font =("Airborne 86", 40, "bold"))

        positions = [(-270, -100), (-150, -150), (-30, -100), (70, -150), (170, -100), (270, -150)]     

        index = 0
        
        for i in branch_images:
            emblem = trtl.Turtle(shape=branch_images[index])
            emblems.append(emblem)
            emblem.penup()
            emblem.goto(positions[index])
            emblem.onclick(branch_click)
            
            trtl.onclick(lambda x,y: branch_click(emblems[index-1]))
            index +=1
            
for letter in "mnafcs":
    wn.onkeypress(lambda l=letter: branch_click(l), letter)   

#wn.onkeypress(branch_click("a"))
envelope.onclick(open_envelope)
wn.listen()
wn.mainloop()