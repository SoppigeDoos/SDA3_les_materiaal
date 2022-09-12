from tkinter import *
from datetime import date, datetime

root = Tk()
root.title("assignment02")

def get_events():
    list_events = []
    with open('events.txt') as file:
        for line in file:
            line = line.rstrip('n')
            current_event = line.split(',')
            event_date = datetime.strptime(current_event[1], '%d / %m / %y')
            current_event[1] = event_date
            list_events.append(current_event)
    return list_events

def days_between_dates(date1, date2):
    time_between = str(date1-date2)
    number_of_days = time_between.split(' ')

c= Canvas(root)


root.mainloop()