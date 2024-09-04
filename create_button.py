import tkinter as tk
from tkinter import *
import socket
import time
from time import sleep

from click import command


def test_print(method):
    print(F"test method {method}")

def create_button(window, lbl_text, btn_text, ):
    button_frame = Frame(window, padx=10, pady=10)
    button_frame.pack(fill=X)
    button_lbl = Label(button_frame, text=lbl_text)
    button_lbl.grid(row=1, column=1)
    button = Button(button_frame, text=btn_text, command=lambda: test_print(button))
    button.grid(row=1, column=2)

