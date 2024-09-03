# # TODO
from time import sleep
from tkinter import *
import time

root = Tk()


# def loop_cb(root):
def getBool():  # get rid of the event argument
    while True:
        print("true")
        sleep(1)
boolvar = BooleanVar()
boolvar.set(False)

cb = Checkbutton(root, text = "loop", variable = boolvar, command = getBool)
cb.pack()
# loop_cb(root)

root.mainloop()