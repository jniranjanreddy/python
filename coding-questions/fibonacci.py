def fibonacci(n):
    fib_sequence = [0, 1]
    while len(fib_sequence) < n:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence

# Example usage
# print(len(fibonacci(12)))
print(fibonacci(10))# Output: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

