# Write a program with three functions. Each function must call
# at least one other function and use the return value
# of that function to do something with it. You can have more
# than three functions, and they don't need to call each other
# in a circular way.

def greet(greeting, name):  # Positional arguments in definition
    sentence = f"{greeting}, {name}! How are you?"
    print(skydive("Listen", "be quiet"))
    return sentence

def skydive(step_1, step_2):
    print("For your own safety, please follow the instructions carefully:")
    print(f"1. {step_1}")
    print(f"2. {step_2}")

skydive("Take your parachute.", "JUMP!")

def write_letter(name, text):
    print(greet("hello", "David"))    
    print(text)
    print(f"Good bye {name}")

write_letter("David", "I am glad to see you in my office, you are always welcome")