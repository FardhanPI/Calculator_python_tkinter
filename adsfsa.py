import tkinter as tk
from tkinter import font


def sevenbutton(element,event=None):

    element_height=root.winfo_height()
    element_width=root.winfo_width()
    sdsdfgsg= element_width - root.winfo_width() * 0.05
    print("oogjogkjgkj")
    element.create_text( anchor=tk.E, text="7", fill="black", font=("Digital-7",35))


def resize_element(event=None):
    # Get the updated screen width and height
    screen_width = root.winfo_width()
    screen_height = root.winfo_height()

    # Calculate the desired size based on a percentage
    element_width = int(screen_width * 0.95)
    element_height = int(screen_height * 0.14)

    # Configure the size of the element
    element.configure(width=element_width, height=element_height)
    button1.configure(width=int(root.winfo_width()*0.024),height=int(root.winfo_height()*0.006),font=("Digital-7",15))
    button2.configure(width=int(root.winfo_width()*0.022),height=int(root.winfo_height()*0.006),font=("Digital-7",15))
    button3.configure(width=int(root.winfo_width()*0.01715),height=int(root.winfo_height()*0.006),font=("Digital-7",17),anchor='nw', padx=root.winfo_width()*0.1, pady=root.winfo_height()*0.047)
    button4.configure(width=int(root.winfo_width()*0.023),height=int(root.winfo_height()*0.0075),font=("Digital-7",15))
    button5.configure(width=int(root.winfo_width()*0.01715),height=int(root.winfo_height()*0.006),font=("Digital-7",17,"bold"),anchor='nw', padx=root.winfo_width()*0.11, pady=root.winfo_height()*0.047)
    button6.configure(width=int(root.winfo_width()*0.01715),height=int(root.winfo_height()*0.006),font=("Digital-7",17,"bold"),anchor='nw', padx=root.winfo_width()*0.11, pady=root.winfo_height()*0.047)
    button7.configure(width=int(root.winfo_width()*0.01715),height=int(root.winfo_height()*0.006),font=("Digital-7",17,"bold"),anchor='nw', padx=root.winfo_width()*0.11, pady=root.winfo_height()*0.047)
    button8.configure(width=int(root.winfo_width()*0.023),height=int(root.winfo_height()*0.0075),font=("Digital-7",15))
    button9.configure(width=int(root.winfo_width()*0.01715),height=int(root.winfo_height()*0.006),font=("Digital-7",17,"bold"),anchor='nw', padx=root.winfo_width()*0.11, pady=root.winfo_height()*0.047)
    button10.configure(width=int(root.winfo_width()*0.01715),height=int(root.winfo_height()*0.006),font=("Digital-7",17,"bold"),anchor='nw', padx=root.winfo_width()*0.11, pady=root.winfo_height()*0.047)
    button11.configure(width=int(root.winfo_width()*0.01715),height=int(root.winfo_height()*0.0075),font=("Digital-7",17,"bold"),anchor='nw', padx=root.winfo_width()*0.11, pady=root.winfo_height()*0.047)
    button12.configure(width=int(root.winfo_width()*0.023),height=int(root.winfo_height()*0.006),font=("Digital-7",15))
    button13.configure(width=int(root.winfo_width()*0.01715),height=int(root.winfo_height()*0.006),font=("Digital-7",17,"bold"),anchor='nw', padx=root.winfo_width()*0.11, pady=root.winfo_height()*0.047)
    button14.configure(width=int(root.winfo_width()*0.01715),height=int(root.winfo_height()*0.006),font=("Digital-7",17,"bold"),anchor='nw', padx=root.winfo_width()*0.11, pady=root.winfo_height()*0.047)
    button15.configure(width=int(root.winfo_width()*0.01715),height=int(root.winfo_height()*0.0075),font=("Digital-7",17,"bold"),anchor='nw', padx=root.winfo_width()*0.11, pady=root.winfo_height()*0.047)
    button16.configure(width=int(root.winfo_width()*0.023),height=int(root.winfo_height()*0.0075),font=("Digital-7",15))
    button17.configure(width=int(root.winfo_width()*0.023),height=int(root.winfo_height()*0.009),font=("Digital-7",15),anchor='nw', padx=root.winfo_width()*0.11, pady=root.winfo_height()*0.047)
    button18.configure(width=int(root.winfo_width()*0.023),height=int(root.winfo_height()*0.1),font=("Digital-7",17,"bold"),anchor='nw', padx=root.winfo_width()*0.11, pady=root.winfo_height()*0.047)
    button19.configure(width=int(root.winfo_width()*0.02),height=int(root.winfo_height()*0.009),font=("Digital-7",15,"bold"),anchor='nw', padx=root.winfo_width()*0.11, pady=root.winfo_height()*0.047)
    button20.configure(width=int(root.winfo_width()*0.01),height=int(root.winfo_height()*0.009),font=("Digital-7",15),anchor='nw', padx=root.winfo_width()*0.11, pady=root.winfo_height()*0.047)

    # Clear the canvas

    # Calculate the rightmost x-coordinate of the canvas

    # Create the text item on the canvas aligned to the right side

    element.place(x=root.winfo_width() * 0.02, y=root.winfo_height() * 0.02)


    button1.place(x=root.winfo_width()* 0.03,y=root.winfo_height() * 0.23)
    button2.place(x=root.winfo_width()* 0.26,y=root.winfo_height() * 0.23)
    button3.place(x=root.winfo_width()* 0.5,y=root.winfo_height() * 0.23)
    button4.place(x=root.winfo_width()* 0.73,y=root.winfo_height() * 0.23)
    button5.place(x=root.winfo_width()* 0.03,y=root.winfo_height() * 0.38)
    button6.place(x=root.winfo_width()* 0.26,y=root.winfo_height() * 0.38)
    button7.place(x=root.winfo_width()* 0.5,y=root.winfo_height() * 0.38)
    button8.place(x=root.winfo_width()* 0.73,y=root.winfo_height() * 0.38)
    button9.place(x=root.winfo_width()* 0.03,y=root.winfo_height() * 0.53)
    button10.place(x=root.winfo_width()* 0.26,y=root.winfo_height() * 0.53)
    button11.place(x=root.winfo_width()* 0.5,y=root.winfo_height() * 0.53)
    button12.place(x=root.winfo_width()* 0.73,y=root.winfo_height() * 0.53)
    button13.place(x=root.winfo_width()* 0.03,y=root.winfo_height() * 0.68)
    button14.place(x=root.winfo_width()* 0.26,y=root.winfo_height() * 0.68)
    button15.place(x=root.winfo_width()* 0.5,y=root.winfo_height() * 0.68)
    button16.place(x=root.winfo_width()* 0.73,y=root.winfo_height() * 0.68)
    button17.place(x=root.winfo_width()* 0.03,y=root.winfo_height() * 0.83)
    button18.place(x=root.winfo_width()* 0.26,y=root.winfo_height() * 0.83)
    button19.place(x=root.winfo_width()* 0.5,y=root.winfo_height() * 0.83)
    button20.place(x=root.winfo_width()* 0.73,y=root.winfo_height() * 0.83)

    return element_height, element_width

