from tkinter import *
from tkinter import ttk

class APP:
    def __init__(self):
        self.master = Tk()
        self.master.iconbitmap("assets/icon.ico")
        self.master.geometry("800x600")
        self.master.title("Measurement Converter")

        self.color_background = "#363f4e"


        self.frame_master = Frame(
            self.master, 
            background = self.color_background,
            width = 800,
            height= 600
            )

        self.option = [
            "Kilometer"
            "Meter",
            "Centimeter",
            "Millimeter",
            "Decimeter",
        ]
        self.MainWindow()
    def run(self):
        self.master.mainloop()

    def MainWindow(self):
        clicked = StringVar()
        clicked.set(self.option[0])

        drop = OptionMenu(self.frame_master, clicked, *self.option)
        drop.pack()