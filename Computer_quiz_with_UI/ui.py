from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self,quiz_brain:QuizBrain):
        self.quiz=quiz_brain
        self.window=Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20,pady=20,background=THEME_COLOR)
        self.score_label=Label(text="Score:0",bg=THEME_COLOR,fg="white")
        self.score_label.grid(row=0,column=1)

        self.canvas=Canvas(width=300,height=250,bg="white")

        self.question=self.canvas.create_text(150,125,
                                              width=280,

                                              text="abcd",
                                              fill=THEME_COLOR,
                                              font=("Arial",20,'italic'))

        self.canvas.grid(row=1,column=0,columnspan=2,pady=50)
        true_image=PhotoImage(file="images/true.png")
        false_image=PhotoImage(file="images/false.png")
        self.true=Button(bd=0,image=true_image,highlightthickness=0,command=self.get_true)
        self.false=Button(image=false_image,bd=0,highlightthickness=0,command=self.get_false)
        self.true.grid(row=2,column=0)
        self.false.grid(row=2, column=1)
        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):

        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f'Score:{self.quiz.score}')
            q_text=self.quiz.next_question()
            self.canvas.itemconfig(self.question,text=q_text)
        else:
            self.canvas.itemconfig(self.question,text="You have reached the limt")
            self.true.config(state="disabled")
            self.false.config(state="disabled")

    def get_true(self):
        self.get_feedback(self.quiz.check_answer("true"))

    def get_false(self):
        self.get_feedback(self.quiz.check_answer("false"))

    def get_feedback(self,is_right):
        if is_right:
            self.canvas.config(bg="Green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000,self.get_next_question)


