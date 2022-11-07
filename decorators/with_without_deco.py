import nirulabs,os
def deco_for_add(func):
    def inner(name):
        names = ["cm", "pm", "minister"]
        if name.lower() in names:
            print("From inner Decoration")
            print(f"Welcome {name}, Please be Seated!!")
            print("Welcome", name.lower(), "Please be Seated!!")
        else:
            func(name)
    return inner

# @deco_for_add
def wish(a):
    print(f"Hello {a}")
decorated = deco_for_add(wish) # assigning
# wish("minister")
# decorated("cm") # This is call decorated inner function.
# decorated("minister")
  
