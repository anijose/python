#Obtain the email ID from the user
email = input("What is your email ID?: ").strip()

#Slice the user name
user = email[:email.index("@")]

#Slice the domain name
domain = email[email.index("@") + 1 :]

#Create the output message
output = "Your user name is {} and your domain name is {}".format(user, domain)

#Display the output message
print(output)
