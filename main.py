# PiNE Ver. 3.1
import tkinter as tk
from tkinter import filedialog as fd
import os


def main():
    root = tk.Tk()
    _ = TextEditor(root)
    root.mainloop()


class TextEditor:
    current_open_file = "no_file"

    def __init__(self, master):
        self.master = master
        self.font_size = 18

        master.geometry("1280x720")
        master.title("PiNE")
        master.iconbitmap("icon.ico")

        self.text_field = tk.Text(font=("MS明朝", self.font_size))
        self.text_field.pack(fill=tk.BOTH, expand=1)
        
        self.main_menu = tk.Menu()
        self.master.config(menu=self.main_menu)

        self.file_menu = tk.Menu(self.main_menu)
        self.main_menu.add_cascade(label="ファイル", menu=self.file_menu)
        self.file_menu.add_command(label="開く", command=self.open_file)
        self.file_menu.add_command(label="名前を付けて保存",
                                   command=self.save_file)

        self.edit_menu = tk.Menu(self.main_menu)
        self.main_menu.add_cascade(label="編集", menu=self.edit_menu)

        self.format_menu = tk.Menu(self.main_menu)
        self.main_menu.add_cascade(label="書式", menu=self.format_menu)
        self.format_menu.add_command(label="フォントサイズ",
                                     command=self.font_size_increase)

    def open_file(self):
        file_name = fd.askopenfilename(initialdir=os.getcwd(),
                                       title="開く",
                                       filetypes=(("テキスト文書", "*.txt"),
                                                  ("すべてのファイル", "*.*")))

        try:
            with open(file_name, encoding="UTF-8") as file:
                for i in file:
                    self.text_field.insert(tk.END, i)
        except UnicodeDecodeError:
            with open(file_name) as file:
                for i in file:
                    self.text_field.insert(tk.END, i)

    def save_file(self):
        f = fd.asksaveasfile(initialdir=os.getcwd(),
                             mode="w",
                             filetypes=(("テキスト文書", "*.txt"),
                                        ("すべてのファイル", "*.*")))

        if f is None:
            return

        text2save = self.text_field.get(1.0, tk.END)
        f.write(text2save)
        f.close()

    def font_size_increase(self):
        self.font_size = 49


if __name__ == "__main__":
    main()
