# Ask the user to input their name. Then print a nice welcome message
# that welcomes them personally to your script.
# If a user enters more than one name, e.g. "firstname lastname",
# then use only their first name to overstep some personal boundaries
# in your welcome message.

question = True


while question:
    name = input("Enter your name: ")

    if " " in name:
        result = name.find(" ")
        firt_name = name[0:result]
        print("Bienvenue " + firt_name)

    else:
        print("Bienvenue " + name)

# Work In Progress
