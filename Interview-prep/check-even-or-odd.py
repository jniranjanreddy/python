def check_even_odd(number):
    if number % 2 == 0:
        print(f"{number} is even.")
    else:
        print(f"{number} is odd.")

# Example usage:
number = int(input("Enter a number: "))

check_even_odd(10)  # Output: 10 is even.
check_even_odd(7)   # Output: 7 is odd.
check_even_odd(number)