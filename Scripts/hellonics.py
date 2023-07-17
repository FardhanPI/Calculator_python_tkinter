import tkinter as tk

root = tk.Tk()
canvas = tk.Canvas(root, width=300, height=200, bg="black")
canvas.pack()

text = canvas.create_text(150, 100, text="Right-aligned", anchor=tk.E, fill="white")

root.mainloop()
