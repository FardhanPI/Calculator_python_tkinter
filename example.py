import tkinter as tk
import datetime


def update_time():
    current_time = datetime.datetime.now().strftime("%H:%M:%S")
    time_label.config(text=current_time)
    window.after(1000, update_time)

# Create the Tkinter window
window = tk.Tk()
window.title("Digital Watch")

# Set the font style for the numbers
font_style = ("Arial", 48)

# Create the label widget for displaying the time
time_label = tk.Label(window, text="", font=font_style)
time_label.pack()

# Update the time every second
update_time()

# Start the Tkinter event loop
window.mainloop()
