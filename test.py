# Ahoj Editor Ver. 4.0
import tkinter as tk
from tkinter import filedialog as fd
import os
from falcon import falcon as falcon



def main():
    root = tk.Tk()
    _ = TextEditor(root)
    root.mainloop()
    print(falcon())


class TextEditor:
    def __init__(self, master):
        master.geometry("1280x720")
        master.title("Ahoj Editor")
        master.iconbitmap("./data/icon.ico")

        self.current_open_file = None

        self.master = master
        self.font = "MS明朝"
        self.font_size = 18

        self.text_field = tk.Text(font=(self.font, self.font_size))
        self.text_field.pack(fill=tk.BOTH, expand=1)

        self.main_menu = tk.Menu()
        self.master.config(menu=self.main_menu)

        self.file_menu = tk.Menu(self.main_menu, tearoff=False)
        self.main_menu.add_cascade(label="ファイル", menu=self.file_menu)
        self.file_menu.add_command(label="開く", command=self.open_file,
                                   accelerator="Ctrl+O")
        self.file_menu.add_command(label="上書き保存", command=self.overwrite,
                                   accelerator="Ctrl+S")
        self.file_menu.add_command(label="名前を付けて保存",
                                   command=self.save_file,
                                   accelerator="Ctrl+Shift+S")
        self.file_menu.add_command(label="最後に開いたファイルを開く",
                                   command=self.open_latest_file,
                                   accelerator="Ctrl+Shift+O")
        self.file_menu.add_command(label="終了",
                                   command=self.quit,
                                   accelerator="Esc")

        self.file_menu.bind_all("<Control-o>", self.open_file)
        self.file_menu.bind_all("<Shift-Control-S>", self.save_file)
        self.file_menu.bind_all("<Control-s>", self.overwrite)
        self.file_menu.bind_all("<Shift-Control-O>", self.open_latest_file)
        self.file_menu.bind_all("<Escape>", self.quit)

        self.edit_menu = tk.Menu(self.main_menu, tearoff=False)
        self.main_menu.add_cascade(label="編集", menu=self.edit_menu)
        self.edit_menu.add_command(label="置換", command=self.replace,
                                   accelerator="Ctrl+H")

    def replace(self):
        print(self.text_field.get(1.0, tk.END))

    def quit(self, *_):
        self.overwrite()
        exit(0)

    def open_check(self):
        if self.text_field.get(1.0, tk.END) != "\n":
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




if __name__ == "__main__":
    main()
