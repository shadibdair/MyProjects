# author - Shadi bdair
# Make a web browser using python.

import tkinter as tk # help us for GUI
from tkinter import *
import webbrowser

# Create the GUI
win = tk.Tk()
# Name of GUI
win.title("WebBrowser")
# Height&Width
win.geometry("520x520")

# ---------------------------------------
# This function when we called them it will show you the address of this website.
# ---------------------------------------
def google():
    webbrowser.open("www.google.com")

def youtube():
    webbrowser.open("www.youtube.com")

def amazon():
    webbrowser.open("www.amazon.com")

def facebook():
    webbrowser.open("www.facebook.com")
# ---------------------------------------


igoogle = PhotoImage(file="google.png")
google = tk.Button(win, image=igoogle, height=255, width=255, command=google)
google.grid(row=0, column=0)

iyoutube = PhotoImage(file="youtube.png")
youtube = tk.Button(win, image=iyoutube, height=255, width=255, command=youtube)
youtube.grid(row=0, column=1)

iamazon = PhotoImage(file="amazon.png")
amazon = tk.Button(win, image=iamazon, height=255, width=255, command=amazon)
amazon.grid(row=1, column=0)

ifacebook = PhotoImage(file="facebook.png")
facebook = tk.Button(win, image=ifacebook, height=255, width=255, command=facebook)
facebook.grid(row=1, column=1)

win.mainloop()
