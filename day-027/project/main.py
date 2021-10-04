import tkinter


def calculate():
    cal = float(input.get()) * 1.609
    result.config(text=f"{cal}")


window = tkinter.Tk()
window.title("Mile to Km Converter")
window.config(padx=50, pady=50)

tkinter.Label(text="is equal to", font=("Ubuntu", 12, "bold")).grid(column=0, row=1)

input = tkinter.Entry(width=10)
input.grid(column=1, row=0)

result = tkinter.Label(text="0", font=("Ubuntu", 12, "bold"))
result.grid(column=1, row=1)

tkinter.Label(text="Miles", font=("Ubuntu", 12, "bold")).grid(column=2, row=0)
tkinter.Label(text="Km", font=("Ubuntu", 12, "bold")).grid(column=2, row=1)

button = tkinter.Button(
    text="Calculate", font=("Ubuntu", 10, "bold"), command=calculate
)
button.grid(column=1, row=2)


window.mainloop()
