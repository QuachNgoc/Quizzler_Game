
from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain ):

        self.quiz = quiz_brain

        self.win = Tk()
        self.win.title("Quizzler")
        self.win.config(padx=20, pady=20, bg=THEME_COLOR)

        self.high_score_label = Label(text=f"High Score: {self.quiz.high_score}", bg=THEME_COLOR, fg="white", font=("Arial", 15, "bold"))
        self.high_score_label.grid(column=0, row=0)
        self.score_label = Label(text=f"Score: 0", bg=THEME_COLOR, fg="white", font=("Arial", 15, "bold"))
        self.score_label.grid(column=1, row=0)
        # Canvas

        self.canvas = Canvas(height=250, width=300)
        self.question_text = self.canvas.create_text(
            150,125,
            text='question here',
            font=("Arial", 20, "italic"),
            fill=THEME_COLOR,
            width=280
        )
        self.canvas.grid(column=0, row=1, columnspan=2, pady=40)

        true_button_img = PhotoImage(file="./images/true.png")
        self.true_button = Button(image=true_button_img, highlightthickness=0, command=self.guess_True)
        self.true_button.grid(column=0, row=2)

        false_button_img = PhotoImage(file="./images/false.png")
        self.false_button = Button(image=false_button_img, highlightthickness=0, command=self.guess_False)
        self.false_button.grid(column=1, row=2)

        self.get_next_question()

        self.win.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)

        else:
            self.canvas.itemconfig(self.question_text, text="You reached the end.")

            self.score_label.config(text=f"Score: {self.quiz.score}")

            if self.quiz.score > self.quiz.high_score:
                self.quiz.high_score = self.quiz.score
                with open("./data.txt", mode="w") as data_1:
                    data_1.write(str(self.quiz.high_score))

                self.quiz.score = 0

            self.high_score_label.config(text=f"High Score: {self.quiz.high_score}")

            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def guess_True(self):
        self.give_feedback( self.quiz.check_answer("True") )

    def guess_False(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.win.after(1000, self.get_next_question)



