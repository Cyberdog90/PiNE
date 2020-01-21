# Ahoj Editor Ver. 21.1
import tkinter as tk
from tkinter import filedialog as fd
import os


def main():
    root = tk.Tk()
    _ = TextEditor(root)
    root.mainloop()


class TextEditor:
    def __init__(self, master):
        # window init
        master.geometry("1280x720")
        master.title("Ahoj Editor")
        master.iconbitmap("./data/icon.ico")
        self.master = master

        # flag variable
        self.current_open_file = None
        self.flag = True
        self.color = True
        self.emergency_call = True
        self.em_text = ""

        # font init
        self.font = "MS明朝"
        self.font_size = 18

        # Entry
        self.text_field = tk.Text(font=(self.font, self.font_size), undo=True)
        self.text_field.pack(fill=tk.BOTH, expand=1)

        # menu
        self.main_menu = tk.Menu()
        self.master.config(menu=self.main_menu)
        self.file_menu = tk.Menu(self.main_menu, tearoff=False)

        # menu function
        self.file_menu.bind_all("<Control-o>", self.open_file)
        self.file_menu.bind_all("<Shift-Control-O>", self.open_latest_file)
        self.file_menu.bind_all("<Shift-Control-S>", self.save_file)
        self.file_menu.bind_all("<Control-s>", self.overwrite)
        self.file_menu.bind_all("<Escape>", self.quit)
        self.file_menu.bind_all("<Shift-Control-C>", self.copy_line)
        self.file_menu.bind_all("<Shift-Control-D>", self.delete_line)
        self.file_menu.bind_all("<Shift-Control-N>", self.night_mode)
        self.file_menu.bind_all("<Shift-Control-M>", self.command_mode)
        self.file_menu.bind_all("<Shift-Control-E>", self.emergency)
        self.file_menu.bind_all("<Control-semicolon>", self.increment)
        self.file_menu.bind_all("<Control-minus>", self.decrement)

        self.debug()

    # bound function
    def open_file(self, *_):
        self.open_check()
        file_name = fd.askopenfilename(initialdir=os.getcwd(),
                                       title="開く",
                                       filetypes=(("テキスト文書", "*.txt"),
                                                  ("すべてのファイル", "*.*")))
        self.file_open(file_name=file_name)
        with open("log.txt", "w") as f:
            f.write(self.current_open_file)

    def open_latest_file(self, *_):
        self.open_check()
        if os.path.exists("{}\\log.txt".format(os.getcwd())):
            with open("log.txt", "r") as f:
                file_name = f.readline()
                self.file_open(file_name=file_name)
        else:
            self.open_file()

    def save_file(self, *_):
        with fd.asksaveasfile(initialdir=os.getcwd(),
                              mode="w",
                              defaultextension=".txt",
                              filetypes=(("テキスト文書", "*.txt"),
                                         ("すべてのファイル", "*.*"))) as f:
            self.current_open_file = f.name
            self.write_log()
            if f is None:
                return

            text2save = self.text_field.get(1.0, tk.END)
            f.write(text2save)

    def overwrite(self, *_):
        if self.current_open_file is not None:
            with open(self.current_open_file, "w") as f:
                text2save = self.text_field.get(1.0, tk.END)
                f.write(text2save)
        else:
            self.save_file()

    def quit(self, *_):
        if self.current_open_file is not None:
            self.overwrite()
        self.open_check()
        self.debug2()

        self.destroy()

    def copy_line(self, *_):
        text = self.get_text()
        self.text_field.insert("insert linestart", "{}\n".format(text))

    def delete_line(self, *_):
        self.text_field.delete("insert linestart", "insert lineend")

    def night_mode(self, *_):
        if self.color:
            self.text_field.config({"background": "Black"})
            self.text_field.config({"foreground": "White"})
            self.color = False
        else:
            self.text_field.config({"background": "White"})
            self.text_field.config({"foreground": "Black"})
            self.color = True

    def command_mode(self, *_):
        pass

    def emergency(self, *_):
        if self.emergency_call:
            self.em_text = self.text_field.get(1.0, tk.END)
            self.text_field.delete(1.0, tk.END)
            text = "TEST" * 2048
            self.text_field.insert(1.0, text)
            self.emergency_call = False
        else:
            self.text_field.delete(1.0, tk.END)
            self.text_field.insert(1.0, self.em_text)
            self.emergency_call = True

    def increment(self, *_):
        self.font_size += 2
        self.text_field.config({"font": (self.font, self.font_size)})

    def decrement(self, *_):
        self.font_size -= 2
        self.text_field.config({"font": (self.font, self.font_size)})

    # util function
    def get_text(self):
        return self.text_field.get("insert linestart", "insert lineend")

    def open_check(self):
        text = len(list("".join(self.text_field.get(1.0, tk.END))))
        if text != 1:
            self.overwrite()
        self.text_field.delete(1.0, tk.END)

    def file_open(self, file_name):
        try:
            with open(file_name, encoding="UTF-8") as file:
                for i in file:
                    self.text_field.insert(tk.END, i)
        except UnicodeDecodeError:
            with open(file_name) as file:
                for i in file:
                    self.text_field.insert(tk.END, i)
        self.current_open_file = file_name

    def write_log(self):
        with open("log.txt", "w") as f:
            f.write(self.current_open_file)

    def destroy(self):
        self.master.destroy()

    def debug(self):
        print(list(self.text_field.get(1.0, tk.END)))

    def debug2(self):
        print(list(self.text_field.get(1.0, tk.END)))


if __name__ == "__main__":
    main()
