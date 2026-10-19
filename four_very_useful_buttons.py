from tkinter import *

window = Tk()
window.geometry("100x100")
window.config(background="black")
tha_button1 = Button(window,text="",background="white")
tha_button1.pack(side="top")
tha_button2 = Button(window,text="",background="white")
tha_button2.pack(side="left")
tha_button3 = Button(window,text="",background="white")
tha_button3.pack(side="right")
tha_button4 = Button(window,text="",background="white")
tha_button4.pack(side="bottom")

window.mainloop()