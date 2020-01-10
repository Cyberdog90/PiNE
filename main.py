# PiNE Ver. 3.0
import tkinter as tk
from tkinter import filedialog as fd


def main():
    root = tk.Tk()
    _ = TextEditor(root)
    root.mainloop()


class TextEditor:
    def __init__(self, master):
        self.master = master

        master.geometry("1280x720")
        master.title("PiNE")
        master.iconbitmap("icon.ico")

        self.text_field = tk.Text()
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

    def open_file(self):
        file_name = fd.askopenfilename(initialdir="/",
                                       title="開く",
                                       filetypes=(("テキスト文書", "*.txt"),
                                                  ("すべてのファイル", "*.*")))

        with open(file_name, encoding="UTF-8") as file:
            for i in file:
                self.text_field.insert(tk.END, i)

    def save_file(self):
        f = fd.asksaveasfile(initialdir="/",
                             mode="w",
                             # defaultextension=".txt",
                             filetypes=(("テキスト文書", "*.txt"),
                                        ("すべてのファイル", "*.*")))
        if f is None:
            return
        text2save = self.text_field.get(1.0, tk.END)
        f.write(text2save)
        f.close()


if __name__ == "__main__":
    main()
