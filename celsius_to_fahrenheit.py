from tkinter import *

window = Tk()
window.geometry("300x200")
window.title("Celsius to Fahrenheit")
window.config(background="black")

def convert():
    celsius = int(entry_1.get())
    fahrenheit = (celsius*1.8)+32
    label_3.config(text="Temperature in Fahrenheit: " + str(fahrenheit)) 

label_1 = Label(window,text="Celsius -> Fahrenheit",fg="grey",bg="black")
label_1.place(x=80,y=20)
label_2 = Label(window,text="Enter Temperatur in Celsius:",fg="white",bg="black")
label_2.place(x=20,y=50)
entry_1 = Entry(window,width=15)
entry_1.place(x=180,y=50)
label_3 = Label(window,text="Temperatur in Fahrenheit: ",fg="white",bg="black")
label_3.place(x=60,y=80)
button_1 = Button(window,text="Convert",background="white",width=15,command=convert)
button_1.place(x=100,y=120)

window.mainloop()