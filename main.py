from tkinter import *
from tkinter import messagebox
window = Tk()
window.title("main")
window.geometry("250x250")


def calculate():
    try:
        messagebox.showerror("Error", "You do not qualify to go anywhere!")
    except ValueError:
        messagebox.showerror("Enter a integer")



# Widgets
label = Label(window, text="Please Enter amount in your account")
label.pack(pady=5)
entry_number = Entry(window,)
entry_number.pack(pady=5)
button_calculate = Button(window, text="Check Qualification", command=calculate)
button_calculate.pack()

window.mainloop()
