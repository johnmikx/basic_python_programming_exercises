# Prog10: Create a program that ask user to input 2 numbers. 
# Print all the numbers between the two numbers.

# ------------------------------------------------------------------

# Phase 1: Planning

# - Objective: I will create a program to print all numbers between two user-input numbers.
# - Scope: Range-based loop.
# - Resources: Python

# ------------------------------------------------------------------

# Phase 2: Requirements Gathering/Analysis

# - Requirements:
#     - Accept two numerical inputs from user
#     - Print all numbers between the two inputs (inclusive)
#     - Handle case where second number is smaller than first

# ------------------------------------------------------------------

# Phase 3: Design

# - Algorithm (input, process, output):
#     1. Get two numbers from user
#        1.2. Convert to integers (coz it reads as 'string')
#     2. Use 'if statement' to determine smaller and larger number
#        2.1. Use `for loop` to print all numbers in range
#        2.2. Increment by 1 for inclusive numbers in between
#     3. Print the result

# ------------------------------------------------------------------

# Phase 4: Implementation/Development

# Ask user for inputs
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

if num1 > num2: # Ensuring num1 is the smaller number
    num1, num2 = num2, num1

print(f"Numbers between {num1} and {num2}:") # Title
for num in range(num1 + 1, num2): # Increment by 1 for inclusive numbers in between
    print(num, end=" ") # Print all numbers between num1 and num2

# ------------------------------------------------------------------

# Phase 5: Testing

# Test Case 1: First < Second (e.g., 5, 10) -> Should display 6 7 8 9
# Test Case 2: First > Second (e.g., 10, 5) -> Should display 6 7 8 9
# Test Case 3: Equal numbers (e.g., 5, 5) -> Should display nothing
#    Test Case 3.1: Near unequal numbers (e.g., 4, 5) -> Should display nothing
# Test Case 4: Negative numbers (e.g., -3, 3) -> Should display -2 -1 0 1 2 

# ------------------------------------------------------------------

# Phase 6: Deployment

# Program is ready for use and can be executed as part of the batch 2

# ------------------------------------------------------------------

# Phase 7: Maintenance & Support

# I’d be grateful for any feedback, suggestions, or ideas to help improve things :)
# - Mike