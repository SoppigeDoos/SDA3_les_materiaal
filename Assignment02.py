from datetime import date, datetime
from tkinter import *

root = Tk()
root.title("assignment02")

y=0

def get_events():
    list_events = []
    with open ("events.txt", "rt") as file:
        for line in file:
            line = line.rstrip('\n')
            current_Event = line.split(',')
            event_date = datetime.strptime(current_Event[1], '%d/%m/%y').date()
            current_Event[1] = event_date
            list_events.append(current_Event)
    return list_events

def days_between_dates(date1, date2):
    time_between = str(date1-date2)
    number_of_days = time_between.split(' ')
    return number_of_days[0]

events = get_events()
today = date.today()

for event in events:
    days_until = days_between_dates(event[1], today)
    print()


canvas = Canvas (root, height= 300, width= 300)
canvas.pack()
for event in events:
    dagen= days_between_dates(event[1], today)
    canvas.create_text(5, 5+y, anchor= "nw", text= (event[0], "nog", dagen, "dagen"))
    y=y+15


root.mainloop()