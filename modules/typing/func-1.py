from typing import Optional

# def say_hi(name: Optional[str] = None):
#     if name is not None:
#             print(f"Hello {name}")
#     else:
#             print("Hello World")

# say_hi()
##################
class hello:
    def say_hi(self, name: Optional[str] = None):
        if name is not None:
            print(f"Hello {name}")
        else:
            print("Hello World")

H = hello()
H.say_hi()
#######################