from tkinter import *


window = Tk("kilograms -> grams, lbs, oz")

window.geometry('1000x300')

Label(window, text="Enter Weight in Kilograms").grid(row=0)
e1_value = StringVar()
e1 = Entry(window, textvariable=e1_value)

e1.grid(row=0, column=1)


def convert_kgs_lbs():

    grams = float(e1_value.get()) * 1000
    pounds = float(e1_value.get()) * 2.20462
    ounces = float(e1_value.get()) * 35.274

    t1.delete("1.0", END)
    t1.insert(END, grams)
    t2.delete("1.0", END)
    t2.insert(END, pounds)
    t3.delete("1.0", END)
    t3.insert(END, ounces)


# Label for results
Label(window, text="grams").grid(row=3, column=1)
Label(window, text="pounds").grid(row=3, column=2)
Label(window, text="ounces").grid(row=3, column=3)

# text widgets
t1 = Text(window, height=1, width=20, wrap=WORD, bd=2, bg="green")
t2 = Text(window, height=1, width=20, wrap=WORD, bd=2, bg="green")
t3 = Text(window, height=1, width=20, wrap=WORD, bd=2, bg="green")

t1.grid(row=4, column=1)
t2.grid(row=4, column=2)
t3.grid(row=4, column=3)

btn = Button(window, text="Click", width=25, activebackground="#00ff32",
             command=convert_kgs_lbs)
btn.grid(row=0, column=2)


# btn.pack(side="bottom")


def kg_to_lbs():
    print("hi")


window.mainloop()
