import tkinter as tk
from tkinter import *

from click import command

from create_button import *
from loop import *
from send_command import *

def log(log):
    print(f"{log}")

window = Tk()
window.title("SendyCom tool")
window.geometry("300x500")

info_frame = Frame(window,padx=1,pady=5)
info_frame.pack(fill=X)
info_lbl = Label(info_frame,text="Little tool for big deal")
info_lbl.grid(row=1, column=1)


plus_frame = Frame(window, padx=10, pady=10)
plus_frame.pack()
button = Button(plus_frame, text="+",activebackground='red', command=lambda: log("+"))
button.grid(row=2, column=1)


minus_frame = Frame(window, padx=10, pady=10)
minus_frame.pack()
button = Button(minus_frame, text=" - ", command=lambda: log("-"))
button.grid(row=1, column=2)

create_button(window,"Create a button", "Click")
# loop_cb(window)
create_button(window,"focus far", "Push to Send")
create_button(window,"focus near", "Push to Send")
# create_button(window,"Command", "Push to Send")
# create_button(window,"Command", "Push to Send")


window.mainloop()