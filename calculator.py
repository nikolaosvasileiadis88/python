import tkinter as tk
# This line imports the tkinter module and gives it the name "tk" for easier reference later in the code.





class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Calculator")

        # create display
        self.display = tk.Entry(master, width=20, font=('Arial', 16))
        self.display.grid(row=0, column=0, columnspan=4, padx=5, pady=5)

        # create buttons
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+'
        ]

        # create and place buttons in grid
        r = 1
        c = 0
        for btn in buttons:
            cmd = lambda x=btn: self.click(x)
            tk.Button(master, text=btn, width=5, height=2, font=('Arial', 14), command=cmd)\
                .grid(row=r, column=c, padx=5, pady=5)
            c += 1
            if c > 3:
                c = 0
                r += 1

    def click(self, key):
        if key == '=':
            try:
                result = eval(self.display.get())
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, str(result))
            except:
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, "Error")
        elif key == 'C':
            self.display.delete(0, tk.END)
        else:
            self.display.insert(tk.END, key)

# create main window and calculator
root = tk.Tk()
app = Calculator(root)
root.mainloop()