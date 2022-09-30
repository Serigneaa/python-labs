def greet_many(greeting, *args):
    greetings = ""
    for name in args:
        sentence = f"{greeting}, {name}! How are you?"
        greetings += sentence + "\n"
    return greetings

print(greet_many("Hello", "Richard", "Sofia"))



