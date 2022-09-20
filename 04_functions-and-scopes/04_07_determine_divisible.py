# Write a script where you complete the following tasks:
# - define a function that determines whether the number is
#   divisible by 4 OR 7 and returns a boolean
# - define a function that determines whether a number is
#   divisible by both 4 AND 7 and returns a boolean
# - take in a number from the user between 1 and 1,000,000,000
# - call your functions, passing in the user input as the arguments,
#   and set their output equal to new variables 
# - print your the result variables with descriptive messages



num = input("Enter a number between 1 and 1,000,000,000: ")
num = int(num)

def div_4or7(num):
    if num%4 == 0 or num%7 == 0:
        result = True
        print(result)
        return result

    else:
        result = False
        print(result)
        return result

def div_4and7(num):
    if num%4 == 0 and num%7 == 0:
        result = True
        print(result)
        return result

    else:
        result = False
        print(result)
        return result

div_4or7(num)
div_4and7(num)

