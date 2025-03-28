#!/usr/bin/env python3

from os.path import basename, splitext
import tkinter as tk
from tkinter import messagebox, filedialog
import numpy as np
import matplotlib.pyplot as plt

class Application(tk.Tk):
    name = "Foo"

    def __init__(self):
        super().__init__(className=self.name)
        self.title(self.name)
        self.bind("<Escape>", self.quit)

        self.fceVar = tk.IntVar()
        self.fceMin = tk.StringVar()
        self.fceMax = tk.StringVar()
        self.AxisXVar = tk.StringVar()
        self.AxisYVar = tk.StringVar()
        self.fileVar = tk.StringVar()

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        self.lblGenerator = tk.LabelFrame(self, text="Generuj graf funkce")
        self.lblGenerator.grid(column=0, row=1, sticky="we", padx=10, pady=5)
        self.lblGenerator.grid_columnconfigure(1, weight=1)

        tk.Radiobutton(self.lblGenerator, text="Sin", variable=self.fceVar, value=0).grid(column=0, row=0, sticky="w")
        tk.Radiobutton(self.lblGenerator, text="Log", variable=self.fceVar, value=1).grid(column=0, row=1, sticky="w")
        tk.Radiobutton(self.lblGenerator, text="Exp", variable=self.fceVar, value=2).grid(column=0, row=2, sticky="w")

        self.fceMinEntry = tk.Entry(self.lblGenerator, textvariable=self.fceMin, width=7).grid(column=1, row=0, sticky="e")
        self.fceMaxEntry = tk.Entry(self.lblGenerator, textvariable=self.fceMax, width=7).grid(column=1, row=1, sticky="e")

        self.btnGraf = tk.Button(self, text="Vytvoř graf", command=self.fceGraf).grid(column=1, row=1, sticky="wens", padx=10, pady=5)


        self.lblFrame = tk.LabelFrame(self, text="Graf funkce ze souboru")
        self.lblFrame.grid(column=0, row=2, sticky="we", padx=10, pady=5)

        self.fileEntry = tk.Entry(self.lblFrame, textvariable=self.fileVar).grid(sticky="w")
        self.btnGrafFile = tk.Button(self.lblFrame, text="Vyber soubor", command=self.vyberSoubor).grid(sticky="e")
        self.btnGrafFile = tk.Button(self, text="Vytvoř graf", command=self.fceSoubor).grid(column=1, row=2, sticky="wens", padx=10, pady=5)


        self.lblAxis = tk.LabelFrame(self, text="Popisky os")
        self.lblAxis.grid(column=0, row=3, sticky="we", padx=10, pady=5)

        tk.Label(self.lblAxis, text="Osa X").grid(column=0, row=0)
        tk.Label(self.lblAxis, text="Osa Y").grid(column=0, row=1)

        self.AxisXEntry = tk.Entry(self.lblAxis, textvariable=self.AxisXVar, width=15).grid(column=1, row=0)
        self.AxisYEntry = tk.Entry(self.lblAxis, textvariable=self.AxisYVar, width=15).grid(column=1, row=1)


    def fceGraf(self):
        try:
            od = float(self.fceMin.get())
            do = float(self.fceMax.get())

            x = np.linspace(od, do, 500)
            if self.fceVar.get() == 0:
                y = np.sin(x)
            elif self.fceVar.get() == 1:
                x = x[x > 0]  # Filtrujeme záporné hodnoty
                y = np.log10(x)
            elif self.fceVar.get() == 2:
                y = np.exp(x)
            else:
                raise ValueError("Neplatná volba funkce")

            plt.figure()
            plt.plot(x, y)
            plt.xlabel(self.AxisXVar.get())
            plt.ylabel(self.AxisYVar.get())
            plt.grid(True)
            plt.show()

        except ValueError:
            messagebox.showerror(title='Chybné meze', message='Zadejte meze osy X\njako reálná čísla')

    def vyberSoubor(self):
        cesta = filedialog.askopenfilename(title="Vyberte soubor")
        if cesta:
            self.fileVar.set(cesta)

    def fceSoubor(self):
        try:
            cesta = self.fileVar.get()
            x, y = [], []

            with open(cesta, "r") as f:
                for radek in f:
                    cisla = radek.split()
                    try:
                        x.append(float(cisla[0]))
                        y.append(float(cisla[1]))
                    except ValueError:
                        messagebox.showerror(title="Chyba", message="Neplatná data v souboru!")
                        return

            plt.figure()
            plt.plot(x, y)
            plt.xlabel(self.AxisXVar.get())
            plt.ylabel(self.AxisYVar.get())
            plt.grid(True)
            plt.show()
        except Exception as e:
            messagebox.showerror(title="Chyba", message=f"Graf se nepodařilo vytvořit.\n{e}")

    def quit(self, event=None):
        self.destroy()


app = Application()
app.mainloop()
