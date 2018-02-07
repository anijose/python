#Create a list
user_list = ["Ani", "Manju", "Serah", "Evan", "Aji", "Raji", "Anu", "Soumya"]

#get the name input from the user
print("Hello! My name is Travis")
name = input("What is your name?: ").strip().capitalize()

#check if the name is there in the list
##if the name is there, ask if the user want it to be removed and act based on user response
if name in user_list:
    response = input("Would you like your name to be removed from system? (y/n): ").strip().lower()
    if response == "y":
        user_list.remove(name)
        print("{}, Your name has been removed from the system".format(name))
    elif response == "n":
        print("Sure {}, I will keep your name in the system".format(name))
    else:
        print("oh! I don't recognise that response.. GoodBye!!")
        
##if the name is not there, ask if the user want it to be added and act based on user response
else:
    print("hmmm...Seems like you are a first time visitor here")
    response = input("Would you like to add your name to the system? (y/n): ").strip().lower()
    if response == "y":
        user_list.append(name)
        print("{}, your name has been added to the system".format(name))
    elif response == "n":
        print("OK {}, no worries, see you next time".format(name))
    else:
        print("oh! I don't recognise that response.. GoodBye!!")
