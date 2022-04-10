from tkinter import *
import pandas
import random

# ---------- Constants ----------- #
BACKGROUND_COLOR = "#B1DDC6"


# ---------- Functions ----------- #
def word_correct():
    words_to_learn.remove(card)
    df_words_to_learn = pandas.DataFrame(words_to_learn)
    df_words_to_learn.to_csv("data/words_to_learn.csv", index=False)
    next_card()


def word_wrong():
    next_card()


def next_card():
    global timer
    if timer:
        window.after_cancel(timer)
    global card
    card = random.choice(words_to_learn)
    french_word = card["French"]
    canvas.itemconfig(cnv_card_img, image=flashcard_front_img)
    canvas.itemconfig(cnv_txt_language, text="French", fill="black")
    canvas.itemconfig(cnv_txt_word, text=french_word, fill="black")

    timer = window.after(3000, flip_card)


def flip_card():
    english_word = card["English"]
    canvas.itemconfig(cnv_card_img, image=flashcard_back_img)
    canvas.itemconfig(cnv_txt_language, text="English", fill="white")
    canvas.itemconfig(cnv_txt_word, text=english_word, fill="white")


# ---------- Setup the Screen ----------- #
timer = False
card = {}
window = Tk()
window.title("Flashcards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=650, bg=BACKGROUND_COLOR, highlightthickness=0)
flashcard_front_img = PhotoImage(file="images/card_front.png")
flashcard_back_img = PhotoImage(file="images/card_back.png")
cnv_card_img = canvas.create_image(400, 350, image=flashcard_front_img)
cnv_txt_language = canvas.create_text(400, 200, text="Language", fill="black", font=("Ariel", 40, "italic"))
cnv_txt_word = canvas.create_text(400, 350, text="Word", fill="black", font=("Ariel", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

img_x = PhotoImage(file="images/wrong.png")
btn_wrong = Button(image=img_x, highlightbackground=BACKGROUND_COLOR, command=word_wrong)
btn_wrong.grid(column=0, row=1)

img_check = PhotoImage(file="images/right.png")
btn_right = Button(image=img_check, highlightbackground=BACKGROUND_COLOR, command=word_correct)
btn_right.grid(column=1, row=1)

# ---------- Load Words ----------- #
try:
    df_french_words = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    df_french_words = pandas.read_csv("data/french_words.csv")
finally:
    words_to_learn = df_french_words.to_dict(orient="records")

next_card()

# ---------- Save Results ----------- #

window.mainloop()
