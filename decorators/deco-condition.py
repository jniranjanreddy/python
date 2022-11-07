def deco_for_add(func):
    def inner(name):
        names = ["cm", "pm", "minister"]
        if name.lower() in names:
            print(f"Welcome {name}, Please be Seated!!")
            print("Welcome", name.lower(), "Please be Seated!!")
        else:
            func(name)
    return inner

@deco_for_add
def add(a):
    print(f"Hello {a}")

add("PM")