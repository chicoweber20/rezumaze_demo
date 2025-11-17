import tkinter as tk
import math

class ScientificCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Scientific Calculator")
        self.root.geometry("480x600+200+100")  # Good size, placed on screen

        self.expression = ""
        self.display_var = tk.StringVar()
        self.display_var.set("0")

        self.create_widgets()

    def create_widgets(self):
        # BIG, CLEAR DISPLAY
        display = tk.Entry(
            self.root,
            textvariable=self.display_var,
            font=("Consolas", 28),
            borderwidth=10,
            relief="sunken",
            bg="#f2f2f2",
            fg="black",
            justify="right"
        )
        display.grid(row=0, column=0, columnspan=6, padx=10, pady=20, ipady=15, sticky="nsew")

        buttons = [
            ("C",1,0),("←",1,1),("(",1,2),(")",1,3),("%",1,4),("/",1,5),
            ("7",2,0),("8",2,1),("9",2,2),("*",2,3),("sin",2,4),("cos",2,5),
            ("4",3,0),("5",3,1),("6",3,2),("-",3,3),("tan",3,4),("sqrt",3,5),
            ("1",4,0),("2",4,1),("3",4,2),("+",4,3),("ln",4,4),("log",4,5),
            ("0",5,0),(".",5,1),("^",5,2),("x²",5,3),("=",5,4),("π",5,5),
            ("e",6,0),
        ]

        for (text, row, col) in buttons:
            btn = tk.Button(
                self.root,
                text=text,
                width=6,
                height=2,
                font=("Consolas", 14),
                command=lambda x=text: self.on_button_click(x)
            )
            btn.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")

        # Make rows/columns expand a bit
        for r in range(7):
            self.root.rowconfigure(r, weight=1)
        for c in range(6):
            self.root.columnconfigure(c, weight=1)

    def on_button_click(self, char):
        if char == "C":
            self.expression = ""
        elif char == "←":
            self.expression = self.expression[:-1]
        elif char == "=":
            self.calculate_result()
            return
        elif char == "sin":
            self.expression += "math.sin("
        elif char == "cos":
            self.expression += "math.cos("
        elif char == "tan":
            self.expression += "math.tan("
        elif char == "sqrt":
            self.expression += "math.sqrt("
        elif char == "ln":
            self.expression += "math.log("
        elif char == "log":
            self.expression += "math.log10("
        elif char == "x²":
            self.expression += "**2"
        elif char == "^":
            self.expression += "**"
        elif char == "π":
            self.expression += "math.pi"
        elif char == "e":
            self.expression += "math.e"
        else:
            self.expression += str(char)

        self.update_display()

    def update_display(self):
        if self.expression == "":
            self.display_var.set("0")
        else:
            self.display_var.set(self.expression)

    def calculate_result(self):
        try:
            # Evaluate using math module
            result = eval(self.expression, {"__builtins__": None, "math": math})
            self.expression = str(result)
        except Exception:
            self.expression = ""
            self.display_var.set("Error")
            return

        self.update_display()


if __name__ == "__main__":
    root = tk.Tk()
    ScientificCalculator(root)
    root.mainloop()
