from tkinter import *
root=Tk()
root.title("New window")
label=Label(root,text="Hello, Students!",font=("Arial Bold",40))
label.config(bg="green",fg="white")
def button_clicked():
    print("button Clicked")
button=Button(root,text="click,click,klik",command=button_clicked)
button.pack(padx=20,pady=20)

label.pack(side="right")
root.mainloop()