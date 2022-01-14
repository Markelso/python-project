def printCalendar ():

    print("THE CALENDAR MENU (Choose a task typing its number!)")
    print("==================================================")
    print("1--Print calendar")
    print("2--Add event")
    print("3--Remove events")
    print("4--Search if a day have events or not")
    print("5--Search event by name")
    print("6--Show events")
    print("7--Playu Rock,Paper,Scissors")
    print("8--Show how many events are added.")
    print("7--Exit")

def addEvents ():

    print("You have chosen to add an event.")
    events = []

    event_num = int(input("How many events you want to add?"))

    i = 0
    while i < event_num:
        event = input("Enter the event you have and specify thr date.")
        events.append(event)
        i += 1
