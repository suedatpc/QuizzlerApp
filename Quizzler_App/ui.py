from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
FONT = ("Arial", 20, "italic")
SCORE_FONT = ("Arial", 10, "bold")

class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.root = Tk()
        self.root.title("Quizzler")
        self.root.config(bg=THEME_COLOR, padx=20, pady=20)

        self.label_score = Label(text="Score: 0", font=SCORE_FONT, bg=THEME_COLOR, fg="white")
        self.label_score.grid(column=1, row=0)
        self.canvas = Canvas(self.root, width=300, height=250, bg="white")
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)
        
        self.question_text = self.canvas.create_text(150, 125, text="Some Question Text", fill=THEME_COLOR, font=FONT, width=280)

        correct_img = PhotoImage(file="Quizzler_App/images/true.png")
        incorrect_img = PhotoImage(file="Quizzler_App/images/false.png")
        self.correct_button = Button(image=correct_img, highlightthickness=0, activebackground=THEME_COLOR, border=0, command=self.true_clicked)
        self.incorrect_button = Button(image=incorrect_img, highlightthickness=0, activebackground=THEME_COLOR, border=0, command=self.false_clicked)
        self.correct_button.grid(column=0, row=2)
        self.incorrect_button.grid(column=1, row=2)
        

        self.get_next_question()
        self.root.mainloop()


    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.fix_score()
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz.")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def true_clicked(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def false_clicked(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.root.after(1000, self.get_next_question)

    def fix_score(self):
        self.label_score.config(text=f"Score:{self.quiz.score}")