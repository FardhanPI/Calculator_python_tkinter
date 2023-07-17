from tkinter import *

def resize_element(event):
    # Get the updated screen width and height
    screen_width = root.winfo_width()
    screen_height = root.winfo_height()

    # Calculate the desired size based on a percentage
    element_width = int(screen_width * 0.1)  # 50% of the screen width
    element_height = int(screen_height * 0.01)  # 30% of the screen height

    # Configure the size of the element
    text_output.config(width=element_width, height=element_height)


root = Tk()
root.geometry("300x300")
root.title("Calculator")
root.configure(bg="#141212")
root.bind("<Configure>", resize_element)

text_output=Entry()
text_output.pack()

def labels():
    label =Label(root, text="HELLO")



button1 = Button(root,text="Button 1",command=labels)
button2 = Button(root,text="Button 2",command=labels)

button1.configure(bg="gray")
button2.configure(bg="gray")




root.mainloop()

