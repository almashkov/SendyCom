import tkinter as tk
from tkinter import *
from create_button import *
from loop import *
from send_command import *

window = Tk()
window.title("SendyCom tool")
window.geometry("300x500")

info_frame = Frame(window,padx=1,pady=5)
info_frame.pack(fill=X)

info_lbl = Label(info_frame,text="Little tool for big deal")
info_lbl.grid(row=1, column=1)

# create_button(window,"Command", "Push to Send")
# loop_cb(window)
create_button(window,"focus far", "Push to Send")
create_button(window,"focus near", "Push to Send")
# create_button(window,"Command", "Push to Send")
# create_button(window,"Command", "Push to Send")


window.mainloop()