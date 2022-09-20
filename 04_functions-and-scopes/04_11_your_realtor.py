# Write a function that prints out nicely formatted information about a
# real estate advertisement. The information can vary for every advertisement, which
# is why your function should be able to take an arbitrary amount of
# keyword arguments, and display them all in a list form with some 
# introductory information.

def realestate_ad(**kwargs):
    for key, value in kwargs.items():
        print(f" How to buy your {key} in {value}")

realestate_ad(mansion="USA", yurts="Kyrgyzstan", igloos="Canada")

# How to buy your property in country