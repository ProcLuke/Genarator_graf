#!/usr/bin/env python3

from os.path import basename, splitext
import tkinter as tk

# from tkinter import ttk


class MyEntry(tk.Entry):
    def __init__(self, master=None, cnf={}, **kw):
        super().__init__(master, cnf, **kw)

        if not "textvariable" in kw:
            self.variable = tk.StringVar()
            self.config(textvariable=self.variable)
        else:
            self.variable = kw["textvariable"]

    @property
    def value(self):
        return self.variable.get()

    @value.setter
    def value(self, new: str):
        self.variable.set(new)

"""
class About(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent, class_=parent.name)
        self.config()

        btn = tk.Button(self, text="Konec", command=self.close)
        btn.pack()

    def close(self):
        self.destroy()
"""

class Application(tk.Tk):
    name = basename(splitext(basename(__file__.capitalize()))[0])
    name = "Foo"

    def __init__(self):
        super().__init__(className=self.name)
        self.title(self.name)
        self.bind("<Escape>", self.quit)
        self.lbl = tk.Label(self, text="Graf funkce")
        self.lbl.pack()

        self.fceVar = tk.IntVar()
        self.fceMin = tk.StringVar()
        self.fceMax = tk.StringVar()

        self.lblGenerator = tk.LabelFrame(self, text="Generuj graf fce",width=5)
        self.lblGenerator.pack()
        self.rbSin = tk.Radiobutton(self.lblGenerator, text="Sin", variable=self.fceVar, value="0").grid(column=0, row=1)
        self.rbLog = tk.Radiobutton(self.lblGenerator, text="Log", variable=self.fceVar, value="1").grid(column=0, row=2)
        self.rbExp = tk.Radiobutton(self.lblGenerator, text="Exp", variable=self.fceVar, value="2").grid(column=0, row=3)



        self.btn = tk.Button(self, text="Quit", command=self.quit)
        self.btn.pack()

    def fceGraf():
        pass

    """
    def about(self):
        window = About(self)
        window.grab_set()
    """

    def quit(self, event=None):
        super().destroy()


app = Application()
app.mainloop()
