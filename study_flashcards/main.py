from tkinter import *
from PIL import Image, ImageTk
import pandas
import random

from pandas.core.frame import DataFrame
from pandas.io.sql import PandasSQL

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
words = {}
#------------- DATA SETUP -------------#
try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    data = pandas.read_csv("data/french_words.csv")
words = data.to_dict(orient="records")

def create_new_card():
    global current_card, flip_timer

    window.after_cancel(flip_timer)
    current_card = random.choice(words)
    new_french_word = current_card["French"]
    canvas.itemconfig(card_word, text=new_french_word, fill="black")
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(frontgroung, image=front_card)
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(frontgroung, image=back_card)

def is_known():
    words.remove(current_card)
    data = pandas.DataFrame(words)
    data.to_csv("data/words_to_learn.csv", index=False)
    create_new_card()


#------------- UI SETUP -------------#
window = Tk()
window.title("Flash Cards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
front_img = Image.open("images/card_front.png")
front_card = ImageTk.PhotoImage(front_img)
frontgroung = canvas.create_image(400, 263, image=front_card)

back_img = Image.open("images/card_back.png")
back_card = ImageTk.PhotoImage(back_img)


card_title = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"), fill="black")
card_word = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"), fill="black")

canvas.grid(column=1, row=0)

# Buttons
tick = Image.open("images/right.png")
tick_image = ImageTk.PhotoImage(tick)
correct_button = Button(image=tick_image, command=is_known)
correct_button.grid(column=2, row=1)

cross = Image.open("images/wrong.png")
cross_image = ImageTk.PhotoImage(cross)
wrong_button = Button(image=cross_image, command=create_new_card)
wrong_button.grid(column=0, row=1)


flip_timer = window.after(3000, func=flip_card)

create_new_card()

window.mainloop()
