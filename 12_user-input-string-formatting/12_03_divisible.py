# Write a program that takes a number between 1 and 1,000,000,000
# from the user and determines whether it is divisible by 3 using an `if` statement.
# Print the result.

user_input = input("Enter a number between 1 and 1,000,000,000: ")
number = int(user_input)
    
if number%3 == 0:
    print(number)

else:
    print("Enter just a integer number")

# Work In Progress
