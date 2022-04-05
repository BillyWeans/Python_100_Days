import tkinter

window = tkinter.Tk()
window.title("This is my window")
window.minsize(width=500, height=300)
window.config(padx=50, pady=50)

my_label = tkinter.Label(text="I am a Label", font=("Arial", 24, "bold"))
#my_label.pack(side="left")
my_label.grid(column=0, row=0)
my_label.config(padx=50, pady=50)

my_label["text"] = "New Text"
# Code below does the exact same thing
my_label.config(text="New Text")


def button_clicked():
    my_label.config(text=input.get())


button = tkinter.Button(text="Click Me", command=button_clicked)
button.grid(column=1, row=1)

button2= tkinter.Button(text="Click Me2")
button2.grid(column=2, row=0)

input = tkinter.Entry(width=20)
input.insert(tkinter.END, string="This is the text that originally appears")
input.grid(column=3, row=2)

window.mainloop()
