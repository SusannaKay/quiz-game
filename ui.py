from tkinter import *
THEME_COLOR = "#375362"

class QuizUi():

    def __init__(self):

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(background=THEME_COLOR, padx=20, pady=20)

        

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(150,125, text="testo domanda", font=("Arial", 20, "italic"))
        self.canvas.grid(column=0,row=1, columnspan=2, pady=50)

        
        self.score_label = Label(text=f"Score: 0", fg="white", bg=THEME_COLOR)
        self.score_label.grid(column=1, row=0)

        true_img = PhotoImage(file="images/true.png")
        self.true = Button(borderwidth=0, image=true_img, highlightthickness=0)
        self.true.grid(column=0,row=2)

        false_img = PhotoImage(file="images/false.png")
        self.false = Button(borderwidth=0, image=false_img, highlightthickness=0)
        self.false.grid(column=1,row=2)
        
        
        


        self.window.mainloop()
        