def on_enter(event):
    event.widget.configure(bg='#111111')  # Change the button background color on mouse enter

def on_leave(event):
    event.widget.configure(bg='black')  # Change the button background color on mouse leave


def copy_text():
    text = element.itemcget(text_item, "text")
    root.clipboard_clear()
    root.clipboard_append(text)


# Create a Tkinter root window
root = tk.Tk()

root.title("Calculator")
root.configure(bg="black")
root.iconphoto(True, tk.PhotoImage(file="img.png"))
root.minsize(width=350,height=500)

bold_font = font.Font(weight="bold")
# Create the element
element = tk.Canvas(root, bg="white", highlightthickness=0)
button1= tk.Button(root,text="%", fg="green",bg="black", border=0)
button2= tk.Button(root,text="C", fg="green",bg="black", border=0)
button3= tk.Button(root,text="←", fg="green",bg="black", border=0)
button4= tk.Button(root,text="÷", fg="green",bg="black", border=0)
button5= tk.Button(root,text="7", fg="green",bg="black", border=0, command=lambda: sevenbutton(element))
button6= tk.Button(root,text="8", fg="green",bg="black", border=0)
button7= tk.Button(root,text="9", fg="green",bg="black", border=0)
button8= tk.Button(root,text="×", fg="green",bg="black", border=0)
button9= tk.Button(root,text="4", fg="green",bg="black", border=0)
button10= tk.Button(root,text="5", fg="green",bg="black", border=0)
button11= tk.Button(root,text="6", fg="green",bg="black", border=0)
button12= tk.Button(root,text="−", fg="green",bg="black", border=0)
button13= tk.Button(root,text="1", fg="green",bg="black", border=0)
button14= tk.Button(root,text="2", fg="green",bg="black", border=0)
button15= tk.Button(root,text="3", fg="green",bg="black", border=0)
button16= tk.Button(root,text="+", fg="green",bg="black", border=0)
button17= tk.Button(root,text="-+", fg="green",bg="black", border=0)
button18= tk.Button(root,text="0", fg="green",bg="black", border=0)
button19= tk.Button(root,text=".", fg="green",bg="black", border=0)
button20= tk.Button(root,text="=", fg="green",bg="black", border=0)

