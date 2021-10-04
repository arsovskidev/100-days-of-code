from tkinter import *


def button_clicked():
    print("I got clicked")
    my_label.config(text=my_input.get())


window = Tk()
window.title("GUI Program")
window.minsize(500, 500)
# window.config(padx=100, pady=200)

# Label
my_label = Label(text="I am a label", font=("Ubuntu", 24, "bold"))
# my_label.pack()
# my_label.place(x=250, y=250)
# my_label.config(padx=50, pady=50)
my_label.grid(column=0, row=0)

# Button
my_button = Button(text="Submit", font=("Ubuntu", 12), command=button_clicked)
# my_button.pack()
my_button.grid(column=1, row=1)

# New Button
new_button = Button(text="New Button", font=("Ubuntu", 12))
# my_button.pack()
new_button.grid(column=2, row=0)

# Entry
my_input = Entry(width=10)
# my_input.pack()
my_input.grid(column=3, row=2)

window.mainloop()
