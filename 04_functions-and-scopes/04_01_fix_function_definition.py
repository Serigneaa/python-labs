# The following function definition has a whole lot of bugs in it!
# Run the script and follow Python's error hints to fix them all.
# After your fixes, the function should allow you to take a name as an input
# and return a greeting message that you can save to a variable.

# WRONG Code
# function say_hello("name"):
#        return print(f"Hello {name}!")

# greeting = hello(name)
# print(greeting)

# RIGHT Code
def say_hello(name):
        greeting = f"Hello {name}!"
        print(greeting)
        return greeting

say_hello("Isaac")
