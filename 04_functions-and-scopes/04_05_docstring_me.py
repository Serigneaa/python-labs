# Add a Google-style docstring to the function below. Your docstring
# should at least describe what it does, what arguments it takes,
# and what it returns.

def km_to_miles(km):
    """Convert km to miles.

    Args:
        km (float): the number of kilometres, with may be decimal

    Returns:
        str: The miles conversion of the kilometers
    """
    miles = km * 0.6
    return miles

print(km_to_miles.__doc__)
