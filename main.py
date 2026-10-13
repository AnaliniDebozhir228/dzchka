import tkinter as tk

root = tk.Tk()
root.geometry("300x300")

positions = [(125, 10), (200, 40), (230, 115), (200, 190),
             (125, 220), (50, 190), (20, 115), (50, 40)]

i = 0
while i < 8:
    x, y = positions[i]
    tk.Button(root).place(x=x, y=y)
    i += 1

root.mainloop()
