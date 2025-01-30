from tkinter import messagebox

class meters:
    def main(self, list_left, list_right):
        self.type_left = list_left[0]
        try:
            self.value_left = float(list_left[1])
        except Exception as e:
            messagebox.showerror("ERROR!", "Enter a number!")

        self.type_right = list_right[0]

        if self.type_left == "Kilometer":
            self.Kilometer()

        elif self.type_left == "Meter":
            self.Meter()

        elif self.type_left == "Centimeter":
            self.Centimeter()

        elif self.type_left == "Millimeter":
            self.Millimeter()

        elif self.type_left == "Decimeter":
            self.Decimeter()



    def Kilometer(self):
        if self.type_right == "Kilometer":
            messagebox.showinfo("Result", f"Result is {self.value_left}")

        elif self.type_right == "Meter":
            messagebox.showinfo("Result", f"Result is {self.value_left * 1000}")

        elif self.type_right == "Centimeter":
            messagebox.showinfo("Result", f"Result is {self.value_left * 1000 * 100}")

        elif self.type_right == "Millimeter":
            messagebox.showinfo("Result", f"Result is {self.value_left * 1000 * 1000}")

        elif self.type_right == "Decimeter":
            messagebox.showinfo("Result", f"Result is {self.value_left * 10 * 1000}")

        else:
            messagebox.showerror("ERROR", "Anything is error")

    def Meter(self):
        if self.type_right == "Kilometer":
            messagebox.showinfo("Result", f"Result is {self.value_left / 1000}")

        elif self.type_right == "Meter":
            messagebox.showinfo("Result", f"Result is {self.value_left}")

        elif self.type_right == "Centimeter":
            messagebox.showinfo("Result", f"Result is {self.value_left * 100}")

        elif self.type_right == "Millimeter":
            messagebox.showinfo("Result", f"Result is {self.value_left * 1000}")

        elif self.type_right == "Decimeter":
            messagebox.showinfo("Result", f"Result is {self.value_left * 10}")

        else:
            messagebox.showerror("ERROR", "Anything is error")

    def Centimeter(self):
        if self.type_right == "Kilometer":
            messagebox.showinfo("Result", f"Result is {self.value_left / 100000}")

        elif self.type_right == "Meter":
            messagebox.showinfo("Result", f"Result is {self.value_left / 100}")

        elif self.type_right == "Centimeter":
            messagebox.showinfo("Result", f"Result is {self.value_left}")

        elif self.type_right == "Millimeter":
            messagebox.showinfo("Result", f"Result is {self.value_left / 10}")

        elif self.type_right == "Decimeter":
            messagebox.showinfo("Result", f"Result is {self.value_left * 10}")

        else:
            messagebox.showerror("ERROR", "Anything is error")

    def Millimeter(self):
        if self.type_right == "Kilometer":
            messagebox.showinfo("Result", f"Result is {self.value_left / 1000000}")

        elif self.type_right == "Meter":
            messagebox.showinfo("Result", f"Result is {self.value_left / 1000}")

        elif self.type_right == "Centimeter":
            messagebox.showinfo("Result", f"Result is {self.value_left / 10}")

        elif self.type_right == "Millimeter":
            messagebox.showinfo("Result", f"Result is {self.value_left}")

        elif self.type_right == "Decimeter":
            messagebox.showinfo("Result", f"Result is {self.value_left / 100}")

        else:
            messagebox.showerror("ERROR", "Anything is error")

    def Decimeter(self):
        if self.type_right == "Kilometer":
            messagebox.showinfo("Result", f"Result is {self.value_left / 1000 / 10}")

        elif self.type_right == "Meter":
            messagebox.showinfo("Result", f"Result is {self.value_left / 10}")

        elif self.type_right == "Centimeter":
            messagebox.showinfo("Result", f"Result is {self.value_left / 10}")

        elif self.type_right == "Millimeter":
            messagebox.showinfo("Result", f"Result is {self.value_left * 100}")

        elif self.type_right == "Decimeter":
            messagebox.showinfo("Result", f"Result is {self.value_left}")

        else:
            messagebox.showerror("ERROR", "Anything is error")
