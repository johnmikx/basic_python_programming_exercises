# Prog06: Create a program that ask user to input 2 numbers. 
# Print the result when the first number is raised to the second number.

# ------------------------------------------------------------------

# Phase 1: Planning

# - Objective: I will create a program to calculate the first number raised to the power of the second number.
# - Scope: Simple exponentiation operation.
# - Resources: Python

# ------------------------------------------------------------------

# Phase 2: Requirements Gathering/Analysis

# - Requirements:
#     - Accept two numerical inputs from user
#     - Display the result when the first number is raised to the power of the second number

# ------------------------------------------------------------------

# Phase 3: Design

# - Algorithm (input, process, output):
#     1. Get two numbers from user (first number as base and second number as exponent)
#        1.2. Convert to floats (coz it reads as 'string') for decimal support
#     2. Calculate result using exponentiation operator
#     3. Print the result

# ------------------------------------------------------------------

# Phase 4: Implementation/Development

# Ask user for inputs
base = float(input("Enter first number: "))
exponent = float(input("Enter second number: "))

# Calculate and print the result
result = base ** exponent
print(f"{base} raised to {exponent} is: {result}")

# ------------------------------------------------------------------

# Phase 5: Testing

# Test Case 1: Positive base, positive exponent (e.g., 2, 3) -> Should display 8.0
# Test Case 2: Negative base, even exponent (e.g., -2, 2) -> Should display 4.0
#    Test Case 2.1: Negative base, odd exponent (e.g., -2, 3) -> Should display -8.0
# Test Case 3: Positive base, negative exponent (e.g., 2, -3) -> Should display 0.125
#    Test Case 3.1: Negative base, negative even exponent (e.g., -2, -2) -> Should display 0.25
#    Test Case 3.2: Negative base, negative odd exponent (e.g., -2, -3) -> Should display -0.125
# Test Case 4: Any number to power 0 (e.g., 5, 0) -> Should display 1.0
# Test Case 5: Fractional/Decimal exponent (e.g., 4, 0.5) -> Should display 2.0

# ------------------------------------------------------------------

# Phase 6: Deployment

# Program is ready for use and can be executed as part of the batch 1

# ------------------------------------------------------------------

# Phase 7: Maintenance & Support

# I’d be grateful for any feedback, suggestions, or ideas to help improve things :)
# - Mike