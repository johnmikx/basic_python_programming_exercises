# Prog02: Create a program that ask user to input 2 numbers. 
# Print "Not Equal" when the numbers are not the same.

# ------------------------------------------------------------------

# Phase 1: Planning

# - Objective: I will create a program to check if two user-input numbers are not equal.
# - Scope: Simple inequality of two numbers.
# - Resources: Python

# ------------------------------------------------------------------

# Phase 2: Requirements Gathering/Analysis

# - Requirements:
#     - Accept two numerical inputs from user
#     - Compare two numbers and display "Not Equal" when numbers are different

# ------------------------------------------------------------------

# Phase 3: Design

# - Algorithm (input, process, output):
#     1. Get two numbers from user
#        1.2. Convert to integers (coz it reads as 'string')
#     2. Use `if-else` to check inequality
#     3. Print the result

# ------------------------------------------------------------------

# Phase 4: Implementation/Development

# Ask user for inputs
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Check if numbers are not equal
if num1 != num2:
    print("Not Equal")
else:
    print("Equal")

# ------------------------------------------------------------------

# Phase 5: Testing

# Test Case 1: Different numbers (e.g., 3, 7) -> Should display "Not Equal"
# Test Case 2: Equal numbers (e.g., 5, 5) -> Should display "Equal"

# ------------------------------------------------------------------

# Phase 6: Deployment

# Program is ready for use and can be executed as part of the batch 2

# ------------------------------------------------------------------

# Phase 7: Maintenance & Support

# I’d be grateful for any feedback, suggestions, or ideas to help improve things :)
# - Mike