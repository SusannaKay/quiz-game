from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizUi():

    def __init__(self, quiz_questions: QuizBrain):
        self.quiz = quiz_questions
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(background=THEME_COLOR, padx=20, pady=20)

        

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(
            150,
            125, 
            text="testo domanda", 
            font=("Arial", 20, "italic"),
            width=280)
        self.canvas.grid(column=0,row=1, columnspan=2, pady=50)

        
        self.score_label = Label(text=f"Score: 0", fg="white", bg=THEME_COLOR)
        self.score_label.grid(column=1, row=0)

        true_img = PhotoImage(file="images/true.png")
        self.true = Button(borderwidth=0, image=true_img, highlightthickness=0)
        self.true.grid(column=0,row=2)

        false_img = PhotoImage(file="images/false.png")
        self.false = Button(borderwidth=0, image=false_img, highlightthickness=0)
        self.false.grid(column=1,row=2)
        
        self.next_question()
        


        self.window.mainloop()
    
    def next_question(self):
        q_text= self.quiz.next_question()
        self.canvas.itemconfig(self.question_text, text=q_text)

