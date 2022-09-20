# How can you call the function defined below using the given
# dictionary as its input.
# You shouldn't explicitly access the dict values, but use
# dictionary unpacking when passing the argument instead.

# WRONG Code
# def congratulate(name, age):
#     return f"Today {name} is {age} years old.\nHappy Birthday!"

# user = {"name": "Adelheid", "age": 22}

# RIGHT Code
def congratulate(**kwargs):
    for key, value in kwargs.items():
        print(f"Today {key} is {value} years old.\nHappy Birthday!")

congratulate(Adelheid = 22, Serigne=30)


