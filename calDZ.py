import tkinter as tk

def click(text):
    if text == "C":
        entry.delete(0, tk.END)
    elif text == "=":
        try:
            result = eval(entry.get())
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Ошибка")
    else:
        entry.insert(tk.END, text)

root = tk.Tk()
root.title("Tk")

entry = tk.Entry(root, font=("dasdasd", 15) ,justify="right")
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

tk.Button(root, text="7", font=("Arial", 14), width=5, command=lambda: click("7")).grid(row=1, column=0)
tk.Button(root, text="8", font=("Arial", 14), width=5, command=lambda: click("8")).grid(row=1, column=1)
tk.Button(root, text="9", font=("Arial", 14), width=5, command=lambda: click("9")).grid(row=1, column=2)
tk.Button(root, text="/", font=("Arial", 14), width=5, command=lambda: click("/")).grid(row=1, column=3)

tk.Button(root, text="4", font=("Arial", 14), width=5, command=lambda: click("4")).grid(row=2, column=0)
tk.Button(root, text="5", font=("Arial", 14), width=5, command=lambda: click("5")).grid(row=2, column=1)
tk.Button(root, text="6", font=("Arial", 14), width=5, command=lambda: click("6")).grid(row=2, column=2)
tk.Button(root, text="*", font=("Arial", 14), width=5, command=lambda: click("*")).grid(row=2, column=3)

tk.Button(root, text="1", font=("Arial", 14), width=5, command=lambda: click("1")).grid(row=3, column=0)
tk.Button(root, text="2", font=("Arial", 14), width=5, command=lambda: click("2")).grid(row=3, column=1)
tk.Button(root, text="3", font=("Arial", 14), width=5, command=lambda: click("3")).grid(row=3, column=2)
tk.Button(root, text="-", font=("Arial", 14), width=5, command=lambda: click("-")).grid(row=3, column=3)

tk.Button(root, text="C", font=("Arial", 14), width=5, command=lambda: click("C")).grid(row=4, column=0)
tk.Button(root, text="0", font=("Arial", 14), width=5, command=lambda: click("0")).grid(row=4, column=1)
tk.Button(root, text="=", font=("Arial", 14), width=5, command=lambda: click("=")).grid(row=4, column=2)
tk.Button(root, text="+", font=("Arial", 14), width=5, command=lambda: click("+")).grid(row=4, column=3)

root.mainloop()