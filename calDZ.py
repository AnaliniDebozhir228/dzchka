import tkinter as tk

root = tk.Tk()

text_input = tk.Entry(root, width=20)
text_input.grid(row=0, column=0, columnspan=4)

def click(value):
    if value == "=":
        try:
            text_input.delete(0, tk.END)
            text_input.insert(0, eval(expression.get()))
        except:
            text_input.insert(0, "Ошибка")
    else:
        expression.set(expression.get() + value)

expression = tk.StringVar()

def click(value):
    if value == "=":
        try:
            result = eval(expression.get())
            text_input.delete(0, tk.END)
            text_input.insert(0, str(result))
            expression.set(str(result))
        except:
            text_input.delete(0, tk.END)
            text_input.insert(0, "Ошибка")
            expression.set("")
    else:
        expression.set(expression.get() + value)
        text_input.delete(0, tk.END)
        text_input.insert(0, expression.get())

buttons = [
    "1", "2", "3", "4", "5",
    "6", "7", "8", "9", "0",
    "+", "-", "*", "/", "="
]

for i, value in enumerate(buttons):
    tk.Button(
        root, text=value, width=5,
        command=lambda v=value: click(v)
    ).grid(row=1 + i // 5, column=i % 5)

root.mainloop()
