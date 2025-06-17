from tkinter import *
window=Tk()
window.title("sum calci")
window.geometry("800x200")
def calculate_sum():
    num1=float(entry1.get())
    num2=float(entry2.get())

    total=num1+num2

    result_label.config(Text=f"sum: {total}")

label1=Label(window,text="Number 1:")
label1.grid(row=0,column=0,padx=10,pady=5)
    