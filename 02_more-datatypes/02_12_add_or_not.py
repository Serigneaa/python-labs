# MEMORY GAME WITH SETS
# Continuously collect number input from a user with a `while` loop.
# Confirm that the input can be converted to an integer,
# then add it to a Python `set()`.
# If the element was already in the set, notify the user that their
# their input is a duplicate and deduct a point.
# If the user loses 5 points, quit the program.
# They win if they manage to create a set that has more than 10 items.

aset = set()
r_counter = 0
a_counter = 0

while r_counter<=5:
    number = input("Enter a number:")
    number = int(number)
    print(type(number))
    if type(number) == int:
        print("Cool that you enter an integer")
        alist = list(aset)
        if alist.count(number) == 0:
            aset = set(alist)
            #print(aset)
            aset = aset | {number}
            #print(aset)
            if len(aset) == 10:
                print("you win")
                print(aset)
                break

        else:
            print("your input is a duplicate, you will remove 1 point")
            r_counter -= r_counter
            if r_counter == 5:
                print("You lose")
    else:
        continue

