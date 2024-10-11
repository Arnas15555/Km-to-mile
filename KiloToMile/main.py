from tkinter import *

window = Tk()
window.title("Distance Converter")
window.minsize(width=250, height=150)
window.config(padx=25, pady=15)


def calculate():
    miles = float(text_entry.get())
    kilometers = round(miles * 1.60934, 2)
    answer_label.config(text=f"{kilometers}")


text_entry = Entry(width=10)
text_entry.grid(row=0, column=1)

mile_label = Label(text="Miles")
mile_label.grid(row=0, column=2)

equal_label = Label(text="is equal to")
equal_label.grid(row=1, column=0)

answer_label = Label(text="0")
answer_label.grid(row=1, column=1)

km_label = Label(text="Km")
km_label.grid(row=1, column=2)

button = Button(text="Calculate", command=calculate)
button.grid(row=2, column=1)

window.mainloop()
