from tkinter import *

root = Tk()
root.title("assignment01")

X1=4
Y1=30
X2=54
Y2=80

X3=4
Y3=90
X4=54
Y4=140

def close():
   root.destroy()
   root.quit()

canvas= Canvas (root, height= 180, width= 180)

t1 = canvas.create_text( 5, 5, text="Moest ik een vraag stellen?", fill="black", font=("times", 12), anchor= "nw", )

o1 = canvas.create_oval(X1,Y1,X2,Y2, fill= "blue", outline= "black") #cir1
o2 = canvas.create_oval(X1+60,Y1,X2+60,Y2, fill= "red", outline= "black") #cir2
o3 = canvas.create_oval(X1+120,Y1,X2+120,Y2, fill= "green", outline= "black") #cir 3

r1 = canvas.create_rectangle(X3,Y3,X4,Y4, fill= "green", outline= "black") #rec1
r2 = canvas.create_rectangle(X3+60,Y3,X4+60,Y4, fill= "blue", outline= "black") #rec2
r3 = canvas.create_rectangle(X3+120,Y3,X4+120,Y4, fill= "red", outline= "black") #rec3

exit = Button(canvas, text= "Close the Window", font=("Calibri",11,"bold"), command=close)
exit.place(x=30, y =150)


canvas.pack(expand=YES, fill=BOTH)
root.mainloop()