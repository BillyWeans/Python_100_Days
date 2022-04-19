from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.lbl_score = Label(text=f"Score: 0", bg=THEME_COLOR)
        self.lbl_score.grid(column=1, row=0)
        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(150, 100, text="This is some text", fill="black",
                                                     font=("Arial", 20, "italic"),
                                                     width=270)
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        img_true = PhotoImage(file="images/true.png")
        img_false = PhotoImage(file="images/false.png")
        self.btn_yes = Button(image=img_true, command=self.answer_true)
        self.btn_yes.grid(column=0, row=2)
        self.btn_no = Button(image=img_false, command=self.answer_false)
        self.btn_no.grid(column=1, row=2)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        self.score = self.quiz.score
        if self.quiz.still_has_questions():
            self.lbl_score.config(text=f"Score: {self.score}", bg=THEME_COLOR)
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
            self.btn_yes.config(state="active")
            self.btn_no.config(state="active")
        else:
            self.canvas.itemconfig(self.question_text, text="You have reached the end of the quiz!")
            self.btn_yes.config(state="disabled")
            self.btn_no.config(state="disabled")

    def answer_true(self):
        answer_correct = self.quiz.check_answer("true")
        self.show_answer(answer_correct)

    def answer_false(self):
        answer_correct = self.quiz.check_answer("false")
        self.show_answer(answer_correct)

    def show_answer(self, answer_correct):
        self.btn_yes.config(state="disabled")
        self.btn_no.config(state="disabled")
        if answer_correct:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)
