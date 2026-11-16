from tkinter import *

window = Tk()
window.geometry("250x125")
window.title("System Login")
window.config(background="black")

def login():
    username_answer = "bigben"
    password_answer = "pineapplepie1"
    username_login = entry_1.get()
    passwort_login = entry_2.get()
    if username_login == username_answer and passwort_login == password_answer:
        label_3.config(text="Login sucessful!",fg="green")
    else:
        label_3.config(text="Login unsucessful!",fg="red")

label_1 = Label(window,text="Username:",bg="black",fg="white") # missing: bg,fg,font,width,height,bd
label_1.place(x=35,y=15)
entry_1 = Entry(window,width=15,bg="white",fg="black",bd=2)
entry_1.place(x=120,y=15)
label_2 = Label(window,text="Password:",bg="black",fg="white")
label_2.place(x=35,y=40)
entry_2 = Entry(window,width=15,bd=2,)
entry_2.place(x=120,y=40)
button_1 = Button(window,text="Login",background="green",command=login)
button_1.place(x=35,y=80)
button_2 = Button(window,text="Cancel",background="red",command=window.destroy) 
button_2.place(x=170,y=80)
label_3 = Label(window,text="",bg="black")
label_3.place(x=100,y=30)

window.mainloop()