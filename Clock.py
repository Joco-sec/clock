# import tkinter module
from tkinter import *
from tkinter.ttk import *



# importing strftime to restrieve system's time
from time import strftime



# creating tkinter window
root = Tk()
root.title("Clock")

#function that displays time on label
def time():
    string = strftime("%H:%M:%S %p")
    lbl.config(text=string)
    lbl.after(1000, time)

# styling widget
lbl = Label(root, font=('sans', 40, 'bold'),
            background='black',
            foreground='white')


# Placing the clock at the center of the tkinter window
lbl.pack(anchor='center')
time()

mainloop()

