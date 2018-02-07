# Program for gathering data about you and collating.

#Ask the users name
name = input("What is your Name?: ")

#Ask the users age
age = input("How old are you?: ")

#Ask the users place
place = input("Where are you from?: ")

#Ask the users hobby
hobby = input("What is your hobby?: ")

#Create the string
string = "Hello {}, you are {} years old. Your are from {} and you like {}"

#Create the output and print it
output = string.format(name, age, place, hobby)
print(output)
