from tkinter import *
from tkinter import messagebox

window = Tk()
window.title("Authentication")
window.geometry("500x500")
window.config(bg="grey")
# Dictionary of Usernames : Passwords
usernames_password = {"Gideon": "1234", "Daniels": "1234", "Ashwin": "1234", "danny": "1456"}


def confirm():
    try:
        # import pdb;pdb.set_trace()
        user_name = entry_username.get()
        password = entry_password.get()
        if user_name in usernames_password and password == usernames_password[user_name]:
            window.destroy()
            import main
        else:
            messagebox.showerror("Error","Insert correct password and username.")
    except :
        messagebox.showerror("Error", "Insert correct password and username.")



# Widgets

label_header = Label(window, text="Please Enter Login Details")
label_header.pack()
label_username = Label(window, text="Username",bg="blue")
label_username.pack(pady=20)
entry_username = Entry(window,)
entry_username.pack(pady=10)
label_password = Label(window, text="Password", bg="blue")
label_password.pack(pady=10)
entry_password = Entry(window, show="*")
entry_password.pack(pady=10)
button_confirm = Button(window, text="Login", command=confirm, bg="blue")
button_confirm.pack(pady=20)









window.mainloop()