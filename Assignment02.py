from time import strftime
from tkinter import *

root = Tk()
root.title("assignment02")

c= Canvas(root)
c.pack()

time_string = strftime("%d / %m / %Y")

c.create_text(50, 10, text= time_string, fill="black", font=("times"))


root.mainloop()