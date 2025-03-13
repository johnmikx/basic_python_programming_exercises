# Prog08: Create a program that ask user to input 10 numbers. 
# Print how many are odd numbers.

# ------------------------------------------------------------------

# Phase 1: Planning

# - Objective: I will create a program to count how many odd numbers are in ten user inputs.
# - Scope: Input processing, counting, and odd number detection.
# - Resources: Python

# ------------------------------------------------------------------

# Phase 2: Requirements Gathering/Analysis

# - Requirements:
#     - Accept ten numerical inputs from user
#     - Use a loop to get ten numbers from user
#     - Determine if each number is odd
#     - Count how many odd numbers were entered and display the final count

# ------------------------------------------------------------------

# Phase 3: Design

# - Algorithm (input, process, output):
#     1. Initialize
#        1.2. Use a loop (for loop) to get ten numbers
#        1.3. Convert to integers (coz it reads as 'string')
#     2. Check if each number is odd using modulo operator
#        2.1. Keep a counter for odd numbers
#     3. Print the final count

# ------------------------------------------------------------------

# Phase 4: Implementation/Development

# Initialize
odd_count = 0

for i in range(10):
    num = int(input(f"Enter number {i+1}: ")) # Ask user for inputs

    if num % 2 != 0: # Check if each number is odd
        odd_count += 1 # Counter for odd numbers

# Print the final count
print(f"The count of odd numbers is: {odd_count}")

# ------------------------------------------------------------------

# Phase 5: Testing

# Test Case 1: All odd numbers -> Should display 10
# Test Case 2: All even numbers -> Should display 0
# Test Case 3: Mix of odd and even numbers -> Should display correct count

# ------------------------------------------------------------------

# Phase 6: Deployment

# Program is ready for use and can be executed as part of the batch 1

# ------------------------------------------------------------------

# Phase 7: Maintenance & Support

# I’d be grateful for any feedback, suggestions, or ideas to help improve things :)
# - Mike