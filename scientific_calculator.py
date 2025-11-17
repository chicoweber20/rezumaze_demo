import tkinter as tk
from math import sin, cos, tan, log10, log, sqrt, pi, e

class ScientificCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Scientific Calculator")
        self.root.resizable(False, False)

        self.expression = ""
        self.create_widgets()

    def create_widgets(self):
        # Display
        self.display = tk.Entry(
            self.root, font=("Consolas", 20), borderwidth=5,
            relief="ridge", justify="right"
        )
        self.display.grid(row=0, column=0, columnspan=6, padx=10, pady=10, ipady=10)

        # Button layout (text, row, col, colspan)
        buttons = [
            ("C",   1, 0, 1),  ("←",   1, 1, 1),  ("(",   1, 2, 1),  (")",   1, 3, 1), ("%",  1, 4, 1), ("/", 1, 5, 1),
            ("7",   2, 0, 1),  ("8",   2, 1, 1),  ("9",   2, 2, 1),  ("*",   2, 3, 1), ("sin", 2, 4, 1), ("cos", 2, 5, 1),
            ("4",   3, 0, 1),  ("5",   3, 1, 1),  ("6",   3, 2, 1),  ("-",   3, 3, 1), ("tan", 3, 4, 1), ("sqrt", 3, 5, 1),
            ("1",   4, 0, 1),  ("2",   4, 1, 1),  ("3",   4, 2, 1),  ("+",   4, 3, 1), ("ln",  4, 4, 1), ("log", 4, 5, 1),
            ("0",   5, 0, 2),  (".",   5, 2, 1),  ("^",   5, 3, 1),  ("x²",  5, 4, 1), ("=",  5, 5, 1),
            ("π",   6, 0, 3),  ("e",   6, 3, 3),
        ]

        for (text, row, col, colspan) in buttons:
            action = lambda x=text: self.on_button_click(x)
            tk.Button(
                self.root,
                text=text,
                width=5,
                height=2,
                font=("Consolas", 14),
                command=action
            ).grid(row=row, column=col, columnspan=colspan, sticky="nsew", padx=3, pady=3)

        # Make grid cells expand proportionally (optional, but nice)
        for i in range(7):
            self.root.rowconfigure(i, weight=1)
        for j in range(6):
            self.root.columnconfigure(j, weight=1)

    def on_button_click(self, char):
        if char == "C":
            self.expression = ""
            self.update_display()
        elif char == "←":
            self.expression = self.expression[:-1]
            self.update_display()
        elif char == "=":
            self.calculate_result()
        elif char == "sin":
            self.expression += "sin("
            self.update_display()
        elif char == "cos":
            self.expression += "cos("
            self.update_display()
        elif char == "tan":
            self.expression += "tan("
            self.update_display()
        elif char == "sqrt":
            self.expression += "sqrt("
            self.update_display()
        elif char == "log":  # base-10
            self.expression += "log10("
            self.update_display()
        elif char == "ln":   # natural log
            self.expression += "log("
            self.update_display()
        elif char == "x²":
            self.expression += "**2"
            self.update_display()
        elif char == "^":
            self.expression += "**"
            self.update_display()
        elif char == "π":
            self.expression += "pi"
            self.update_display()
        elif char == "e":
            self.expression += "e"
            self.update_display()
        else:
            self.expression += str(char)
            self.update_display()

    def update_display(self):
        self.display.delete(0, tk.END)
        self.display.insert(tk.END, self.expression)

    def calculate_result(self):
        try:
            # allowed names for eval
            allowed_names = {
                "sin": sin,
                "cos": cos,
                "tan": tan,
                "log10": log10,
                "log": log,   # natural log
                "sqrt": sqrt,
                "pi": pi,
                "e": e
            }
            result = eval(self.expression, {"__builtins__": None}, allowed_names)
            self.expression = str(result)
        except Exception:
            self.expression = "Error"
        finally:
            self.update_display()


if __name__ == "__main__":
    root = tk.Tk()
    app = ScientificCalculator(root)
    root.mainloop()
