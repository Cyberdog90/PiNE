# PiNE Ver. 2.0
import tkinter as tk


def get_text():
    global string
    string = txt_field.get()


root = tk.Tk()
root.geometry("1280x720")
root.title("PiNE")
root.iconbitmap("icon.ico")

txt_field = tk.Entry(width=100)
txt_field.place(x=5, y=5)
but = tk.Button(text="click", command=get_text)
but.pack()
root.mainloop()
with open("test.txt", "w") as f:
    f.write(string)
