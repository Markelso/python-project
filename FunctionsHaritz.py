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
    print("7--Drawing machine")
    print("9--Exit")

def addEvents (events):

    print("You have chosen to add an event.")


    event_num = int(input("How many events you want to add?"))

    i = 0
    while i < event_num:
        event = input("Enter the event you have and specify thr date.")
        events.append(event)
        i += 1
def drawingMachine ():

    print("WELCOME TO THE DRAWING MACHINE!")
    print("=========================")
    print("What do you want to draw?")
    print("=========================")
    print("1.- Drawing a pyramid.")
    print("2.- Drawing a triangle.")
    print("3.- Dawing a rombous.")
    print("4.- Drawing a number trinagle.")
    print("5.- Exit program.")
    print("Enter the number of the exercise: ")

    def pyramid ():
        altuera = input("Sartu piramidearen altuera.")


    printf("Enter the height of the pyramid: ");
    scanf("%d", & altuera);

    int
    i, j;


for (i=1;i <= altuera;i++){
for (j=1;j <= altuera-i;j++){
printf(" ");
}

for (j=1;j <= 2 * i-1;j++){
printf("*");
}
printf("\n");

}
}


while option != 5 :
            if option == 1:
            pyramid()

            if option == 2:
            triangle()

            if option == 3 :
            rombous()

            if option == 4:
            numberTriangle()

        option = input("Please, enter the number depending of the drawing you want to draw.")

    }