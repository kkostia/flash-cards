from tkinter import *
from csv import *
from random import *

BACKGROUND_COLOR = "#B1DDC6"

# Pickinjg random word from data
def pick_word():
    with open("data/french_words.csv", "r") as f:
        list_of_words = list(reader(f))
        random_word = choice(list_of_words)
        french_word = random_word[0]
        english_word = random_word[1]
        print(french_word)
        print(english_word)


# UI setup
window = Tk()
window.title("Flash Cards")
window.geometry("900x800")
window.config(bg=BACKGROUND_COLOR)

# Configure grid layout
window.columnconfigure(0, weight=1)
window.columnconfigure(1, weight=1)
window.rowconfigure(0, weight=1)
window.rowconfigure(1, weight=1)
window.rowconfigure(2, weight=1)

# Correct file paths (Use double backslashes `\\` or raw strings `r""`)
card_front_img = PhotoImage(file=r"images\card_front.png")
right_img = PhotoImage(file=r"images\right.png")
wrong_img = PhotoImage(file=r"images\wrong.png")

# Whiteboard (Canvas) with image
whiteboard = Canvas(window, width=800, height=526, highlightthickness=0)
whiteboard.create_image(400, 263, image=card_front_img)
whiteboard.grid(row=0, column=0, columnspan=2, padx=50, pady=50)

# Labels inside the canvas
whiteboard.create_text(400, 150, text="Title", font=("Arial", 40, "italic"), fill="black")
whiteboard.create_text(400, 263, text="Word", font=("Arial", 60, "bold"), fill="black")

# Buttons with images
wrong_button = Button(window, image=wrong_img, highlightthickness=0, bd=0, bg=BACKGROUND_COLOR, command=pick_word)
wrong_button.grid(row=1, column=0, pady=20)

right_button = Button(window, image=right_img, highlightthickness=0, bd=0, bg=BACKGROUND_COLOR, command = pick_word)
right_button.grid(row=1, column=1, pady=20)



pick_word()


window.mainloop()

