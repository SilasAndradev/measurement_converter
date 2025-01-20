from tkinter import *
from tkinter import ttk

class APP:
    def __init__(self):
        self.master = Tk()
        self.master.iconbitmap("assets/icon.ico")
        self.master.geometry("800x600")
        self.master.title("Measurement Converter")

        self.color_background = "#363f4e"

        self.master.config(background = self.color_background)

        

    def run(self):
        self.master.mainloop()