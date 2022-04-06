from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

CHECKMARK = "✔"
SECS_IN_MINUTE = 60 #Useful to flip this for debugging

timer = None
reps = 1

# ---------------------------- TIMER RESET ------------------------------- #
def app_reset():
    window.after_cancel(timer)
    global reps
    lbl_check.config(text="")
    lbl_timer.config(text="Timer", fg=GREEN)
    canvas.itemconfig(timer_text, text="00:00")
    reps = 1

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_countdown():
    global reps
    work_sec = (WORK_MIN * SECS_IN_MINUTE)
    short_break_sec = (SHORT_BREAK_MIN * SECS_IN_MINUTE)
    long_break_sec = (LONG_BREAK_MIN * SECS_IN_MINUTE)

    if reps % 8 == 0:
        count_down(long_break_sec)
        lbl_timer.config(text="Break", fg=RED)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        lbl_timer.config(text="Break", fg=PINK)
    elif reps % 2 == 1:
        count_down(work_sec)
        lbl_timer.config(text="Work", fg=GREEN)

    reps += 1

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):

    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    display_count = f"{count_min}:{count_sec}"  # TODO - This needs fixing
    canvas.itemconfig(timer_text, text=display_count)
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        num_checks = math.floor(reps / 2)
        check_text = ""
        for _ in range(num_checks):
            check_text += CHECKMARK
        lbl_check.config(text=check_text)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))

lbl_timer = Label(text="Timer", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 35, "normal"))
lbl_check = Label(text="", width=10, bg=YELLOW, fg=GREEN, font=(FONT_NAME, 30, "normal"))

btn_start = Button(text="Start", bg=YELLOW, fg="blue", highlightbackground=YELLOW, command=start_countdown)
btn_reset = Button(text="Reset", bg=YELLOW, fg="blue", highlightbackground=YELLOW, command=app_reset)

lbl_timer.grid(column=1, row=0)
canvas.grid(column=1, row=1)
btn_start.grid(column=0, row=2)
lbl_check.grid(column=1, row=3)
btn_reset.grid(column=2, row=2)

window.mainloop()
