import tkinter as tk
from tkinter import messagebox

def convert(C):
    C = float(C) 
    F=(C*9/5)+32
    return F

def con():
    C = entry_c.get() 
    result = convert(C)
    messagebox.showinfo("Result", f"Converted Result: {result}")


Root=tk.Tk()
Root.title("C to F Converter")
Root.geometry("300x200")

label_c=tk.Label(Root, text="C 온도를 입력하세요")
label_c.grid(row=0, column=0, padx=5, pady=5)
entry_c=tk.Entry(Root, width=10)
entry_c.grid(row=0, column=1)

cvt_button=tk.Button(Root, text="Convert", command=con)
cvt_button.grid(row=2, column=1, padx=5, pady=5)



Root.mainloop()