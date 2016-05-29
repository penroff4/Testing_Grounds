import tkinter

window = tkinter.Tk()

username_label = tkinter.Label(window, text="Username")
username_entry = tkinter.Entry(window)

password_label = tkinter.Label(window, text="Password")
password_entry = tkinter.Entry(window)

login_button = tkinter.Button(window, text="Login")

username_label.pack()
username_entry.pack()

password_label.pack()
password_entry.pack()

login_button.pack()

window.mainloop()
