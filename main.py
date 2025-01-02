from tkinter import *
import pandas as pd

word = pd.read_csv(".//data/data.csv")
BACKGROUND_COLOR = "#B1DDC6"
POINTS = 0
def background_returns():
    canvas.itemconfig(background , image= back_img)

def background_switch():
    canvas.itemconfig(background , image= front_img)
    window.after(3000, background_returns)


window = Tk()
window.configure(padx=25,pady=25,background=BACKGROUND_COLOR)
window.minsize(width=600,height=700)


back_img = PhotoImage(file="./images/card_back.png")
front_img = PhotoImage(file="./images/card_front.png")
x_img = PhotoImage(file="./images/wrong.png",width=100, height=100)
v_img = PhotoImage(file="./images/right.png",width=100, height=100)

canvas = Canvas()
canvas.configure(width=800,height=526,highlightthickness=0,background=BACKGROUND_COLOR)
background = canvas.create_image(400,263,image=back_img)
display = canvas.create_text(400,100 ,text="test", justify="center" )

canvas.grid()


x_switch = Button(text="Switch")
x_switch.configure(image=v_img )
x_switch.place(x=580,y=530)

y_switch = Button(text="Switch")
y_switch.configure(image=x_img )
y_switch.place(x=100,y=530)


testing_switch = Button()
testing_switch.configure(text="Guziol",command=background_switch)
testing_switch.place(x=360,y=455)

points = Label()
points.configure(text="0", justify="center",highlightthickness=0, background="gray")
points.place(x=400,y=2)




window.mainloop()
