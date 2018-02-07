#Program to intract with the user and allocate the film tickets

#Create a dictionary with Film names, min age requirement and number of seats available

film_list = {
    "Pulimurugan":{"age":3, "tickets":10},
    "Bahubali":{"age":18, "tickets":5},
    "Sing":{"age":3, "tickets":30},
    "Take Off":{"age":8, "tickets":16},
    "Avengers":{"age":12, "tickets":20}
    }
#Ask the user, which film they would like to watch & how may tickets
choice = input("Which film would you like to watch?: ").strip().title()
tickets_needed = int(input("How many tickets you need?: ").strip())

#Check the age requirement
if choice in film_list and tickets_needed <= film_list[choice]["tickets"]:
    if tickets_needed > 1:
        age = int(input("What is the age of youngest person in your group?: ").strip())
    else:
        age = int(input("How old are you?: ").strip())
    if age >= film_list[choice]["age"]:
        print("Enjoy the film")
    else:
        print("You are not old enough to watch this movie")
elif choice not in film_list:
    print("Sorry, that movie is not being displayed here")
elif tickets_needed >= film_list[choice]["tickets"]:
    print("Sorry.. Sold out")
