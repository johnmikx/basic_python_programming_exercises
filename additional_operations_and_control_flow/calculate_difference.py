# Prog03: Create a program that ask user to input 2 numbers. 
# Print the difference of the two numbers.

# ------------------------------------------------------------------

# Phase 1: Planning

# - Objective: I will create a program to calculate the difference of two user-input numbers.
# - Scope: Simple subtraction operation.
# - Resources: Python

# ------------------------------------------------------------------

# Phase 2: Requirements Gathering/Analysis

# - Requirements:
#     - Accept two numerical inputs from user
#     - Subtract two numbers and display the difference

# ------------------------------------------------------------------

# Phase 3: Design

# - Algorithm (input, process, output):
#     1. Get two numbers from user
#        1.2. Convert to floats (coz it reads as 'string') for decimal support
#     2. Calculate difference using subtraction operator
#     3. Print the result

# ------------------------------------------------------------------

# Phase 4: Implementation/Development

# Ask user for inputs
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Calculate and print the difference
difference = num1 - num2
print(f"The difference is: {difference}")

# ------------------------------------------------------------------

# Phase 5: Testing

# Test Case 1: First > Second (e.g., 10, 5) -> Should display 5
# Test Case 2: First < Second (e.g., 3, 7) -> Should display -4
# Test Case 3: Equal numbers (e.g., 5, 5) -> Should display 0
# Test Case 4: Mixed numbers (e.g., 5, -3) -> Should display 8
#    Test Case 4.1: Mixed numbers (e.g., -3, 5) -> Should display -8
# Test Case 5: Decimal numbers (e.g., 5.5, 2.5) -> Should display 3.0

# ------------------------------------------------------------------

# Phase 6: Deployment

# Program is ready for use and can be executed as part of the batch 2

# ------------------------------------------------------------------

# Phase 7: Maintenance & Support

# I’d be grateful for any feedback, suggestions, or ideas to help improve things :)
# - Mike