# Prog04: Create a program that ask user to input 2 numbers. 
# Print the quotient of the two numbers without the decimal point.

# ------------------------------------------------------------------

# Phase 1: Planning

# - Objective: I will create a program to calculate the quotient without decimal point of two user-input numbers.
# - Scope: Simple division operation without decimal result.
# - Resources: Python

# ------------------------------------------------------------------

# Phase 2: Requirements Gathering/Analysis

# - Requirements:
#     - Accept two numerical inputs from user
#     - Divide two numbers and display the quotient without decimal point
#     - The divisor (second number) must not equal to 0, leading to 'undefined'

# ------------------------------------------------------------------

# Phase 3: Design

# - Algorithm (input, process, output):
#     1. Get two numbers from user
#        1.2. Convert to integers (coz it reads as 'string')
#     2. Check if divisor is equal to 0
#        2.1. Calculate quotient using division (integer division) operator
#     3. Print the result

# ------------------------------------------------------------------

# Phase 4: Implementation/Development

# Ask user for inputs
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

if num2 == 0: # Check if divisor (second number) is zero
    print("undefined")
else: # Calculate using integer division '//' and print the quotient 
    quotient = num1 // num2
    print(f"The quotient is: {quotient}")

# ------------------------------------------------------------------

# Phase 5: Testing

# Test Case 1: Even division (e.g., 10, 2) -> Should display 5
# Test Case 2: Uneven division (e.g., 5, 2) -> Should display 2
# Test Case 3: Division by zero (e.g., 5, 0) -> Should display 'undefined' message
# Test Case 4: Division with negative numbers (e.g., -10, 2) -> Should display -5
#    Test Case 4.1: Division with negative numbers (e.g., -10, -4) -> Should display 2

# ------------------------------------------------------------------

# Phase 6: Deployment

# Program is ready for use and can be executed as part of the batch 2

# ------------------------------------------------------------------

# Phase 7: Maintenance & Support

# I’d be grateful for any feedback, suggestions, or ideas to help improve things :)
# - Mike