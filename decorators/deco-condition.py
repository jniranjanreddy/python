def deco_for_add(func):
    def inner(name):
        if name.lower() == "rama":
            print("Shri Rama")
            print("God is Great")
        else:
            func(name)
    return inner

@deco_for_add
def add(a):
    print(f"print {a}")

add("RAMA")