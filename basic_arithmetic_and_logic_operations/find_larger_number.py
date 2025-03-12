# Prog01: Create a program that ask user to input 2 numbers.
# Print the bigger number.

# ------------------------------------------------------------------

# Phase 1: Planning

# - Objective: I will create a program to find the larger of two user-input numbers.
# - Scope: Simple comparison which number is larger.
# - Resources: Python

# ------------------------------------------------------------------

# Phase 2: Requirements Gathering/Analysis

# - Requirements:
#     - Accept two numerical inputs from user
#     - Compare two numbers and display the larger number

# ------------------------------------------------------------------

# Phase 3: Design

# - Algorithm (input, process, output):
#     1. Get two numbers from user
#     2. Convert to integers (coz it reads as 'string')
#     3. Print the larger number.

# ------------------------------------------------------------------

# Phase 4: Implementation/Development

# Ask user for inputs
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

if num1 > num2: # If true, it prints num1 as larger number
    print(f"{num1} is bigger.")
else: # If false, it prints num2 as larger number
    print(f"{num2} is bigger.")

# ------------------------------------------------------------------

# Phase 5: Testing

# Test Case 1: num1 > num2 (e.g., 10, 5) -> Should display 10
# Test Case 2: num1 < num2 (e.g., 3, 7) -> Should display 7
# Test Case 3: num1 = num2 (e.g., 5, 5) -> Should display 5

# ------------------------------------------------------------------

# Phase 6: Deployment

# Program is ready for use and can be executed as part of the batch 1

# ------------------------------------------------------------------

# Phase 7: Maintenance & Support

# I’d be grateful for any feedback, suggestions, or ideas to help improve things :)
# - Mike