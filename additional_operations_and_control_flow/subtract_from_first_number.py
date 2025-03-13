# Prog06: Create a program that ask user to input 10 numbers. 
# Print the result of the first number minus all of the remaining numbers.

# ------------------------------------------------------------------

# Phase 1: Planning

# - Objective: I will create a program to subtract nine numbers from the first number input by user.
# - Scope: Multiple subtraction operations.
# - Resources: Python

# ------------------------------------------------------------------

# Phase 2: Requirements Gathering/Analysis

# - Requirements:
#     - Accept ten numerical inputs from user
#     - Subtract the last 9 numbers from the first number

# ------------------------------------------------------------------

# Phase 3: Design

# - Algorithm (input, process, output):
#     1. Store the first number separately
#        1.2. Use a loop (for loop) to get the last 9 numbers
#        1.3. Convert to floats (coz it reads as 'string') for decimal support
#     2. Subtract each subsequent number from the first_number
#        2.1. Decrement last 9 user-input numbers from the first number
#     3. Print the result

# ------------------------------------------------------------------

# Phase 4: Implementation/Development

# First number
result = float(input("Enter the first number: "))
first_number = result

for i in range(9):
    num = float(input(f"Enter number {i+2}: ")) # Ask user for last 9 numbers
    result -= num # Decrement last 9 user-input numbers from the first number

# Print the result
print(f"The result of {first_number} minus all other numbers is: {result}")

# ------------------------------------------------------------------

# Phase 5: Testing

# Test Case 1: First number larger than sum of others -> Positive result
# Test Case 2: First number smaller than sum of others -> Negative result
# Test Case 3: Mix of positive and negative inputs
# Test Case 4: All zeros -> Should display 0

# ------------------------------------------------------------------

# Phase 6: Deployment

# Program is ready for use and can be executed as part of the batch 2

# ------------------------------------------------------------------

# Phase 7: Maintenance & Support

# I’d be grateful for any feedback, suggestions, or ideas to help improve things :)
# - Mike