from tkinter import *
import time

def digital():
    d=time.strftime("%H:%M:%S:%p")
    clock.config(text=d)
    clock.after(200,digital)

root=Tk()
root.title("digital clock")
clock=Label(root,font=("Liquid Crystal",100,"bold"),bg="gray")
clock.grid(row=2,column=1)
digital()
root.mainloop()