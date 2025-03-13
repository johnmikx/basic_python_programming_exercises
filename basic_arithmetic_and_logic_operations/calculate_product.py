# Prog04: Create a program that ask user to input 2 numbers. 
# Print the product of the two numbers.

# ------------------------------------------------------------------

# Phase 1: Planning

# - Objective: I will create a program to calculate the product of two user-input numbers.
# - Scope: Simple multiplication operation.
# - Resources: Python

# ------------------------------------------------------------------

# Phase 2: Requirements Gathering/Analysis

# - Requirements:
#     - Accept two numerical inputs from user
#     - Multiply two numbers and display the product

# ------------------------------------------------------------------

# Phase 3: Design

# - Algorithm (input, process, output):
#     1. Get two numbers from user
#        1.2. Convert to floats (coz it reads as 'string') for decimal support
#     2. Calculate product using multiplication operator
#     3. Print the result

# ------------------------------------------------------------------

# Phase 4: Implementation/Development

# Ask user for inputs
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Calculate and print the product
product = num1 * num2
print(f"The product is: {product}")

# ------------------------------------------------------------------

# Phase 5: Testing

# Test Case 1: Positive numbers (e.g., 5, 10) -> Should display 50
# Test Case 2: Negative numbers (e.g., -3, -7) -> Should display 21
# Test Case 3: Mixed numbers (e.g., 5, -3) -> Should display -15
# Test Case 4: Decimal numbers (e.g., 2.5, 4) -> Should display 10.0
# Test Case 5: Multiply by zero (e.g., 5, 0) -> Should display 0

# ------------------------------------------------------------------

# Phase 6: Deployment

# Program is ready for use and can be executed as part of the batch 1

# ------------------------------------------------------------------

# Phase 7: Maintenance & Support

# I’d be grateful for any feedback, suggestions, or ideas to help improve things :)
# - Mike