# Example 1: Exiting a loop when a condition is met

# for i in range(10):
#     print(i)
#     if i == 6:
#         break # It will print 0 to 5

# Example 2: Skipping an iteration in a loop
for i in range(10):
    
    if i == 6:
        print(i)
        continue # It will print 0 to 9 but skip 6
    
        
# x = 1
# if x > 5:
#     pass  # Placeholder for future implementation
# else:
#     print("x is not greater than 5")