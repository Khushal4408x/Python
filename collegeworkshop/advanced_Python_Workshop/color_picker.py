import tkinter as tk
from tkinter import colorchooser

def choose_color():
    color_code=colorchooser.askcolor(title="Choose color")
    print(color_code)

root=tk.Tk()
root.title("Color Picker Example")
root.geometry('800x200')

button =tk.Button(root,text="Choose color",command=choose_color)
button.pack()

root.mainloop()
