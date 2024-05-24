def is_armstrong_number(number):
    # Convert number to string to count digits
    num_str = str(number)
    num_digits = len(num_str)
    
    # Calculate sum of digits raised to the power of num_digits
    total = sum(int(digit) ** num_digits for digit in num_str)
    
    # Check if the total is equal to the original number
    return total == number
    print(total)

for num in range(1, 2001):
    if is_armstrong_number(num):
        print(num)