button1.bind("<Enter>", on_enter)
button1.bind("<Leave>", on_leave)

button2.bind("<Enter>", on_enter)
button2.bind("<Leave>", on_leave)

button3.bind("<Enter>", on_enter)
button3.bind("<Leave>", on_leave)

# Repeat the pattern for buttons 4 to 20
button4.bind("<Enter>", on_enter)
button4.bind("<Leave>", on_leave)

button5.bind("<Enter>", on_enter)
button5.bind("<Leave>", on_leave)

button6.bind("<Enter>", on_enter)
button6.bind("<Leave>", on_leave)

button7.bind("<Enter>", on_enter)
button7.bind("<Leave>", on_leave)

button8.bind("<Enter>", on_enter)
button8.bind("<Leave>", on_leave)

button9.bind("<Enter>", on_enter)
button9.bind("<Leave>", on_leave)

button10.bind("<Enter>", on_enter)
button10.bind("<Leave>", on_leave)

button11.bind("<Enter>", on_enter)
button11.bind("<Leave>", on_leave)

button12.bind("<Enter>", on_enter)
button12.bind("<Leave>", on_leave)

button13.bind("<Enter>", on_enter)
button13.bind("<Leave>", on_leave)

button14.bind("<Enter>", on_enter)
button14.bind("<Leave>", on_leave)

button15.bind("<Enter>", on_enter)
button15.bind("<Leave>", on_leave)

button16.bind("<Enter>", on_enter)
button16.bind("<Leave>", on_leave)

button17.bind("<Enter>", on_enter)
button17.bind("<Leave>", on_leave)

button18.bind("<Enter>", on_enter)
button18.bind("<Leave>", on_leave)

button19.bind("<Enter>", on_enter)
button19.bind("<Leave>", on_leave)

button20.bind("<Enter>", on_enter)
button20.bind("<Leave>", on_leave)

# Bind the resize_element function to the "<Configure>" event
root.bind("<Configure>", resize_element)
element_width, element_height = resize_element()  # Obtain initial values

# Configure the element width and height
element.configure(width=element_width, height=element_height)

# Calculate the rightmost x-coordinate of the canvas
right_x = element_width + root.winfo_width() * 0.02


root.mainloop()
