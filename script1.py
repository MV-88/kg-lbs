from tkinter import *


window = Tk("kilograms -> grams, lbs, oz")

window.geometry('1000x300')

btn = Button(window, text="Click", width=25, activebackground="#00ff32",
             command=window.destroy)

btn.pack(side="bottom")


def kg_to_lbs():
    print("hi")


window.mainloop()
