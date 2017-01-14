import tkinter as tk
from tkinter import messagebox


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        master.geometry("400x400")
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.hi_there = tk.Button(self)
        self.hi_there["text"] = "Welcome To Apna Bank!!\nClick to continue!!"
        self.hi_there["command"] = self.Menu
        self.hi_there.pack(side="top")

        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=root.destroy)
        self.quit.pack(side="top")

    def Menu(self):
        self.master.destroy()
        wn=tk.Tk()
        wn.geometry("200x200")
        b1=tk.Button(text="1] Open Account")
        b1.pack(side="top")
        b2=tk.Button(text="2] Check Balance!!")
        b2.pack(side="top")
        b=tk.Button(text="Quit",command=wn.destroy)
        b.pack(side="top")


        

root = tk.Tk()
app = Application(master=root)
app.mainloop()