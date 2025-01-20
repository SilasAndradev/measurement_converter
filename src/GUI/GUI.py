from tkinter import *
from tkinter import ttk
from measure.meters import meters

class APP:
    def __init__(self):
        self.master = Tk()
        self.master.iconbitmap("assets/icon.ico")
        self.master.geometry("600x400")
        self.master.title("Measurement Converter")

        self.color_background = "#363f4e"
        self.color_background_text = "#87ceeb"

        self.frame_master = Frame(
            self.master, 
            background = self.color_background,
            width = self.master.winfo_screenwidth(),
            height = self.master.winfo_screenheight(),
            ).place(relx=0.5, rely=0.5, anchor=CENTER)

        self.option = [
            "Kilometer",
            "Meter",
            "Centimeter",
            "Millimeter",
            "Decimeter",
        ]
        self.MainWindow()
    def run(self):
        self.master.mainloop()

    def MainWindow(self):
        self.clicked_left = StringVar()
        self.clicked_left.set(self.option[0])

        self.clicked_right = StringVar()
        self.clicked_right.set(self.option[0])

        self.entry_left = Entry(self.frame_master, font=(0,10))
        self.entry_left.place(relx=0.5, rely=0.5, anchor=CENTER, relheight=0.05)


        self.dropdown_left = OptionMenu(self.frame_master, self.clicked_left, *self.option)
        self.dropdown_right = OptionMenu(self.frame_master, self.clicked_right, *self.option)

        self.dropdown_left.place(relx=0.4, rely=0.4, anchor=CENTER)
        self.dropdown_right.place(relx=0.6, rely=0.4, anchor=CENTER)

        self.convert_button = Button(self.frame_master, text='Convert', bg=self.color_background_text,
        font=('Helvetica', 20, 'bold'), foreground='black', command=self.value_to_list).place(relx=0.5, rely=0.7, anchor=CENTER)

    def value_to_list(self):
        self.list_left = (self.clicked_left.get(), self.entry_left.get())
        self.list_right = (self.clicked_right.get())

        meters().main(self.list_left, self.list_right)