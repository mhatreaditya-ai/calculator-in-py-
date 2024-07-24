import tkinter as tk

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Calculator")
        self.root.geometry("570x600+100+200")
        self.root.resizable(False, False)
        self.root.configure(bg="#17161b")

        self.equation = ""

        self.create_widgets()

    def create_widgets(self):
        self.label_result = tk.Label(self.root, width=25, height=2, text="", font=("arial", 30))
        self.label_result.pack()

        buttons = [
            {"text": "C", "command": self.clear, "bg": "#3697f5"},
            {"text": "/", "command": lambda: self.show("/"), "bg": "#2a2d36"},
            {"text": "%", "command": lambda: self.show("%"), "bg": "#2a2d36"},
            {"text": "*", "command": lambda: self.show("*"), "bg": "#2a2d36"},
            {"text": "7", "command": lambda: self.show("7"), "bg": "#3697f5"},
            {"text": "8", "command": lambda: self.show("8"), "bg": "#2a2d36"},
            {"text": "9", "command": lambda: self.show("9"), "bg": "#2a2d36"},
            {"text": "-", "command": lambda: self.show("-"), "bg": "#2a2d36"},
            {"text": "4", "command": lambda: self.show("4"), "bg": "#3697f5"},
            {"text": "5", "command": lambda: self.show("5"), "bg": "#2a2d36"},
            {"text": "6", "command": lambda: self.show("6"), "bg": "#2a2d36"},
            {"text": "+", "command": lambda: self.show("+"), "bg": "#2a2d36"},
            {"text": "1", "command": lambda: self.show("1"), "bg": "#3697f5"},
            {"text": "2", "command": lambda: self.show("2"), "bg": "#2a2d36"},
            {"text": "3", "command": lambda: self.show("3"), "bg": "#2a2d36"},
            {"text": "0", "command": lambda: self.show("0"), "bg": "#2a2d36"},
            {"text": ".", "command": lambda: self.show("."), "bg": "#2a2d36"},
            {"text": "=", "command": self.calculate, "bg": "#fe9037"},
        ]

        x = 10
        y = 100
        for i, button in enumerate(buttons):
            if i % 4 == 0 and i != 0:
                x = 10
                y += 100
            tk.Button(self.root, text=button["text"], width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg=button["bg"], command=button["command"]).place(x=x, y=y)
            x += 140

    def show(self, value):
        self.equation += value
        self.label_result.config(text=self.equation)

    def clear(self):
        self.equation = ""
        self.label_result.config(text=self.equation)

    def calculate(self):
        result = ""
        if self.equation != "":
            try:
                result = eval(self.equation)
            except:
                result = "error"
                self.equation = ""
        self.label_result.config(text=result)

if __name__ == "__main__":
    root = tk.Tk()
    calculator = Calculator(root)
    root.mainloop()
