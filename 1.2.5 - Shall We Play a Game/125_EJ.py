import turtle as trtl
import random


wn = trtl.Screen()
trtl.write("guessing Game")
trtl.hideturtle()
wn.bgcolor("IndianRed1")


EJ = trtl.Turtle()
EJ.hideturtle()
EJ.penup()
EJ.goto(0, 100)

def write_message(message):
    EJ.write(message, align="center", font=("Arial", 18,))


def hangman():
    word_list = ["alden", "sid", "nehemiah", "tanush", "ej"]
    chosen_word = random.choice(word_list).lower()
    word_length = len(chosen_word)
    EJ.goto(0, 150)
    display = ["_"] * word_length
    lives = 6
    guessed_letters = []


    wn.textinput("start Game", "press OK to start.")

    while True:
      
        guess = wn.textinput("hello bro", f"Word: {"".join(display)} Lives: {lives} guess the letter bro:").lower()

        if not guess:  
            write_message("game over")
            break

        if guess in guessed_letters:
            wn.textinput("dude cmon", f"yo fr? u guessed this already")
            continue

        guessed_letters.append(guess)
        found_letter = False

        for position in range(word_length):
            letter = chosen_word[position]
            if letter == guess:
                display[position] = letter
                found_letter = True
                
        if not found_letter:
            lives -= 1
            wn.textinput("wrong bro", f"'{guess}' is wrong brotato \nLives remaining: {lives}")

       
        write_message(" ".join(display))

        if "_" not in display:
            write_message(f"you got lucky brochacho!  '{chosen_word}'.")
            break
        elif lives == 0:
            write_message(f"bro for real? it was {chosen_word}.")
            break


hangman()
wn.mainloop()
