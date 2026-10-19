from tkinter import *

window = Tk()
window.geometry("300x300")
window.title("Newsletter")
window.config(background="blue")
label1 = Label(window,text="Subscribe to the Newsletter")
label1.place(x=30,y=50)
label2 = Label(window,text="Email")
label2.place(x=30,y=170)
entry1 = Entry(window)
entry1.place(x=80,y=170)
button1 = Button(window,text="Subscribe")
button1.place(x=55,y=250)

window.mainloop()