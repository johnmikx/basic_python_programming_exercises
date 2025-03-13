# Prog07: Create a program that ask user to input 10 numbers. 
# Print the sum of all the numbers.

# ------------------------------------------------------------------

# Phase 1: Planning

# - Objective: I will create a program to calculate the sum of ten user-input numbers.
# - Scope: Simple addition operation.
# - Resources: Python

# ------------------------------------------------------------------

# Phase 2: Requirements Gathering/Analysis

# - Requirements:
#     - Accept ten numerical inputs from user
#     - Use a loop to get ten numbers from user and display the sum


# ------------------------------------------------------------------

# Phase 3: Design

# - Algorithm (input, process, output):
#     1. Initialize
#        1.2. Use a loop (for loop) to get ten numbers
#        1.3. Convert to floats (coz it reads as 'string') for decimal support
#     2. Calculate sum using addition operator
#        2.1. Increment every user-input numbers
#     3. Print the total

# ------------------------------------------------------------------

# Phase 4: Implementation/Development

# Initialize sum
total = 0

for i in range(10): 
    num = float(input(f"Enter number {i+1}: ")) # Ask user for inputs
    total += num # Increment every user-input numbers

# Print the sum
print(f"The sum of all numbers is: {total}")

# ------------------------------------------------------------------

# Phase 5: Testing

# Test Case 1: All positive numbers -> Should display correct sum
# Test Case 2: Mix of positive and negative numbers -> Should display correct sum
# Test Case 3: All zeros -> Should display 0
# Test Case 4: Decimal numbers -> Should display correct sum

# ------------------------------------------------------------------

# Phase 6: Deployment

# Program is ready for use and can be executed as part of the batch 1

# ------------------------------------------------------------------

# Phase 7: Maintenance & Support

# I’d be grateful for any feedback, suggestions, or ideas to help improve things :)
# - Mike