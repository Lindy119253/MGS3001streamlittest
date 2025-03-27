from tkinter import *
from tkinter.ttk import *
from time import strftime

myClock = Tk()
myClock.title("Clock")

def time():
    string = strftime('%H:%M:%S %p')
    label.config(text=string)
    label.after(1000, time)
label = Label(myClock, font=("Arial Rounded Bold", 100))
label.pack(anchor = 'center')
time()

mainloop()
