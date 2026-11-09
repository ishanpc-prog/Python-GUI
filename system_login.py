from tkinter import *

window = Tk()
window.geometry("300x300")
window.title("System Login")
window.config(background="black")
label_1 = Label(window,text="Username",bg="grey",fg="yellow") # missing: bg,fg,font,width,height,bd
label_1.place(x=35,y=15)
entry_1 = Entry(window,width=15,bg="yellow",fg="black",bd=2)
entry_1.place(x=120,y=15)
label_2 = Label(window,text="Password",bg="grey")
label_2.place(x=35,y=40)
entry_2 = Entry(window,width=15)
entry_2.place(x=120,y=40)
button_1 = Button(window,text="Login",background="green")
button_1.place(x=35,y=80)
button_2 = Button(window,text="Cancel",background="red",command=window.destroy) 
button_2.place(x=170,y=80)

window.mainloop()