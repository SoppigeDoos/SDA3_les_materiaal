from cgi import test
from tkinter import *

root = Tk()
root.title("assignment03")

def get_steden():
    list_steden = []
    with open ("data_capital_city.txt", "rt") as file:
        for line in file:
            line = line.rstrip('\n')
            current_stad = line.split('/')
            list_steden.append(current_stad)
    return list_steden

steden = get_steden()


def print():
    
    l2 = Label(root, text= "is de hoofstad van")
    l2.grid(row=3, column=0)



l1 = Label(root, text= "Type the name of a country?")

e1 = Entry(root)
b1 = Button(text= "OK", width= 6, command= print)
b2 = Button(text= "Cancel", width = 6)

l1.grid(row=0,column=0)
e1.grid(row=1,column=0)
b1.grid(row=2,column=0, sticky= "w", padx= 15, pady=5)
b2.grid(row=2,column=0, sticky= "e", padx= 15, pady=5)

root.mainloop()
