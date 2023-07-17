from tkinter import Tk, Canvas, Button

def resize_element(root, event=None):
    screen_width = root.winfo_width()
    screen_height = root.winfo_height()

    # Calculate the element width and height based on screen dimensions
    element_width = screen_width // 4
    element_height = screen_height // 5

    return element_width, element_height

def add_text(canvas):
    element_width, element_height = resize_element(root)
    canvas.create_text(element_width, element_height, text="Hello, World!", fill="black")

root = Tk()
root.title("Add Text to Canvas")

canvas = Canvas(root,bg="red", width=200, height=200)
canvas.pack()

button = Button(root, text="Add Text", command=lambda: add_text(canvas))
button.pack()

root.mainloop()
