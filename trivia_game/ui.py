from tkinter import *
from PIL import Image, ImageTk
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizUI:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=50, pady=50, background=THEME_COLOR)

        # question text canvas
        self.canvas = Canvas(width=300, height=300, background="white")
        self.question_text = self.canvas.create_text(150, 150, text="", width=280, font=("Arial", 20, "bold"), fill=THEME_COLOR)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=30)

        # score counter label
        self.score_counter = Label(text=f"Score: {self.quiz.score}", font=("Arial", 20), background=THEME_COLOR, foreground="white")
        self.score_counter.grid(row=0, column=1, pady=20)

        # true answer btn
        right_ans = Image.open("images/true.png")
        true_img = ImageTk.PhotoImage(right_ans)
        self.true_btn = Button(image=true_img, highlightthickness=0, command=self.answer_correct)
        self.true_btn.grid(row=2, column=0, pady=30)

        # false answer btn
        wrong_ans = Image.open("images/false.png")
        false_img = ImageTk.PhotoImage(wrong_ans)
        self.false_btn = Button(image=false_img, highlightthickness=0, command=self.answer_wrong)
        self.false_btn.grid(row=2, column=1, pady=30)

        self.get_question()

        self.window.mainloop()

    def answer_correct(self):
        is_right = self.quiz.check_answer("true")
        self.show_answer(is_right)

    def answer_wrong(self):
        is_right = self.quiz.check_answer("false")
        self.show_answer(is_right)

    def get_question(self):
        if self.quiz.still_has_questions():
            self.canvas.config(background="white")
            next_question = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=next_question)
        else:
            self.canvas.config(background="white")
            self.canvas.itemconfig(self.question_text, text="Quiz is over!")
            self.true_btn.config(state="disabled")
            self.false_btn.config(state="disabled")

    def show_answer(self, is_right: bool):
        if is_right:
            self.canvas.config(background="green")
            self.score_counter.config(text=f"Score: {self.quiz.score}")
        else:
            self.canvas.config(background="red")
        self.window.after(1000, self.get_question)
        