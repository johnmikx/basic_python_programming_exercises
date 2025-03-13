# Prog05: Create a program that ask user to input 2 numbers. 
# Print the remainder when the first number is divided by the second number.

# ------------------------------------------------------------------

# Phase 1: Planning

# - Objective: I will create a program to calculate the remainder when the first number is divided by the second number.
# - Scope: Simple modulo operation.
# - Resources: Python

# ------------------------------------------------------------------

# Phase 2: Requirements Gathering/Analysis

# - Requirements:
#     - Accept two numerical inputs from user
#     - Display the remainder when first number is divided by second
#     - The divisor (second number) must not equal to 0, leading to 'undefined'

# ------------------------------------------------------------------

# Phase 3: Design

# - Algorithm (input, process, output):
#     1. Get two numbers from user
#        1.2. Convert to integers (coz it reads as 'string')
#     2. Check if divisor is equal to 0
#        2.1. Calculate remainder using modulo operator
#     3. Print the result

# ------------------------------------------------------------------

# Phase 4: Implementation/Development

# Ask user for inputs
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

if num2 == 0: # Check if divisor (second number) is zero
    print("undefined")
else: # Calculate using modulo '%' operator and print the remainder 
    remainder = num1 % num2
    print(f"The remainder is: {remainder}")

# ------------------------------------------------------------------

# Phase 5: Testing

# Test Case 1: Divisible numbers (e.g., 10, 2) -> Should display 0
# Test Case 2: Non-divisible numbers (e.g., 10, 3) -> Should display 1
# Test Case 3: Division by zero (e.g., 5, 0) -> Should display 'undefined' message
# Test Case 4: Negative numbers (e.g., -10, 3) -> Should display 2 (according to modulo rules)
#    Test Case 4 (Solution): -10 % 3 = 3 - (10 % 3) = 3 - 1 = 2

# ------------------------------------------------------------------

# Phase 6: Deployment

# Program is ready for use and can be executed as part of the batch 2

# ------------------------------------------------------------------

# Phase 7: Maintenance & Support

# I’d be grateful for any feedback, suggestions, or ideas to help improve things :)
# - Mike