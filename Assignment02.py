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
    return number_of_days[0]

c= Canvas(root)
c.create_text(100, 50, font = 'Arial 28 bold underline', text= 'Countdown Calendar')
events = get_events()
today = date.today()

for event in events:
    event_name = event[0]
    days_until = days_between_dates(events[1], today)
    display = 'It is %s days until %s' % (days_until, event_name)
    c.create_text(100, 100, font = 'Arial 28 bold', text = display )


root.mainloop()