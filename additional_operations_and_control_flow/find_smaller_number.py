# Prog01: Create a program that ask user to input 2 numbers. 
# Print the smaller number.

# ------------------------------------------------------------------

# Phase 1: Planning

# - Objective: I will create a program to find the smaller of two user-input numbers.
# - Scope: Simple comparison which number is smaller.
# - Resources: Python

# ------------------------------------------------------------------

# Phase 2: Requirements Gathering/Analysis

# - Requirements:
#     - Accept two numerical inputs from user
#     - Compare two numbers and display the smaller number

# ------------------------------------------------------------------

# Phase 3: Design

# - Algorithm (input, process, output):
#     1. Get two numbers from user
#     2. Convert to integers (coz it reads as 'string')
#     3. Print the smaller number.

# ------------------------------------------------------------------

# Phase 4: Implementation/Development

# Ask user for inputs
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

if num1 < num2: # If true, it prints num1 as larger number
    print(f"{num1} is smaller.")
else: # If false, it prints num2 as larger number
    print(f"{num2} is smaller.")

# ------------------------------------------------------------------

# Phase 5: Testing

# Test Case 1: num1 < num2 (e.g., 5, 10) -> Should display 5
# Test Case 2: num1 > num2 (e.g., 7, 3) -> Should display 3
# Test Case 3: num1 = num2 (e.g., 5, 5) -> Should display 5

# ------------------------------------------------------------------

# Phase 6: Deployment

# Program is ready for use and can be executed as part of the batch 2

# ------------------------------------------------------------------

# Phase 7: Maintenance & Support

# I’d be grateful for any feedback, suggestions, or ideas to help improve things :)
# - Mike