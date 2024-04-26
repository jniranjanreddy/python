try:
    x = 10 / 0
except ZeroDivisionError:
    print("Error: Division by zero!")
else:
    print("Division successful!")

#example-2.py ends here



try:
    num = int(input("Enter a number: "))
except ValueError:
    print("Error: Invalid input! Please enter a valid number.")
else:
    print("You entered:", num)