from tkinter import *
import pandas as pd
import random
BACKGROUND_COLOR = "#B1DDC6"
data={}
try:
    df=pd.read_csv("data/words_to_learn")
except FileNotFoundError:
    original_data=pd.read_csv("data/french_words.csv")
    data=original_data.to_dict('records')

else:
    data=df.to_dict('records')
currentword={}
window=Tk()
def next_word():
    global currentword,flip_timer
    window.after_cancel(flip_timer)
    currentword=random.choice(data)
    canvas.itemconfig(card_title,text="French",fill="Black")
    canvas.itemconfig(card_text,text=currentword['French'],fill="Black")
    canvas.itemconfig(card_image,image=card_front_image)
    flip_timer=window.after(3000,flip_card)

def flip_card():
    canvas.itemconfig(card_image,image=card_back_image)
    canvas.itemconfig(card_title,text="English",fill="White")
    canvas.itemconfig(card_text,text=currentword["English"],fill="White")

def words_learned():

    data.remove(currentword)
    to_learn=pd.DataFrame(data)
    to_learn.to_csv("data/word_to_learn.csv")
    next_word()

window.title("Flash Card Game")
window.config(padx=50,pady=50,bg=BACKGROUND_COLOR)
flip_timer=window.after(3000,func=flip_card)

canvas=Canvas(width=800,height=526)

canvas.config(bg=BACKGROUND_COLOR,highlightthickness=0)
card_front_image=PhotoImage(file="images/card_front.png")
card_back_image=PhotoImage(file="images/card_back.png")
card_image =canvas.create_image(400,263,image=card_front_image)
card_title=canvas.create_text(400,152,font=("Aerial",40,"italic"),text="")
card_text=canvas.create_text(400, 263, font=("Aerial", 60, "bold"), text='')

canvas.grid(row=0,column=0,columnspan=2)
unknown_image=PhotoImage(file='images/wrong.png')

wrong=Button(image=unknown_image,bd=0,highlightthickness=0,command=next_word)

wrong.grid(row=1,column=0)
check_image=PhotoImage(file='images/right.png')
correct=Button(image=check_image,bd=0,highlightthickness=0,command=words_learned)
correct.grid(row=1,column=1)
next_word()
window.mainloop()