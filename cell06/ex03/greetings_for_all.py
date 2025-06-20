def greetings(name="noble stranger"):
    if not isinstance(name, str):
        print("Error! It was not a name.")
    else:
        print(f"Hello, {name}.")

greetings("Alexandra")
greetings("wil")
greetings()
greetings(42)