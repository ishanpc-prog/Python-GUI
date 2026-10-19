from tkinter import *

window = Tk()
window.geometry("300x300")
window.title("Traffic lights!")
window.config(background="white")
green_button = Button(window,text="GREEN",background="green",width=25)
green_button.place(x=50,y=250)
yellow_button = Button(window,text="YELLOW",background="yellow",width=25)
yellow_button.place(x=50,y=150)
red_button = Button(window,text="RED",background="red",width=25)
red_button.place(x=50,y=50)
window.mainloop()