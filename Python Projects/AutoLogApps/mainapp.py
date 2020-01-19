import tkinter as tk # help us for GUI
from tkinter import filedialog, Text # Fileddialog - help us pick apps || Text - is gonna help us display some text.
import os # os - Allows us to run the app that we're gonna add to our tap.
import subprocess, sys


# Root have the body and basically this holds the app , the structure
root = tk.Tk()
# To appends all the files we're adding to it
apps = []

# Will check if we have this file save.txt and read it then print the temporary files
if os.path.isfile('save.txt'):
    with open('save.txt', 'r') as f:
        tempApps = f.read()
        tempApps = tempApps.split(',')
        # To strip out all the empty spaces 
        apps = [x for x in tempApps if x.strip()]
# This function for open files and to see file .exe and all files names you will have in your device.
def addApp():

    # Is giving us access to everything that attached to our frame in this case all the label.
    for widget in frame.winfo_children():
        # That gonna destroy everything beforehand and then attach update version of it.
        widget.destroy()

    filename = filedialog.askopenfilename(initialdir="/", title="Select File", filetypes=(("executables","*.exe"), ("all files", "*.*")))

    apps.append(filename)
    print(filename)
    for app in apps:
        label = tk.Label(frame, text=app, bg="red")
        label.pack()


# This function to run the files that selected
def runApps():
    # Will run all the files as loop
    for app in apps:
        if sys.platform == "win32":
            os.startfile(app)
        else:
            opener="open" if sys.platform == "darwin" else "xdg-open"
            subprocess.call([opener,app])

# Inside the box the Height, Width and color: GREEN. 
canvas = tk.Canvas(root, height=500, width=500, bg="#263D42")
# To attach it on screen
canvas.pack()

# Create inside the box another box in the center.
frame = tk.Frame(root, bg="white")
frame.place(relwidth=0.8, relheight=0.7, relx=0.1, rely=0.1)

# Create button name - Open File 
openFile = tk.Button(root, text="Open File", padx=10, pady=5, fg="white", bg="#263D42", command=addApp)
# To attach it on screen
openFile.pack()
# Create button name - Run Apps
runApps = tk.Button(root, text="Run Apps", padx=10, pady=5, fg="white", bg="#263D42", command=runApps)
# To attach it on screen
runApps.pack()

# To see all the apps on screen
for app in apps:
    label = tk.Label(frame, text=app)
    label.pack()

root.mainloop()

# Whenever we close our app it's gonna save a text file  we're gonna write 
# that txt file as F and with F we can write basically all the apps that we saved up in this.
with open('save.txt', 'w') as f:
    for app in apps:
        f.write(app + ',')
