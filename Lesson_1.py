from tkinter import *

window = Tk()
window.geometry("500x500")
window.title("GUI Window")
window.config(background="red")
click_button = Button(window,text="click me",background="white",command=window.destroy)
click_button.pack(side="top")

window.mainloop()