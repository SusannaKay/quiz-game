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
        self.true = Button(borderwidth=0, image=true_img, highlightthickness=0, command= self.true_ans)
        self.true.grid(column=0,row=2)

        false_img = PhotoImage(file="images/false.png")
        self.false = Button(borderwidth=0, image=false_img, highlightthickness=0, command= self.false_ans)
        self.false.grid(column=1,row=2)
        
        self.next_question()
        


        self.window.mainloop()
    
    def next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            
            self.score_label.config(text=f"Score:{self.quiz.score}")
            q_text= self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You have reached the end of the quiz")
            self.true.config(state="disabled")
            self.false.config(state="disabled")
        

    def true_ans(self):
        self.give_feedback(self.quiz.check_answer("true"))
    
    def false_ans(self):
        self.give_feedback(self.quiz.check_answer("false"))
    
    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
            
        self.window.after(1000, self.next_question)

    
        

