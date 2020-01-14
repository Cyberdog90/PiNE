# Ahoj Editor Ver. Ahoj
import tkinter as tk
from tkinter import filedialog as fd
import os


def main():
    root = tk.Tk()
    _ = TextEditor(root)
    root.mainloop()


class TextEditor:
    def __init__(self, master):
        master.geometry("1280x720")
        master.title("Ahoj Editor")
        master.iconbitmap("./data/icon.ico")

        self.current_open_file = None
        self.flag = True
        self.color = True

        self.master = master
        self.font = "MS明朝"
        self.font_size = 18

        self.text_field = tk.Text(font=(self.font, self.font_size), undo=True)
        self.text_field.pack(fill=tk.BOTH, expand=1)

        self.main_menu = tk.Menu()
        self.master.config(menu=self.main_menu)

        self.file_menu = tk.Menu(self.main_menu, tearoff=False)

        self.file_menu.bind_all("<Control-o>", self.open_file)
        self.file_menu.bind_all("<Shift-Control-S>", self.save_file)
        self.file_menu.bind_all("<Control-s>", self.overwrite)
        self.file_menu.bind_all("<Shift-Control-O>", self.open_latest_file)
        self.file_menu.bind_all("<Escape>", self.quit)
        self.file_menu.bind_all("<Shift-Control-D>", self.get_pos)
        self.file_menu.bind_all("<Shift-Control-N>", self.night_mode)
        self.file_menu.bind_all("<Shift-Control-C>", self.command_mode)

    def night_mode(self, *_):
        if self.color:
            self.text_field.config({"background": "Black"})
            self.text_field.config({"foreground": "White"})
            self.color = False
        else:
            self.text_field.config({"background": "White"})
            self.text_field.config({"foreground": "Black"})
            self.color = True

    def quit(self, *_):
        if self.current_open_file is not None:
            self.overwrite()
        self.open_check()
        self.destroy()

    def get_pos(self, *_):
        text = self.text_field.get("insert linestart", "insert lineend")
        self.text_field.insert("insert linestart", "{}\n".format(text))

    def open_check(self):
        text = len(list("".join(self.text_field.get(1.0, tk.END))))
        if text != 1:
            self.overwrite()
        self.text_field.delete(1.0, tk.END)

    def open_latest_file(self, *_):
        self.open_check()
        with open("log.txt", "r") as f:
            file_name = f.readline()
            try:
                with open(file_name, encoding="UTF-8") as file:
                    for i in file:
                        self.text_field.insert(tk.END, i)
            except UnicodeDecodeError:
                with open(file_name) as file:
                    for i in file:
                        self.text_field.insert(tk.END, i)

            self.current_open_file = file_name

    def overwrite(self, *_):
        if self.current_open_file is not None:
            with open(self.current_open_file, "w") as f:
                text2save = self.text_field.get(1.0, tk.END)
                f.write(text2save)
        else:
            self.save_file()

    def open_file(self, *_):
        self.open_check()
        file_name = fd.askopenfilename(initialdir=os.getcwd(),
                                       title="開く",
                                       filetypes=("テキスト文書", "*.txt"))

        try:
            with open(file_name, encoding="UTF-8") as file:
                for i in file:
                    self.text_field.insert(tk.END, i)
        except UnicodeDecodeError:
            with open(file_name) as file:
                for i in file:
                    self.text_field.insert(tk.END, i)

        self.current_open_file = file_name
        with open("log.txt", "w") as f:
            f.write(self.current_open_file)

    def save_file(self, *_):
        with fd.asksaveasfile(initialdir=os.getcwd(),
                              mode="w",
                              defaultextension=".txt",
                              filetypes=(("テキスト文書", "*.txt"),
                                         ("すべてのファイル", "*.*"))) as f:
            if f is None:
                return

            text2save = self.text_field.get(1.0, tk.END)
            f.write(text2save)

    def destroy(self):
        self.master.destroy()

    def command_mode(self, *_):
        text = self.text_field.get("insert linestart", "insert lineend")
        text = text.split()

        type = text[0]
        if type == "#":
            pass
        elif type == "@":
            if text[1] == "font":
                self.text_field.config({"foreground": "{}".format(text[2])})
                self.text_field.delete("insert linestart", "insert lineend")
        else:
            return

        if text[1] == "font":
            self.text_field.config({"foreground": "{}".format(text[2])})
            self.text_field.delete("insert linestart", "insert lineend")


if __name__ == "__main__":
    main()
