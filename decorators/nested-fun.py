#!/usr/bin/env python3
def outer():
    print("Outer Function started.")

    def inner():
        print("Inner Function")

    inner()
    print("Outer function completed.")


outer()
